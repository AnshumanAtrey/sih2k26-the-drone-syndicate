# STYLE.md — the visual language

> Rewritten 9 Sep 2026. The old kit produced two kinds of asset: mute cinematic scenes with no
> information, and generic dark-mode bar charts. Both were wrong for this format. A judge reads one
> PDF page, offline, with nobody talking. **The visual has to carry the argument by itself.**

---

## The one rule everything else follows

**No mute images. No naked charts.**

Every visual in this deck is a *third thing*: a cinematic or diagrammatic scene that has the numbers
rendered inside it, positioned where they explain what you are looking at. A photo of a flood with a
bar chart next to it is two assets fighting. A flood seen through a drone's HUD, with the coverage
figure on the HUD, is one asset that argues.

| Banned | Why | Do instead |
|---|---|---|
| A bar chart | Nine other teams will submit the same bar chart | Make the bars *physical* — stacked banknotes, stacked rotor discs, a ladder of pixels |
| A line chart | Reads as a lab report | Put the curve inside the object it describes — a clock face, a descending stair, a fuel gauge |
| A mood shot with no text | Costs a whole page and says nothing | Add the HUD. The HUD is where the data lives |
| A Gantt chart | Correct information, dead delivery | Draw it as a flight path with milestone waypoints |
| A generic architecture box-diagram | Every deck has one | Draw the real airframes and the real silicon, labelled with real part numbers |

**Corollary:** if a visual's numbers could be deleted without the picture changing, the picture is
decoration and does not belong on a 6-page deck.

---

## Tier-1 prefix — dark, photographic (only P2.1, P2.2, P5.3; all three already rendered)

```
Style: premium defence-tech mission-control aesthetic. Deep navy-charcoal ground (#0B1220), cyan-teal primary accent (#22D3EE), warm amber-orange secondary (#F59E0B), restrained holographic HUD and grid elements, crisp technical illustration with cinematic lighting. Editorial-infographic discipline: generous negative space, strong left-to-right reading order, nothing centred by default. No watermarks, no borders, no stock-photo gloss, no lens flares, no generic "AI tech" swirls. All text renders in a clean geometric sans-serif, uppercase, tight tracking, small relative to the frame, in #E2E8F0 (primary) or #94A3B8 (secondary), with numerals in #22D3EE when they describe our system and #F59E0B when they describe the status quo. 16:9 widescreen unless stated.
```

## Two tiers — decided by the real template, 11 Sep 2026

The official PPTX is **white** (`schemeClr bg1`), 13.333 × 7.5 in. That forces a split, and the split
is a system rather than a compromise: **photographs are windows, diagrams are page furniture.**

| Tier | What | Background | On the slide |
|---|---|---|---|
| **1 — Windows** | photographs and screen captures: `P2.1` frog, `P2.2` hero, `P5.3` dashboard | **dark**, full-bleed | placed as a framed panel, 1 px `#CBD5E1` rule, 6 px radius |
| **2 — Page furniture** | every diagram and data graphic | **pure `#FFFFFF`**, flat | placed borderless — it *melts into* the slide, no frame, no card |

Never mix the two treatments for the same kind of object on one slide. A dark diagram next to a white
diagram reads as an accident; a dark photo next to a white diagram reads as a design.

**Why pure white beats "transparent".** If the artwork's background is genuinely `#FFFFFF` and the
slide is `#FFFFFF`, nothing needs removing — it already blends, losslessly. Transparency is only the
fallback when a render comes back with a faint gradient or vignette, and
`scripts/whiten.py` (in this folder) fixes that in one pass.

**Free cropping.** Because the ground is pure white, a tier-2 render can be cropped to any aspect
with no visible seam. So generate every tier-2 prompt at **16:9 with generous white space**, then
crop to the band you need — the measured slide budget wants two 16:9 panels plus one ~4:1 band per
content slide (`DATA.md` §1a).

---

## Light palette — tier 2 (contrast-checked on white)

| Token | Hex | Contrast on white | Meaning |
|---|---|---|---|
| Ground | `#FFFFFF` | — | flat, always |
| **Ink** | `#0B1220` | 19:1 | primary text, linework |
| **Teal** | `#0E7490` | **5.4:1** | **Kestrel. Us. Our numbers.** |
| **Amber** | `#B45309` | **5.0:1** | **the status quo. The baseline.** |
| Red | `#B91C1C` | 6.5:1 | hazard, failure, the false positive |
| Green | `#15803D` | 5.0:1 | survivor found, rescue, success |
| Slate | `#475569` | 7.6:1 | secondary text, footnotes, rules |
| Fill | `#E2E8F0` | — | light tints, inactive states |
| Rule | `#CBD5E1` | — | gridlines, dividers, photo frames |

