#!/usr/bin/env python3
"""Capture and consume an exact legacy PID-file identity during cutover."""

import argparse
import errno
import os
import stat
from pathlib import Path


def _open_regular(path: Path) -> int:
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    return os.open(path, flags)


def _validate(info: os.stat_result) -> None:
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_nlink != 1:
        raise SystemExit("unsafe legacy pid file metadata")


def capture(path: Path, expected: str) -> None:
    fd = _open_regular(path)
    try:
        info = os.fstat(fd)
        _validate(info)
        value = os.read(fd, 128).decode().strip()
        if value != expected:
            raise SystemExit("legacy pid changed")
        print(
            info.st_dev, info.st_ino, info.st_uid, info.st_mode, info.st_nlink,
            info.st_ctime_ns, info.st_mtime_ns, info.st_size,
        )
    finally:
        os.close(fd)


def consume(path: Path, expected: str, identity: tuple[int, ...]) -> None:
    parent = path.parent
    name = path.name
    directory_flags = (
        os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_DIRECTORY", 0)
        | getattr(os, "O_NOFOLLOW", 0)
    )
    directory_fd = os.open(parent, directory_flags)
    try:
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        try:
            fd = os.open(name, flags, dir_fd=directory_fd)
        except OSError as exc:
            if exc.errno == errno.ENOENT:
                return
            raise
        try:
            info = os.fstat(fd)
            _validate(info)
            observed = (
                info.st_dev, info.st_ino, info.st_uid, info.st_mode, info.st_nlink,
                info.st_ctime_ns, info.st_mtime_ns, info.st_size,
            )
            if observed != identity:
                raise SystemExit("legacy pid file identity changed during drain")
            if os.read(fd, 128).decode().strip() != expected:
                raise SystemExit("legacy pid file value changed during drain")
            current = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
            current_identity = (
                current.st_dev, current.st_ino, current.st_uid, current.st_mode, current.st_nlink,
                current.st_ctime_ns, current.st_mtime_ns, current.st_size,
            )
            if current_identity != identity:
                raise SystemExit("legacy pid file path changed during drain")
            os.unlink(name, dir_fd=directory_fd)
            unlinked = os.fstat(fd)
            if (unlinked.st_dev, unlinked.st_ino) != identity[:2] or unlinked.st_nlink != 0:
                raise SystemExit("legacy pid file unlink identity changed during drain")
        finally:
            os.close(fd)
    finally:
        os.close(directory_fd)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("capture", "consume"))
    parser.add_argument("path", type=Path)
    parser.add_argument("expected_pid")
    parser.add_argument("identity", nargs="*", type=int)
    args = parser.parse_args()
    if args.action == "capture":
        if args.identity:
            parser.error("capture takes no identity")
        capture(args.path, args.expected_pid)
    else:
        if len(args.identity) != 8:
            parser.error("consume requires dev ino uid mode nlink ctime_ns mtime_ns size")
        consume(args.path, args.expected_pid, tuple(args.identity))


if __name__ == "__main__":
    main()
