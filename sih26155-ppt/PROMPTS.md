# PROMPTS — Walrus Securitas · SIH26155

12 prompts across the 4 content slides (Slides 1 & 6 are text view slides, no prompts). **Each fenced
block is complete** — the Walrus brand prefix is merged in, copy the whole block and paste. Route to
whichever image model renders in-image text most faithfully (Nano Banana Pro / Gemini 3 Pro Image /
GPT Image). Run `python3 ../kestrel-ppt/scripts/whiten.py images/<file>.png` after each render.

**The Walrus brand system (from `walrus-hq/graphic-designer/lib/tokens.css` — the single source):**
- **orange `#FE5301`** — the *only* colour that shouts. Walrus, our system, the winning value, the one
  accent. One loud note per frame. (Deep partner `#D84600` for the learning path.)
- **ink `#141417`** — linework and primary text · **grey `#5A6472`** — the status quo, the manual old
  way, secondary text · **`#F4F4F4`** — light fills.
- **Severity scale (data, not decoration):** critical `#E5484D` · high `#FE5301` · medium `#E0A800` ·
  low `#5A6472`. A **FAIL** is red `#E5484D`; a **PASS** is a calm ink tick — **never green.**
- **No teal, no blue, no green, no eye glyph.** Orange reticle ticks in the four corners are the only
  frame. Labels: geometric monospace, uppercase, wide tracking. Big numerals: elegant light serif.
- **Engine blocks carry only the WALRUS wordmark** — a clean orange rectangle with white text, no icon
  and no empty placeholder box. The model never draws a logo. *Optional* polish: composite the real
  mark (`walrus-hq/branding/walrus-mark-orange-transparent.png`) beside the wordmark in the PPT — but
  the block already reads correctly without it.

**Label discipline:** every string ≤5 words, all horizontal, never curved. Models can't count icons
reliably above ~5 — where a count matters it's "exactly N"; elsewhere counts are illustrative. Six
prompts are `[DATA-EXACT]` — if a printed numeral comes back altered, reject and regenerate, or build
that one as native PPT shapes. **A wrong number is worse than a plain chart.**

---

## SLIDE 2 — PROPOSED SOLUTION

### W2.1 — One config in, one report out  `[flow band]`
**Slide 2** · crop to a wide band (~4:1) · establishes the problem *and* the fix in one strip
**Reject if:** the input side isn't visibly many *different* vendors · the output isn't ONE unified
report · the engine block has an empty placeholder box, an eye glyph, or a drawn logo

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card or panel behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our system, the winning value, and the single accent. Everything else is ink on white: linework and primary text in ink #141417; the status quo, the manual old way and secondary text in muted warm grey #5A6472; light fills in #F4F4F4. Findings use the severity scale and nothing else — critical #E5484D, high #FE5301, medium #E0A800, low #5A6472; a FAIL is red #E5484D, a PASS is a calm ink tick, never green. Absolutely NO teal, NO blue, NO green anywhere. Draw small orange reticle tick marks in the four corners as the only frame. Section labels are geometric MONOSPACE, uppercase, small, wide letter-spacing; large stat numerals are an elegant light serif. A small solid-orange tab may sit before a heading, and one key phrase may carry an orange marker-highlight swipe. Minimal, generous white space, strong left-to-right reading order. ALL text perfectly horizontal — never curved, never rotated. No watermarks, no borders beyond the corner ticks, no outer glow, no 3D bevel, no gloss, and do not draw any company logo yourself. 16:9.

