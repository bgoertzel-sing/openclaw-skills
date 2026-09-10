---
name: "playwright"
description: "Automate headless browser sessions with Playwright: navigate, click, scroll, fill forms, screenshot, extract DOM text, and handle JavaScript-rendered pages."
---

# Playwright Browser Automation

Use for JavaScript-rendered pages, interactive dashboards, click-dependent navigation, login flows, screenshots, and any web access beyond simple URL fetching. Prefer `web_fetch` first; escalate to this skill when JS or interaction is required.

## Setup

Playwright Python package and Chromium browser are installed:
```
pip3 install playwright
python3 -m playwright install chromium
```

Verify: `python3 -c "from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.chromium.launch(); b.close(); p.stop()"`

## Workflow

1. Launch a headless Chromium browser via Python `sync_playwright`.
2. Create a context (optionally with viewport, user-agent, locale, or proxy).
3. Open a page, navigate to the URL, and wait for network idle or a selector.
4. Perform actions: click, fill, select, hover, scroll, evaluate JS.
5. Extract content: `page.content()` for full HTML, `page.inner_text()` for visible text, `page.screenshot()` for image capture.
6. Close the browser to free resources.

## Usage pattern

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com", wait_until="networkidle")
    page.screenshot(path="/tmp/screenshot.png")
    text = page.inner_text("body")
    browser.close()
```

## Running from the agent

Write a Python script to `scratch/`, run it with `exec`, and read the output. For one-off page fetches, inline the script. For multi-step flows, write a reusable script with CLI args.

Save screenshots to `scratch/` or the project `artifacts/` directory. Use `read` to inspect saved screenshots (image tool).

## Notes

- This is a real browser: it executes JavaScript, loads images, and respects timeouts.
- Set explicit timeouts: `page.goto(url, timeout=30000)`, `page.wait_for_selector(sel, timeout=10000)`.
- For bot-protected sites, try setting a realistic user-agent and using `wait_until="domcontentloaded"` instead of `networkidle`.
- Cookies and sessions do not persist between browser launches unless saved to a context storage state file.
- Resource cleanup: always close the browser. Use `with` blocks or try/finally.
- Do not store credentials in scripts. If login is needed, use environment variables or credential files outside the repo.
