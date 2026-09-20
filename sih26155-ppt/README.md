# Walrus Securitas — SIH26155 idea presentation kit

> **PS:** SIH26155 · **NTRO** · Software · Blockchain & Cybersecurity
> **Idea:** the Walrus Securitas **network compliance auditor** — reads any vendor's device config
> and checks every hardening control (CIS / NIST / STIG / ISO) without missing one. A capability
> inside the Walrus Securitas AI security platform, not a standalone product.
> **Deadline:** 20 Sep 2026 · portal deliverable = the SIH idea PPT (6 pages, PDF).
> **The PS's own "Deliverables for Evaluation":** GitHub link · README · 2-page arch doc · 2-min demo
> video · 5-slide technical presentation. Confirm which stage wants which before exporting.

**Branding: Walrus Securitas throughout.** This is not a new product — it's the *network compliance
auditor* module of the Walrus Securitas platform: the same engine as the Walrus Harness, pointed at
device configs instead of live targets. The title slide reads **Walrus Securitas**, tagged "network
compliance auditor · part of the Walrus Securitas security platform" so the module is positioned
without diluting focus on SIH26155.

---

## The build question — answered

**Do NOT ship a landing page. Ship the tool running, with real config samples and a real key.**

Three reasons, in order of weight:

1. **The PS asks for it literally.** Its evaluation deliverables name a *Source Code Link* and a
   *2-minute Demo Video*. A landing page satisfies neither. A tool that ingests a Cisco config and
   spits out a real pass/fail PDF satisfies both in one artefact.
2. **It's our whole edge.** Kestrel won trust on a live HuggingFace demo + real measured Qualcomm
   numbers, not a mockup. A landing page is a *claim*; a running audit is *proof*. Criterion #8 is
   literally "user experience" and criteria include feasibility + practicability — a working tool
   scores all three at once.
3. **Half the engine already exists.** Walrus Harness gives us the orchestrator loop, the
   checklist-completeness gate (RUNG-07 — "tick every applicable line before the phase can exit"),
   the normalized findings schema, the append-only evidence log, and the auto-report generator. We
   are *not* starting from zero — we bolt a config-normalizer + a framework-check layer + a training
   GUI onto a spine that's built.

**What "running" means for the demo (so a judge needs no key of their own):**

- Live tool: upload a config → real model call → real normalized model → real pass/fail against a
  real CIS/STIG control set → real per-device PDF. Use a rate-limited key behind the server.
- Plus a **"Load sample" button** that replays a *real, pre-run* audit on a bundled Cisco / Juniper /
  Arista config, so the demo works cold, offline, in front of a judge with no internet — exactly the
  way the Kestrel HuggingFace space runs in-browser. The cached run is real output, not faked.
- A thin landing wrapper is fine (hero → "Try it" → the tool), but the tool is the submission.

**If the idea deadline is genuinely today:** the 6-page PDF is the only thing that must go in now.
Stand up the *minimum real thing* alongside it — one config in, one real PDF out, one real key — and
put its URL + GitHub on Slide 6. Full product (bulk ingest, training GUI, all four frameworks) is the
finale build. Minimum-real beats maximum-mockup every time.

---

## The 6-slide argument (template is fixed: Title · Solution · Approach · Feasibility · Impact · References)

Read cold, offline, nobody presenting. Every visual carries its own labels. Max 6 pages, PDF, points
& diagrams not paragraphs. Budget per content slide: **two 16:9 panels + one ~4:1 band = 3 visuals.**

| # | Slide | Visuals | The one thing it must land |
|---|---|---|---|
| 1 | Title | — | Walrus Securitas · SIH26155 · NTRO · team block. Tag: "network compliance auditor". Quiet, typographic. |
| 2 | Proposed Solution | W2.1 flow · W2.2 funnel · W2.3 `[DATA-EXACT]` | Misconfiguration is the #1 breach cause. One config in → one hardening report out, for **any** vendor. |
| 3 | **Technical Approach** ← the focus | W3.1 quick arch · W3.2 agent arch · W3.3 AI pipeline | Orchestrator → queue → worker fleet, each with its own harness, one shared live ledger, and a checklist gate that **cannot skip a control**. |
| 4 | Feasibility & Viability | W4.1 runs-anywhere · W4.2 trust design · W4.3 risks | Air-gapped or cloud, any vendor, easy integration. The AI never *decides* — it parses; the check is deterministic and every finding cites a config line. |
| 5 | Impact & Benefits | W5.1 `[DATA-EXACT]` · W5.2 sovereign+scale · W5.3 dashboard | Days → minutes. 100% control coverage. Nothing leaves the building. 1 device or 10,000. |
| 6 | Research & References | — | CIS · NIST 800-53 · DISA STIG · ISO 27001 · Netmiko/NAPALM · NCIIPC · + the Walrus Harness we built. |

