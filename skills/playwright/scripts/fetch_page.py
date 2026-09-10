#!/usr/bin/env python3
"""Fetch a page with Playwright, print visible text, optionally screenshot.

Usage:
  python3 fetch_page.py URL [--screenshot PATH] [--selector SEL] [--timeout MS]
"""
import argparse
import sys
from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description="Fetch a page with Playwright")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--screenshot", default=None, help="Save screenshot to this path")
    parser.add_argument("--selector", default=None, help="Wait for this CSS selector before extracting")
    parser.add_argument("--timeout", type=int, default=30000, help="Navigation timeout in ms")
    parser.add_argument("--wait", default="networkidle", choices=["load", "domcontentloaded", "networkidle"], help="Wait until condition")
    args = parser.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(args.timeout)
        page.goto(args.url, wait_until=args.wait, timeout=args.timeout)
        if args.selector:
            page.wait_for_selector(args.selector, timeout=args.timeout)
        if args.screenshot:
            page.screenshot(path=args.screenshot, full_page=True)
            print(f"Screenshot saved: {args.screenshot}", file=sys.stderr)
        text = page.inner_text("body")
        print(text)
        browser.close()


if __name__ == "__main__":
    main()
