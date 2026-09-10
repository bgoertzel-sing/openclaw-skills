#!/usr/bin/env python3
"""Download and verify the frozen MTG-Jamendo subset for this experiment."""
import csv
import hashlib
import urllib.request
from pathlib import Path
from mutagen.mp3 import MP3

ROOT = Path(__file__).resolve().parent
META = ROOT / "data/mtg-jamendo-metadata"
OUT = ROOT / "data/audio"
BASE = "https://cdn.freesound.org/mtg-jamendo/raw_30s/audio-low"
SOURCE_COMMIT = "cafd8e20c265ed84f1e61f1c875327971f43a62f"
DOWNLOAD_DATE = "2026-07-26"
TRACK_IDS = [
    "track_0000382", "track_0000387",
    "track_0000759", "track_0000760", "track_0000761", "track_0000762",
    "track_0000764", "track_0000765", "track_0000766", "track_0000767",
    "track_0000768", "track_0000770", "track_0000772",
    "track_0000773", "track_0000774", "track_0000776",
    "track_0001092", "track_0001093", "track_0001094", "track_0001095",
    "track_0001096", "track_0001097", "track_0001098", "track_0001099",
]


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


raw = {r["TRACK_ID"]: r for r in csv.DictReader(
    (META / "data/raw.tsv").open(), delimiter="\t")}
descriptions = {r["TRACK_ID"]: r for r in csv.DictReader(
    (META / "data/raw.meta.tsv").open(), delimiter="\t")}
license_rows = {}
lines = (META / "audio_licenses.txt").read_text().splitlines()
for i in range(0, len(lines), 4):
    if i + 2 < len(lines):
        license_rows[lines[i].strip()] = (lines[i + 1].strip(),
                                          lines[i + 2].strip())
publisher_hashes = {}
for line in (META / "data/download/raw_30s_audio-low_sha256_tracks.txt").read_text().splitlines():
    digest, path = line.split()
    publisher_hashes[path] = digest

OUT.mkdir(parents=True, exist_ok=True)
manifest = []
for track_id in TRACK_IDS:
    row = raw[track_id]
    source_path = row["PATH"]
    low_path = source_path[:-4] + ".low.mp3"
    destination = OUT / f"{track_id}.mp3"
    source_url = f"{BASE}/{low_path}"
    license_text = license_rows[source_path][1]
    if "Creative Commons Attribution" not in license_text:
        raise RuntimeError(f"Non-approved license: {track_id}: {license_text}")
    if float(row["DURATION"]) < 180:
        raise RuntimeError(f"Metadata duration below 180s: {track_id}")
    if not destination.exists():
        print(f"Downloading {track_id}: {source_url}", flush=True)
        urllib.request.urlretrieve(source_url, destination)
    digest = sha256(destination)
    expected = publisher_hashes[low_path]
    if digest != expected:
        raise RuntimeError(f"Publisher checksum mismatch: {track_id}")
    measured = float(MP3(destination).info.length)
    if measured < 180:
        raise RuntimeError(f"Measured duration below 180s: {track_id}: {measured}")
    detail = descriptions.get(track_id, {})
    manifest.append({
        "track_id": track_id,
        "artist": detail.get("ARTIST_NAME", ""),
        "title": detail.get("TRACK_NAME", ""),
        "duration_seconds_metadata": row["DURATION"],
        "duration_seconds_measured": f"{measured:.3f}",
        "source_url": source_url,
        "license": license_text,
        "sha256": digest,
        "publisher_sha256": expected,
        "source_metadata_commit": SOURCE_COMMIT,
        "download_date": DOWNLOAD_DATE,
        "local_file": destination.name,
    })

with (ROOT / "audio_manifest.tsv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=manifest[0].keys(), delimiter="\t")
    writer.writeheader()
    writer.writerows(manifest)
print(f"Verified {len(manifest)} tracks, {sum(float(r['duration_seconds_measured']) for r in manifest)/60:.2f} minutes")