Composition: a single left-to-right flow across the whole width, in three zones joined by one continuous orange arrow.
LEFT ZONE: a messy leaning stack of five distinctly different NETWORK-DEVICE configuration cards in muted grey - a Cisco IOS running-config, a Juniper "set" config, an Arista EOS config, a firewall policy and a switch config - each with visibly different syntax so they read as different vendors, a small tangled look and a tiny grey magnifier-with-question-mark to signal manual, error-prone checking. Do NOT use cloud or application configs (no Terraform, Kubernetes, Docker, nginx or .env).
CENTRE ZONE: one clean solid orange rounded-rectangle engine block, clearly the hub, with the single word WALRUS set inside it in white and nothing else on the block - no icon, no logo, no inner box, panel or outline, and no blank gap around the text; the word sits directly and snugly on the orange fill. The arrow from the messy stack enters its left side.
RIGHT ZONE: one single clean report page from the engine's right side, showing a short vertical list of NETWORK-HARDENING rows - three rows with calm ink tick marks (e.g. "SSHv2 enforced", "logging enabled", "NTP configured") and two rows with red crosses (e.g. "Telnet enabled", "SNMP community public") - and at the bottom a small monospace snippet block on a faint orange tint with a Cisco-style fix command.
Under each zone a short caption line.

Render style: clean flat technical line illustration with light tint fills, editorial and uncrowded. Not a flowchart of identical rectangles.

Text labels (render exactly, all horizontal):
- under LEFT zone, two lines, grey: "ANY VENDOR, ANY SYNTAX" / "CHECKED BY HAND TODAY"
- on the CENTRE engine, white-on-orange: "WALRUS"
- under CENTRE zone, ink: "READ. NORMALIZE. CHECK."
- under RIGHT zone, two lines, ink then orange: "ONE HARDENING REPORT" / "PASS / FAIL + FIX COMMANDS"

Constraint: 16:9, pure white ground. Only the labels listed. Five input cards must look like different vendors; the output must be a single page. The engine is just an orange block with the WALRUS wordmark - no empty boxes or logo placeholders anywhere.
```

---

### W2.2 — Many vendors, one neutral model  `[16:9]`
**Slide 2** · keep 16:9
**Reject if:** the vendor snippets don't converge into ONE central box · the four framework badges
aren't clearly downstream · any real company logo appears

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card or panel behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our system, the winning value, and the single accent. Everything else is ink on white: linework and primary text in ink #141417; source material and secondary text in muted warm grey #5A6472; light fills in #F4F4F4. Absolutely NO teal, NO blue, NO green anywhere. Draw small orange reticle tick marks in the four corners as the only frame. Section labels are geometric MONOSPACE, uppercase, small, wide letter-spacing; large numerals are an elegant light serif. Minimal, generous white space. ALL text perfectly horizontal — never curved, never rotated. No watermarks, no borders beyond the corner ticks, no glow, no 3D bevel, no gloss, and do not draw any company logo yourself. 16:9.

Composition: three tiers stacked vertically.
TOP TIER: a row of six small configuration snippet cards in muted grey, each with two or three lines of different-looking monospace text so they read as six different vendors' CLI. Six thin grey arrows drop from them and converge.
MIDDLE TIER: one wide solid orange rounded rectangle spanning the centre, the convergence point of all six arrows - the vendor-neutral schema. A small orange normalize/merge glyph on its left.
BOTTOM TIER: four evenly spaced framework badges in a row, each a clean ink-outlined rounded tag, with four orange arrows fanning down to them from the central box.

Render style: clean flat technical diagram, light tint fills, plenty of white gaps. Not skeuomorphic, no real logos.

Text labels (render exactly, all horizontal):
- above the TOP row, grey: "PROPRIETARY VENDOR CONFIGS"
- on the MIDDLE box, two lines, white-on-orange: "SECURITY BASELINE MODEL" / "ONE NEUTRAL SCHEMA"
- on the four BOTTOM badges, one each, ink: "CIS BENCHMARKS" / "NIST SP 800-53" / "DISA STIGs" / "ISO 27001"

Constraint: 16:9, pure white ground. Only the labels listed. Suggest vendors only by differing code style, never real logos. Six input cards illustrative; the four framework badges must be exactly four.
```

---

