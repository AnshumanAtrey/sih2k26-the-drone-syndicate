import sys, pathlib
from playwright.sync_api import sync_playwright
html = pathlib.Path("deck.html").resolve().as_uri()
out  = "WALRUS-SIH26155-idea-submission.pdf"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(html, wait_until="networkidle")
    pg.wait_for_timeout(1500)
    pg.pdf(path=out, width="13.333in", height="7.5in",
           print_background=True, prefer_css_page_size=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
    b.close()
print("wrote", out)
