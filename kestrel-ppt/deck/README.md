# deck/ — the submission PDF and the thing that builds it

**`KESTREL-SIH26177-idea-submission.pdf`** — 6 pages, exactly 13.333 × 7.5 in, **8.6 MB**.

## Why a build script instead of PowerPoint

The layout is dense and every element is positioned in absolute inches, so **overlap is a
computable property rather than something you squint at**. `build.py` emits `deck.html`
and records every box it places into `boxes.json`; the verifier then asserts:

- zero same-slide box overlaps
- zero boxes crossing the official bottom bar at y = 6.95 in
- zero glyphs rendered off-page
- page size exactly 13.333 × 7.5 in, 6 pages

That check found three real collisions during the build, including one where a declared
block was taller than its content and silently clipped a reference line.

## Toolchain

```
build.py  ->  deck.html  ->  headless Brave --print-to-pdf  ->  PyMuPDF verification
```

No LibreOffice on this machine, so PPTX→PDF was unavailable. Chromium's print engine renders
modern CSS exactly and hits the page size to three decimals, which is what the template needs.
The official SIH 2026 logo, the bottom colour bar and the title band geometry are reproduced
from `given/SIH2026-TEMPLATE-EXTRACT.md` (title band 0–0.84 in, bar 6.95–7.5 in).

Rebuild with:
```bash
python3 build.py && "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
  --headless --disable-gpu --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf=kestrel.pdf "file://$PWD/deck.html"
```

## Images chosen, and why

| Slide | Visuals | Reason |
|---|---|---|
| 1 Title | `c4-swarm` · `s1-one-drone` | Swarm and single aircraft together — the PS says "a drone", we show both readings immediately |
| 2 Proposed Solution | `s1-one-drone` · `c4-swarm` · `f1-sachet` | One aircraft → six → the SACHET inversion, which is the novelty claim |
| 3 Technical Approach | `s2-loop` · `f2-buried` | Our decision algorithm, and the fusion argument that justifies it |
| 4 Feasibility | `r3-alternatives` · `f4-cost` · `f5-degrade` | Four architectures scored, cost against helicopter, graceful degradation |
| 5 Impact | `r1-survival` · `p5-dashboard` · `c6-void` | Survival curve, the PS's own "command centre dashboard" bullet, and the human close |

**Excluded on purpose:** `R2-8-mission-timeline` still reads *"MOTHERSHIP UP, RELAY LIVE"* and the
mothership was deleted in `DATA.md` Addendum 4. Stale artwork, not used.

## Size

Photographic panels are JPEG q84 at 1250 px (~200 dpi at their placed width); diagrams stay PNG so
their text stays crisp. That took the PDF from **20.5 MB to 8.6 MB** with no visible loss.

## Still open

- Team Name is **Drone Syndicate**. **Team ID is still blank** — fill from the SIH portal registration.