Same semantics as the dark palette — teal is us, amber is what we replace — so a judge learns one
code across both tiers. **Never use the dark palette's `#22D3EE` or `#F59E0B` as text on white**;
they fail contrast. They survive only as large fills.

## Tier-2 prefix — light, diagrammatic. Paste before every tier-2 prompt

```
Style: precise editorial-technical infographic for a printed report. PURE WHITE background, hex #FFFFFF, absolutely flat - no gradient, no vignette, no paper texture, no coloured wash, no drop shadow falling on the background, no rounded card or panel behind the artwork, pure white right to all four edges. Linework and primary text in deep navy #0B1220. Our system and good values in teal #0E7490. Status quo, baseline and problem values in burnt amber #B45309. Hazard in #B91C1C. Rescue and success in #15803D. Secondary text, footnotes and rules in slate #475569; light tints in #E2E8F0. Clean geometric sans-serif; ALL text perfectly horizontal - never curved, never rotated, never set along an arc. Generous white space, strong left-to-right reading order. No watermarks, no borders, no frames, no outer glow, no lens flare, no 3D bevel, no stock-illustration gloss. 16:9.
```

## Dark palette — tier 1, unchanged

| Token | Hex | Meaning — never varies |
|---|---|---|
| Navy | `#0B1220` | ground |
| Panel | `#111C2E` | cards, table surfaces |
| Grid | `#24324A` | rules, dividers, gridlines |
| **Cyan** | `#22D3EE` | **Kestrel. Us. Our numbers.** |
| **Amber** | `#F59E0B` | **the status quo. The baseline. What we are replacing.** |
| Red | `#EF4444` | hazard, failure, the false positive |
| Green | `#10B981` | survivor found, safe, rescue |
| Text | `#E2E8F0` | primary |
| Slate | `#94A3B8` | secondary, axis labels, footnotes, assumption boxes |

A judge should have learned this code by the bottom of Slide 2 without being told. Never put a
Kestrel number in amber; never put a baseline number in cyan.

---

## How to write a prompt in this kit

Each prompt has four blocks, in this order. Do not reorder them; image models weight early tokens.

1. **Composition** — what is in the frame and where, in reading order.
2. **Render style** — the medium (photoreal / isometric technical / editorial infographic).
3. **`Text labels (render exactly)`** — an explicit list of every string. Each label **≤ 5 words**.
4. **Constraint tail** — aspect, and what must *not* appear.

**Label discipline.** Current image models render short specified strings reliably and garble
sentences. Never ask for a paragraph. If a label comes back wrong, regenerate twice, then overlay
that one string natively in the PPT — the rest of the image is still good.

**Model routing.** Send these to whichever image model in front of you renders text most faithfully
(Nano Banana Pro / Gemini 3 Pro Image and GPT Image both handle in-image typography and infographic
layout well; older diffusion models will fail the label test). For the three prompts marked
**`[DATA-EXACT]`**, if the numbers come back altered by even one digit, do not accept the image —
either regenerate or build that one visual as native PPT shapes using the same palette. **A wrong
number is worse than a plain chart.**

**Consistency.** Generate the Slide 2 hero first. On every later prompt, attach it and append:
*"match the lighting, palette, material finish and realism of the attached image."*

**Real photos for real hardware.** The RB3 Gen 2 board, the Pixhawk, the FLIR Lepton and the phone
are photographed from vendor pages, never generated. A Qualcomm judge knows what their own dev kit
looks like, and an AI-hallucinated version of it is the single fastest way to lose their trust.

---

## Typography inside the PPT

The template ships **Times New Roman 36 pt bold** titles and **Arial 32 pt** pointers. Keep the
title face as shipped — changing it is a visible template edit for no gain. Everything you add:

- Body and callouts: **Inter** or **Arial** Medium, 14–18 pt, ink `#0B1220`
- Numerals in callouts: Bold, 32–56 pt, **teal `#0E7490`** for us / **amber `#B45309`** for baseline
- Footnotes and sources: 10–11 pt, slate `#475569` — every derived figure gets one
- **Mandatory pointer rail:** the template's own sub-bullets, kept verbatim, 11 pt, slate `#475569`,
  in a 2.7 in left rail. Resized and moved, never reworded — see `DATA.md` §1a
- One accent colour per block. Two accents in one block reads as decoration.

## Before you export

- 6 pages, PDF, under 10 MB. Check the page count against the official template *before* designing.
- Read every page at 25% zoom. If the argument isn't legible as shapes and numbers at that size, the
  hierarchy is wrong.
- Print one page in greyscale. If cyan and amber become the same grey, add a shape or weight
  difference — some judges print.
- Every `[DERIVED]` figure carries its assumption box. Shown assumptions score under *"clarity and
  details in the prescribed format."* Hidden ones invite the question you cannot answer.
