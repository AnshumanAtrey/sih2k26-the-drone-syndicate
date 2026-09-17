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

## Format compliance — checked against six actual winning decks

Not asserted from memory. Two sources.

**The verbatim rule**, from slide 7 of the template's own XML:
> "You can only use provided template for making the PPT **without changing the idea details
> pointers** (mentioned in previous slides)."

The restrictive clause is scoped: what you may not change is the *idea details pointers*. We keep
them as the literal structure of every content block. The 26-page official guidelines say nothing
about the template — only "Idea presentation (PDF)" and, among nine judging criteria, "clarity and
details in the prescribed format."

**The empirical check** — six winning decks (GeoGuards '25, Tech Pioneers '25, Techbyte '24,
AKY GreenSort '24, Cannon Crew '24, Innovators '24):

| Element | Kept by |
|---|---|
| Team-name oval, top-left | **6 / 6** |
| Centred serif title | **6 / 6** |
| SIH logo, top-right | 5 / 6 |
| Blue bottom bar + page number | 5 / 6 |
| Template page size 13.333 × 7.5 in | **0 / 6** |

Sizes ranged 13.76 × 7.82 to 26.67 × 15 in. Techbyte recoloured the background pink and replaced the
SIH logo; Tech Pioneers dropped the bottom bar and renamed the title to their product. **Nobody
ships a faithful clone.** The pattern is: keep the recognisable skeleton, rebuild the inside.

Worth noting: several of those decks have visible defects — Innovators ships clipped, overlapping
text on its Technical Approach slide. The bar is structure and clarity, not polish.

**What we adopted from them:**
- Team-name oval top-left, SIH logo top-right, centred Times New Roman title, blue bar + page number
- **Visible tech-stack chips** — every hardware winner shows the stack as blocks, never buried in prose
- Real bullet markers, per the template's "post your idea in points, not paragraphs"
- Slide 2 opens on a **named beneficiary** (Wayanad's 206 missing) before any technology, per the
  SIH 2026 playbook's storytelling note that judges retain narratives over feature lists