### W2.3 — Why it matters  `[DATA-EXACT]` `[band]`
**Slide 2** · crop to a wide band (~4:1)
**Reject if:** "99%" is altered · the two regions blur into one · our short bar isn't the only orange thing

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our system and the winning value. Everything else is ink on white: primary text and the problem numeral in ink #141417; the status quo and secondary text in muted warm grey #5A6472. Hazard may use red #E5484D. Light fills in #F4F4F4. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking; the big numeral in an elegant light serif. Minimal, generous white space. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no logo. 16:9.

Composition: two regions separated by a wide white gutter, each with its own heading.
LEFT REGION: one very large numeral "99%" in heavy ink, dominating the region, with a short stacked caption beneath. A small simple firewall/brick-wall icon with a tiny red crack in it sits beside the numeral.
RIGHT REGION: a two-bar time contrast - a tall muted-grey bar and a very short orange bar side by side, the grey bar many times taller than the orange one, each with a label above and a value below. A small ink clock glyph above both.

Render style: clean flat editorial figure. Not a full chart with axes - just the two bars as physical magnitudes.

Text labels (render exactly, all horizontal):
- LEFT heading, grey: "THE #1 CAUSE"
- under the "99%", two lines, ink then grey: "OF FIREWALL BREACHES" / "ARE MISCONFIGURATIONS, NOT FLAWS"
- LEFT footnote, small grey: "Source: Gartner"
- RIGHT heading, grey: "TIME TO AUDIT"
- above the tall bar, grey: "BY HAND" ; below it, grey: "~HALF A DAY / DEVICE"
- above the short bar, orange: "WALRUS" ; below it, orange: "MINUTES, ALL DEVICES"

Constraint: 16:9, pure white ground. Only the labels listed. "99%" must be exact. The orange short bar must be the only orange element; the grey bar must be clearly many times taller.
```

---

## SLIDE 3 — TECHNICAL APPROACH  *(the focus of the deck)*

### W3.1 — Quick architecture: the four stages  `[16:9]`
**Slide 3** · keep 16:9 · the "read it in three seconds" view
**Reject if:** the four stages aren't a single clean left-to-right line · any stage label wrong · any green

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our system and the flow. Everything else is ink on white: linework and text in ink #141417; secondary text in muted warm grey #5A6472; light fills in #F4F4F4. A FAIL mark is red #E5484D, a PASS mark is a calm ink tick, never green. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking; stage numbers in an elegant light serif. Minimal, generous white space, strong left-to-right order. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no logo. 16:9.

Composition: four large numbered stage tiles in one horizontal row, evenly spaced with wide white gaps, one continuous orange arrow threading through all four left to right.
STAGE 1 tile: a small icon of stacked NETWORK-DEVICE config files being uploaded, labelled like cisco.cfg / juniper.conf / arista.cfg - not cloud or application files.
STAGE 2 tile: an icon of a config transforming into a clean structured schema (braces / key-value rows).
STAGE 3 tile: an icon of that schema compared against a checklist, some rows with ink ticks, some with red crosses.
STAGE 4 tile: an icon of a single device hardening report page (pass/fail rows such as "Telnet enabled", "SNMP public") with a small Cisco-style remediation snippet on a faint orange tint.
Each tile has a large serif number and a two-line monospace caption below it.

Render style: clean flat technical diagram, light tint fills, uncrowded, the look of a well-made engineering figure.

Text labels (render exactly, all horizontal):
- STAGE 1, ink then grey: "1. INGEST" / "ANY VENDOR CONFIG"
- STAGE 2, ink then orange: "2. NORMALIZE" / "TO BASELINE MODEL"
- STAGE 3, ink then grey: "3. CHECK" / "AGAINST FRAMEWORK"
- STAGE 4, ink then orange: "4. REPORT" / "PASS/FAIL + FIX"

Constraint: 16:9, pure white ground. Only the labels listed. Exactly four stages, exactly one connecting arrow.
```

---