Slides 1 and 6 have **no prompts** by design (typographic view slides). All architecture diagrams are
**Tier-2 (pure-white infographic)**; only the dashboard (W5.3) is **Tier-1 (dark screenshot)**. Same
rule as Kestrel: diagrams are page furniture, screenshots are windows.

---

## What maps from Walrus, what's new (the honest split)

| Deck claim | Where it comes from | State |
|---|---|---|
| Orchestrator → workers, each with a harness | Walrus Harness core loop | **built** |
| "Misses no control" checklist gate | Harness RUNG-07 phase-exit checklist — swap vuln list for control list | **built, re-pointed** |
| Every finding cites evidence, nothing claimed unproven | Harness append-only JSONL session log | **built** |
| Per-device PDF report | Harness findings → REPORT.md generator → PDF | **built, re-skinned** |
| Queue + shared live ledger + workers coordinate to avoid collisions | Arrow-arch (MAP/ledger, packet-per-task, workers write own files) + user's pull-model design | **design done, wiring new** |
| Read any vendor CLI without a hard-coded parser | model-driven interpretation (harness already assumes this) | **new domain layer** |
| Normalize → vendor-neutral Security Baseline Model | — | **new** |
| CIS/NIST/STIG/ISO controls as machine-checks | the knowledge base (below) | **new — biggest content lift** |
| Train a new vendor via GUI, no code redeploy | — | **new** |
| Remediation CLI per device/model | model drafts, deterministic layer validates | **new** |

Roughly: orchestration + evidence + "miss nothing" spine is **done**; the network-config domain layer
and the control knowledge base are the **fresh** work.

---

## The knowledge base — "so our AI does not miss anything"

The vulnerability/hardening list a junior analyst gets handed by a CISO, but deeper and machine-loaded
so the fleet can't skip a line. For this PS it is the **control knowledge base** — one entry per
hardening check, per device class:

```
control_id:      CIS-CISCO-IOS-1.2.4  (or NIST AC-2, STIG-xxxx, ISO A.8.9)
title:           Disable Telnet on all VTY lines
device_class:    router | switch | firewall | l3-switch | cloud-sg
frameworks:      [CIS, STIG, NIST-800-53:AC-17, ISO-27001:A.8.20]
severity:        high
why:             cleartext admin protocol → credential capture on the wire
check:           normalized_model.mgmt.telnet_enabled == false
evidence_hint:   line vty / transport input
remediation_cli: {cisco_ios: "line vty 0 4 / transport input ssh", juniper: "...", arista: "..."}
```

This is the exact artefact that makes the checklist gate real: the fleet must return a pass/fail for
**every** control whose `device_class` matches the ingested device before the audit can close. It's
W4.2's visual, and it's a standalone build deliverable. **Say the word and I'll draft the seed KB**
(a starter set of CIS/STIG controls in this schema, YAML or JSONL) as the next step — it drops
straight onto the harness's checklist loader.

---

## Brand system — Walrus Securitas, not a generic deck

Every prompt is built on the real Walrus brand tokens
(`walrus-hq/graphic-designer/lib/tokens.css` — the single source):

- **Orange `#FE5301` is the only colour that shouts** — Walrus, our system, the winning value. One
  loud note per frame. Everything else is **ink `#141417` on white**, with the status quo drawn in
  muted **grey `#5A6472`**. Deep partner `#D84600` only for the learning loop.
- **Findings use the severity scale** and nothing else: crit `#E5484D` · high `#FE5301` · med
  `#E0A800` · low `#5A6472`. FAIL = red, PASS = a calm ink tick. **No green, no teal, no blue.**
- **Signature devices:** orange corner reticle ticks · monospace uppercase labels (Azeret Mono) ·
  light-serif stat numerals (Aleo) · an orange eyebrow tab · one orange marker-highlight swipe.
- **Engine blocks are just a clean orange rectangle with the WALRUS wordmark** — no icon, no empty
  placeholder box, and the old eye/"I" glyph is gone. The model never draws a logo. *Optional:*
  composite the real mark (`walrus-hq/branding/walrus-mark-orange-transparent.png`) beside the wordmark
  in the PPT for polish. Body/tables set in Aleo / Host Grotesk / Azeret Mono per tokens.

## Prompts

All in [`PROMPTS.md`](PROMPTS.md). Each block is self-contained — the Walrus brand prefix is merged
in, copy the whole fenced block and paste. Route to whichever image model renders in-image text most
faithfully (Nano Banana Pro / Gemini 3 Pro Image / GPT Image). Reuse `../kestrel-ppt/scripts/whiten.py`
to snap near-white to pure `#FFFFFF` after each render. Real artefacts (a Cisco IOS config snippet,
the walrus mark, the actual console screenshot) are captured or composited, never generated.
