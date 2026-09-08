#!/usr/bin/env python3
"""Convert a Markdown file to a styled PDF using markdown + weasyprint."""

import sys
import markdown
from weasyprint import HTML

CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 9pt;
        color: #666;
    }
}

body {
    font-family: "DejaVu Sans", "Liberation Sans", "Noto Sans", Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #1a1a1a;
    max-width: 100%;
}

h1 {
    font-size: 20pt;
    color: #1a3a5c;
    border-bottom: 2px solid #1a3a5c;
    padding-bottom: 6pt;
    margin-top: 24pt;
    margin-bottom: 12pt;
    page-break-after: avoid;
}

h2 {
    font-size: 15pt;
    color: #2a5a8c;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4pt;
    margin-top: 20pt;
    margin-bottom: 10pt;
    page-break-after: avoid;
}

h3 {
    font-size: 12pt;
    color: #3a6a9c;
    margin-top: 16pt;
    margin-bottom: 8pt;
    page-break-after: avoid;
}

h4 {
    font-size: 11pt;
    color: #4a7aac;
    margin-top: 12pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
}

p {
    margin-bottom: 8pt;
    text-align: justify;
    orphans: 3;
    widows: 3;
}

code {
    font-family: "DejaVu Sans Mono", "Liberation Mono", "Noto Sans Mono", monospace;
    font-size: 9pt;
    background-color: #f4f4f8;
    padding: 1pt 3pt;
    border-radius: 2pt;
}

pre {
    background-color: #f4f4f8;
    border: 1px solid #ddd;
    border-radius: 4pt;
    padding: 10pt 12pt;
    font-size: 8.5pt;
    line-height: 1.4;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: avoid;
    margin-bottom: 10pt;
}

pre code {
    background: none;
    padding: 0;
    font-size: 8.5pt;
}

ul, ol {
    margin-bottom: 8pt;
    padding-left: 20pt;
}

li {
    margin-bottom: 4pt;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 12pt;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #ccc;
    padding: 6pt 8pt;
    text-align: left;
}

th {
    background-color: #e8eef4;
    font-weight: bold;
    color: #1a3a5c;
}

tr:nth-child(even) td {
    background-color: #f9f9fb;
}

strong {
    color: #1a3a5c;
}

em {
    color: #555;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 16pt 0;
}

blockquote {
    border-left: 3px solid #2a5a8c;
    margin: 10pt 0;
    padding: 6pt 12pt;
    background-color: #f0f4f8;
    font-style: italic;
}
"""

def md_to_pdf(md_path: str, pdf_path: str) -> None:
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    extensions = ["tables", "fenced_code", "codehilite", "toc", "smarty", "sane_lists"]
    html_body = markdown.markdown(md_text, extensions=extensions)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Plain2MeTTa v2 Spec</title></head>
<body>{html_body}</body>
</html>"""

    HTML(string=full_html).write_pdf(pdf_path, stylesheets=[],
                                      presentational_hints=True)
    # Apply CSS via inline style
    full_html_styled = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Plain2MeTTa v2 Spec</title>
<style>{CSS}</style>
</head>
<body>{html_body}</body>
</html>"""
    
    HTML(string=full_html_styled).write_pdf(pdf_path, presentational_hints=True)
    print(f"PDF written to {pdf_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.md output.pdf")
        sys.exit(1)
    md_to_pdf(sys.argv[1], sys.argv[2])