### W3.2 — The agent architecture (in depth)  `[16:9]` ★ the heart of the deck
**Slide 3** · keep 16:9 · this is the system Walrus actually is
**Reject if:** workers are shown being *handed* tasks by the orchestrator — they must **pull** from the
queue · there is no shared ledger every worker reads and writes · the knowledge base isn't feeding the
workers · any eye glyph or empty placeholder box appears

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our system and the active flow. Everything else is ink on white: linework and text in ink #141417; passive infrastructure and secondary text in muted warm grey #5A6472; light fills in #F4F4F4. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Every box labelled in geometric MONOSPACE uppercase, wide tracking. Minimal, generous white space. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, not 3D, not isometric, no company logo. 16:9.

Composition: a layered top-to-bottom architecture diagram with clearly separated regions and clean arrows.
TOP: one solid orange ORCHESTRATOR box, centred, with the word ORCHESTRATOR set in white inside it and nothing else - no icon, no logo, no inner box, panel or outline, and no blank gap around the text; the word sits directly and snugly on the orange fill. A single arrow runs from it DOWN to a QUEUE.
QUEUE (upper middle): a vertical stack of four small task tickets drawn as stacked grey cards, each ticket a device to audit - a passive holding area.
WORKER FLEET (middle): a row of three identical ink-outlined worker boxes below the queue. Each worker box contains a small orange gear labelled inside as its harness. From each worker an arrow reaches UP into the queue to take a ticket - arrows point FROM the workers TO the queue (pulling), not from queue down to workers. Between two adjacent workers, one short dotted grey horizontal arrow for peer coordination.
SHARED LEDGER (right side, spanning the fleet's height): a tall orange-outlined document/log panel every worker connects to with a thin double-headed arrow, so all three both write and read.
KNOWLEDGE BASE (left side, spanning the fleet's height): a grey database cylinder feeding a thin orange arrow into each of the three workers.
BOTTOM: three arrows from the workers converge into one ink REPORTS block.

Render style: clean flat systems-architecture diagram, light tint fills, generous spacing, every box labelled.

Text labels (render exactly, all horizontal):
- TOP box, white-on-orange: "ORCHESTRATOR"
- beside the queue, grey: "WORK QUEUE - ONE PER DEVICE"
- inside each worker gear, orange: "HARNESS"
- under the worker row, ink: "WORKERS PULL WORK"
- on the dotted arrow between two workers, grey: "COORDINATE, PAUSE ON CLASH"
- on the right panel, orange: "SHARED LIVE LEDGER"
- under that panel, grey: "WHO IS DOING WHAT"
- on the left cylinder, grey: "CONTROL KNOWLEDGE BASE"
- on the bottom block, ink: "PER-DEVICE REPORTS"

Constraint: 16:9, pure white ground. Only the labels listed. The pull direction (workers -> queue) is the single most important requirement. Three workers illustrative. No empty boxes or logo placeholders - labelled orange blocks only.
```

---

### W3.3 — The AI pipeline: one config's journey  `[band]`
**Slide 3** · crop to a wide band (~4:1)
**Reject if:** the "unknown structure" branch doesn't loop back to update the engine · the "miss
nothing" checklist isn't shown complete · RAW config and NORMALIZED model look identical

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — for our system and the main flow; the learning/adaptation loop may use the deep partner orange #D84600, drawn dashed. Everything else is ink on white: text in ink #141417; raw/old material and secondary text in muted warm grey #5A6472; light fills in #F4F4F4. A FAIL is red #E5484D, a PASS is a calm ink tick, never green. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking. Minimal, generous white space, strong left-to-right order. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no logo, no brain glyph. 16:9.

Composition: a mostly left-to-right pipeline with one return loop below.
STEP A (far left): a card of raw messy monospace config lines in grey, labelled raw.
STEP B: an AI-read stage drawn as a small orange nested-brackets / parse glyph (NOT a brain, NOT an eye) reading step A.
STEP C: a clean structured key-value schema card in orange - the normalized model, visibly tidier than step A.
STEP D: a comparison stage - the schema card beside a vertical checklist whose every row carries a mark, most calm ink ticks and a couple of red crosses, labelled as the deviation check against the framework.
DECISION below step B/C: a small grey diamond where an unrecognised config structure is detected; from it a dashed deep-orange arrow drops to a TRAINING panel (a simple GUI card where an admin maps a raw line to a category), and from that panel a dashed deep-orange arrow curves back LEFT into step B, closing the learning loop.
Above step D, a small orange banner strip showing a fully-ticked checklist to signal completeness.

Render style: clean flat technical pipeline, light tint fills, uncrowded.

Text labels (render exactly, all horizontal):
- STEP A, grey: "RAW CONFIG"
- STEP B, orange: "AI READS IT"
- STEP C, orange: "NORMALIZED MODEL"
- STEP D, ink: "CHECK vs FRAMEWORK"
- above step D banner, orange: "EVERY CONTROL, TICKED"
- at the diamond, grey: "UNKNOWN FORMAT?"
- on the training panel, two lines, ink then grey: "ADMIN MAPS IT ONCE" / "NO CODE REDEPLOY"
- on the return arrow, deep orange: "ENGINE LEARNS"

Constraint: 16:9, pure white ground. Only the labels listed. The dashed learning arrow must visibly loop back to STEP B. The normalized card (C) must look tidier than the raw card (A). No brain and no eye glyph anywhere.
```

---

## SLIDE 4 — FEASIBILITY AND VIABILITY

### W4.1 — Runs anywhere, integrates easily  `[16:9]`
**Slide 4** · keep 16:9 · answers "diverse enough for any system" + "easy integration"
**Reject if:** the word WALRUS appears more than once (only the centre block may carry it) · a deploy
target repeats the wordmark or has a white placeholder box · any integration channel is missing

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — for our engine and the flow. Everything else is ink on white: linework and text in ink #141417; input sources and infrastructure in muted warm grey #5A6472; light fills in #F4F4F4. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking. Minimal, generous white space, left-in / right-out reading order. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no company logo. 16:9.

Composition: a central hub with inputs on the left and deployment targets on the right.
CENTRE: one solid orange WALRUS engine block, the word WALRUS in white sitting directly and snugly on the orange fill - no icon, no box, no gap. This block is the ONLY place the word WALRUS appears anywhere in the image.
LEFT (integration in): four small grey source icons stacked vertically, each with an orange arrow pointing right into the engine - a dashboard upload tray, a network-pull connector, an API bracket symbol, and a folder/git repo.
RIGHT (deploy anywhere): three grey platform icons stacked vertically - an air-gapped server rack with a small no-signal/cut-cable badge, a private-cloud outline, and a laptop. One orange arrow fans from the centre engine to each. Each platform carries one small solid-orange square mark (a few percent of the icon's size) to signal the engine running there - NOT the word WALRUS. The wordmark is never repeated on the right side.
BOTTOM STRIP: a thin full-width faint-orange bar with a short capability line.

Render style: clean flat systems diagram, light tint fills, generous spacing.

Text labels (render exactly, all horizontal):
- on the centre engine, white-on-orange: "WALRUS"
- beside the four LEFT sources, one each, grey: "UPLOAD" / "NETMIKO / NAPALM" / "REST API" / "CONFIG REPO"
- LEFT group heading, ink: "EASY INTEGRATION"
- under the three RIGHT targets, one each, grey: "AIR-GAPPED SERVER" / "PRIVATE CLOUD" / "SINGLE LAPTOP"
- RIGHT group heading, ink: "SAME ENGINE, ANYWHERE"
- BOTTOM strip, orange: "40+ VENDORS, 4 FRAMEWORKS, ZERO CODE"

Constraint: 16:9, pure white ground. Only the labels listed. The word WALRUS appears EXACTLY ONCE, on the centre engine. The three right-hand targets are grey platform icons with one small orange square mark each - no wordmark, no white box. The air-gapped target must carry a clear no-external-connection badge.
```

---

### W4.2 — The trust design: the AI never decides  `[16:9]`
**Slide 4** · keep 16:9 · the anti-hallucination + knowledge-base story
**Reject if:** the model is shown making the pass/fail verdict — it must ONLY parse · no evidence line
links a finding to a real config line · a brain or eye glyph appears in the deterministic panel

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for the AI/parse side and the accent. Everything else is ink on white: the deterministic rules side and linework in ink #141417; the knowledge base and secondary text in muted warm grey #5A6472; light fills in #F4F4F4. A FAIL is red #E5484D, a PASS is a calm ink tick, never green. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking. Minimal, generous white space. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no company logo. 16:9.

Composition: an upper half split into two panels, and a lower evidence strip spanning both.
UPPER-LEFT PANEL ("the AI only parses"): a small orange nested-brackets parse glyph (NOT a brain, NOT an eye) reading a raw config card and emitting a tidy set of key-value fields. A caption makes clear it proposes fields, it does not judge.
UPPER-RIGHT PANEL ("the check is deterministic"): a hard mechanical gear / logic-block glyph in ink that takes those fields on one side and a stack from a small grey database cylinder (the control knowledge base) on the other, and outputs a column of verdicts - calm ink ticks and red crosses. NO parse, brain or eye glyph anywhere in this panel.
A bold ink vertical divider between the two panels with a short label on it.
LOWER EVIDENCE STRIP: one finding card (a red-crossed row) with a thin line dropping to a highlighted single line inside a config snippet, showing the exact source of the verdict.
TOP-RIGHT CORNER motif: a small fully-ticked checklist in orange.

Render style: clean flat technical diagram, light tint fills, two clearly distinct panels.

Text labels (render exactly, all horizontal):
- UPPER-LEFT heading, orange: "AI ONLY PARSES"
- under it, grey: "PROPOSES FIELDS, NEVER JUDGES"
- UPPER-RIGHT heading, ink: "CHECK IS DETERMINISTIC"
- under it, grey: "RULES + KNOWLEDGE BASE DECIDE"
- on the divider, grey: "NO MODEL ON THE VERDICT"
- database cylinder, grey: "CONTROL KNOWLEDGE BASE"
- LOWER strip, ink: "EVERY VERDICT CITES ITS CONFIG LINE"
- corner motif, orange: "MISSES NO CONTROL"

Constraint: 16:9, pure white ground. Only the labels listed. There must be NO parse, brain or eye glyph in the right-hand deterministic panel - that is the entire point. The evidence line must connect a finding to a specific config line.
```

---

### W4.3 — Three risks, three answers  `[band]`
**Slide 4** · crop to a wide band (~4:1)
**Reject if:** risks and answers aren't clearly paired · the answer cards aren't the orange ones

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our answers. Risks are muted warm grey #5A6472 with a medium-severity gold #E0A800 warning glyph; linework and text in ink #141417; light fills in #F4F4F4. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking. Minimal, generous white space, left-to-right. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no logo. 16:9.

Composition: three equal columns across the width, wide white gaps between them. Each column is a vertical pair: a grey risk card on top with a small gold warning glyph, a short orange down-arrow, and a solid orange answer card below with a small ink tick.

Render style: clean flat editorial cards, light tint fills, three tidy columns.

Text labels (render exactly, all horizontal):
- COLUMN 1 top, grey: "UNKNOWN VENDOR" ; bottom, white-on-orange: "TRAIN VIA GUI, ZERO CODE"
- COLUMN 2 top, grey: "MODEL HALLUCINATES" ; bottom, white-on-orange: "DETERMINISTIC CHECK + EVIDENCE"
- COLUMN 3 top, grey: "10,000 DEVICES" ; bottom, white-on-orange: "QUEUE + FLEET, PARALLEL"

Constraint: 16:9, pure white ground. Only the labels listed. Exactly three columns; each risk sits directly above its answer.
```

---

## SLIDE 5 — IMPACT AND BENEFITS

### W5.1 — Days to minutes, nothing skipped  `[DATA-EXACT]` `[band]`
**Slide 5** · crop to a wide band (~4:1)
**Reject if:** the coverage figure isn't 100% · the time magnitudes read backwards · our values aren't the orange ones

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our system and the winning value. The status quo and secondary text in muted warm grey #5A6472; linework and text in ink #141417; light fills in #F4F4F4. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking; the big numeral in an elegant light serif. Minimal, generous white space. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no logo. 16:9.

Composition: two regions divided by a wide white gutter, each with a heading.
LEFT REGION (time): two horizontal bars stacked - a long muted-grey bar and a very short orange bar, the grey many times longer, each with a label at the left and a value at the right.
RIGHT REGION (coverage): a simple ring/donut mostly filled orange with a large light-serif "100%" in its centre, and beside it a short grey caption noting the manual shortfall.

Render style: clean flat editorial figure, bars and one donut as physical magnitudes. No axes, no legend.

Text labels (render exactly, all horizontal):
- LEFT heading, grey: "TIME TO FULL AUDIT"
- long bar, grey: "MANUAL - DAYS" ; short bar, orange: "WALRUS - MINUTES"
- RIGHT heading, grey: "CONTROL COVERAGE"
- centre of donut, orange, bold: "100%"
- under the donut, orange: "OF APPLICABLE CONTROLS, EVERY RUN"
- beside it, grey: "MANUAL AUDITS SKIP UNDER TIME"

Constraint: 16:9, pure white ground. Only the labels listed. "100%" must be exact; the grey time bar must be clearly many times longer than the orange one.
```

---

### W5.2 — Sovereign, and it scales  `[16:9]`
**Slide 5** · keep 16:9 · the NCIIPC / critical-infrastructure argument
**Reject if:** the "nothing leaves" seal is ambiguous · the word WALRUS appears more than once (vault only) · the scale grid repeats the wordmark · any eye glyph or empty placeholder box

```
Style: precise editorial-technical infographic in the Walrus Securitas brand system, for a printed report. PURE WHITE background hex #FFFFFF, absolutely flat — no gradient, no vignette, no texture, no coloured wash, no drop shadow on the background, no card behind the artwork, pure white to all four edges. ONE loud colour only — Walrus orange #FE5301 — reserved for our engine and the accent. Linework and text in ink #141417; infrastructure and secondary text in muted warm grey #5A6472; hazard/severed link may use red #E5484D; light fills in #F4F4F4. Absolutely NO teal, NO blue, NO green. Orange reticle ticks in the four corners. Labels in geometric MONOSPACE uppercase, wide tracking. Minimal, generous white space. ALL text horizontal. No watermarks, no borders beyond the corner ticks, no glow, no bevel, no gloss, no company logo. 16:9.

Composition: two panels side by side with a white gutter.
LEFT PANEL (sovereign): a simple ink vault/building outline containing a small orange WALRUS engine block labelled WALRUS in white, the word sitting directly and snugly on the orange fill with no inner box, outline or blank gap, and a small grey open-weight model chip. Around the building, a clear ink boundary ring. A severed network cable with a small red no-cloud badge crosses the boundary to show no external calls.
RIGHT PANEL (scale): three device-group icons of increasing size left to right - one device, a small cluster, a large grid - each device carrying one small solid-orange square mark (the engine) rather than the word WALRUS, and a rising orange arrow across them. Values under each group. The word WALRUS must NOT appear in this panel - it belongs only on the vault engine in the left panel.

Render style: clean flat diagram, light tint fills, two clear panels.

Text labels (render exactly, all horizontal):
- LEFT heading, orange: "NOTHING LEAVES THE BUILDING"
- inside the vault, grey: "OPEN-WEIGHT MODEL, ON-PREM"
- on the severed cable, grey: "NO EXTERNAL CALLS"
- LEFT footnote, grey: "FIT FOR CRITICAL INFRASTRUCTURE - NCIIPC"
- RIGHT heading, ink: "SAME ENGINE, ANY SCALE"
- under the three groups, one each, orange: "1 DEVICE" / "100" / "10,000"

Constraint: 16:9, pure white ground. Only the labels listed. The no-external-connection badge must be unambiguous. The three scale groups carry one small orange square mark per device, not the wordmark. WALRUS appears exactly once, on the vault engine in the left panel.
```

---

### W5.3 — The console (user experience)  `[light UI]` `[16:9]`
**Slide 5** · keep 16:9 · **prefer a real screenshot once the tool runs — this prompt is the fallback mock**
**Reject if:** it looks like a generic dark AI dashboard · the pass/fail counts aren't legible · any numeral wrong · any green or blue

```
Style: realistic modern LIGHT product-console UI screenshot in the Walrus Securitas brand system. PURE WHITE / near-white #FBFAF8 app background, crisp and flat, aligned to a grid. ONE loud colour only — Walrus orange #FE5301 — for active elements, the brand accent and progress. Text and chrome in ink #141417; secondary UI, rules and inactive state in muted warm grey #5A6472; panel fills in #F4F4F4. Findings use the severity scale only — critical #E5484D, high #FE5301, medium #E0A800, low #5A6472; a FAIL is red #E5484D, a PASS is a calm ink/grey tick, never green. Absolutely NO teal, NO blue, NO green, NO dark mode. Small orange reticle ticks may edge the frame. All labels geometric MONOSPACE uppercase, small, wide tracking; numerals in a clean light serif or the mono. Sharp, screenshot-like, minimal. 16:9.

Composition: a three-panel light dashboard screenshot.
LEFT PANEL: a live fleet monitor - a short vertical list of worker rows, each with a small orange activity bar, above a queue-depth readout and an overall progress line in orange.
CENTRE PANEL: one device's compliance result - a donut split into a large calm-grey PASS arc and a small red FAIL arc, with counts, above a scrollable list of failed controls, each row a control id, a severity chip (red/orange/gold), and a short title.
RIGHT PANEL: a generated report preview - a document thumbnail with a highlighted remediation block shown as a small monospace command snippet, its key command in orange.

Render style: realistic light dashboard UI, sharp, screenshot-like, aligned to a grid, generous white space.

Text labels (render exactly, all horizontal, uppercase):
- LEFT panel header: "FLEET - LIVE"
- LEFT readouts, two lines: "QUEUE 12 DEVICES" / "AUDITED 41 / 53"
- CENTRE panel header: "DEVICE: CORE-SW-01"
- in the donut, two values: "PASS 118" / "FAIL 14"
- one failed row example, red: "CIS 1.2.4  HIGH  TELNET ENABLED"
- RIGHT panel header: "REPORT"
- in the snippet, orange: "TRANSPORT INPUT SSH"

Constraint: 16:9, light ground. Only the labels listed. Must read as a real light-themed product console, not a dark abstract concept. Counts "41 / 53", "PASS 118", "FAIL 14" must render exactly; row lists illustrative. No green anywhere - PASS reads via the calm grey arc and an ink tick.
```

---

## After rendering

- `python3 ../kestrel-ppt/scripts/whiten.py images/<file>.png` on every image (snaps near-white to
  pure white, trims margin). Add `--transparent` only if a slide isn't white.
- **Optional polish:** composite the real walrus mark (`walrus-hq/branding/walrus-mark-orange-transparent.png`)
  beside the WALRUS wordmark on an engine block, in the PPT — never let the model draw it. The blocks
  already read correctly with the wordmark alone, so this is a nice-to-have, not a fix.
- Every `[DATA-EXACT]` numeral checked against the README's data anchors before it goes on a slide.
- Capture the **real** W5.3 console screenshot the moment the tool renders one — it beats the mock.
- Build body text and small tables natively in Aleo (display) / Host Grotesk (body) / Azeret Mono
  (labels) per `tokens.css`; export 6 pages, PDF, under 10 MB, nothing below 14 pt. Read every page at
  25% zoom — if the argument isn't legible as shapes and numbers, the hierarchy is wrong.
