#!/usr/bin/env python3
"""Build the SIH 2026 idea deck for Walrus Securitas (PS SIH26155).
Absolute-inch geometry so overlap is checkable. Emits deck.html + boxes.json.
Render to PDF: chrome --headless --print-to-pdf (see render note at bottom)."""
import html, json, pathlib

W, H   = 13.333, 7.5
M      = 0.28
KEY_Y, KEY_H = 0.92, 0.30
R1_LAB, R1_Y, R1_H = 1.40, 1.58, 3.34
R2_LAB, R2_Y = 5.08, 5.26
R2_H   = 6.98 - R2_Y
IMG2   = 4.62                       # row-2 image width
CW     = W - 2*M
GAP    = 0.16
COL    = (CW - GAP) / 2
boxes  = []
SLIDE  = [0]

def px(v): return f"{v:.4f}in"

def el(cls, x, y, w, h, inner="", style="", tag="div", track=True):
    if track: boxes.append(dict(slide=SLIDE[0], cls=cls, x=x, y=y, w=w, h=h))
    return (f'<{tag} class="ab {cls}" style="left:{px(x)};top:{px(y)};'
            f'width:{px(w)};height:{px(h)};{style}">{inner}</{tag}>')

def img(src, x, y, w, h, fit="contain"):
    return el("im", x, y, w, h,
              f'<img src="{src}" style="width:100%;height:100%;object-fit:{fit}">')

def lab(t, x, y, w):
    return el("lab", x, y, w, 0.18, html.escape(t))

def bullets(items):
    return "".join(f'<p><b>{html.escape(h)}</b> {b}</p>' for h, b in items)

def slide(title, body, n):
    return f'''<section class="s sl{n}">
  <div class="oval">Walrus<br>Securitas</div>
  <img class="slogo" src="img/sih-logo.png">
  <div class="tb"><h1>{html.escape(title)}</h1></div>
  {body}
  <div class="bar"></div>
  <div class="ft">@SIH Idea submission · PS 26155 · NTRO · Software · Blockchain &amp; Cybersecurity · <b>Walrus Securitas</b></div>
  <div class="pg">{n}</div>
</section>'''

S = []

# ------------------------------------------------------------- 1 TITLE
S.append(f'''<section class="s title">
  <img class="tmark" src="img/sih-mark.png">
  <h1 class="tev">SMART INDIA HACKATHON 2026</h1>
  <div class="tsub">TITLE PAGE</div>
  <ul class="tlist">
    <li><b>Problem Statement ID</b> &ndash; 26155</li>
    <li><b>Problem Statement Title</b> &ndash; AI-Driven Multi-Vendor Network Security Compliance Auditor</li>
    <li><b>Theme</b> &ndash; Blockchain &amp; Cybersecurity</li>
    <li><b>PS Category</b> &ndash; Software</li>
    <li><b>Team ID</b> &ndash; 133478</li>
    <li><b>Team Name</b> &ndash; Drone Syndicate</li>
  </ul>
  <div class="tfoot">The network compliance auditor, a capability of the Walrus Securitas AI security platform</div>
</section>''')

# ------------------------------------------------------------- 2 PROPOSED SOLUTION
SLIDE[0]=2
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>Misconfiguration, not zero-days, causes ~99% of firewall breaches. Yet every device from 40+ vendors is still hardened by hand, one CLI at a time.</b>")
b += lab("① ANY VENDOR CONFIG IN → ONE HARDENING REPORT OUT", M, R1_LAB, COL)
b += lab("② PROPRIETARY SYNTAX → ONE VENDOR-NEUTRAL MODEL", M+COL+GAP, R1_LAB, COL)
b += img("img/w2-1.png", M, R1_Y, COL, R1_H)
b += img("img/w2-2.png", M+COL+GAP, R1_Y, COL, R1_H)
b += lab("③ WHY IT MATTERS", M, R2_LAB, IMG2)
b += el("shead", M+IMG2+GAP, R2_LAB, CW-IMG2-GAP, 0.20,
        "&#10022; <u>Proposed Solution</u> (Describe your Idea / Solution / Prototype)")
b += img("img/w2-3.png", M, R2_Y, IMG2, R2_H)
b += el("tx", M+IMG2+GAP, R2_Y+0.22, CW-IMG2-GAP, R2_H-0.22, bullets([
  ("Detailed explanation:",
   "Walrus ingests any network-device config from Cisco, Juniper, Arista, Palo Alto, firewalls, "
   "switches, cloud security groups. The AI reads it into <b>one vendor-neutral Security Baseline "
   "Model</b>; a deterministic engine then checks every control from <b>CIS, NIST SP&nbsp;800-53, "
   "DISA STIG and ISO&nbsp;27001</b> and emits a per-device PDF with pass/fail, severity and the "
   "exact fix commands."),
  ("How it addresses the problem:",
   "It replaces slow manual checklist auditing and rigid, vendor-locked suites with <b>one source of "
   "truth</b> across a heterogeneous fleet. An unseen vendor is taught through a low-code training "
   "GUI, with <b>no code redeploy</b>."),
  ("Innovation and uniqueness:",
   "The AI <b>only parses</b>; the verdict is deterministic and every finding <b>cites its exact "
   "config line</b>, so it never hallucinates a pass/fail. A checklist gate makes it structurally "
   "<b>unable to skip a control</b>."),
]))
S.append(slide("PROPOSED SOLUTION", b, 2))

# ------------------------------------------------------------- 3 TECHNICAL APPROACH
SLIDE[0]=3
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>Orchestrator → queue → a fleet of workers that pull work, each with its own harness and one shared live ledger, built so it cannot skip a single control.</b>")
b += lab("① THE ENGINE · WORKERS PULL, LEDGER TRACKS, NOTHING CLASHES", M, R1_LAB, COL)
b += lab("② THE AI PIPELINE · ONE CONFIG'S JOURNEY, WITH A LEARN LOOP", M+COL+GAP, R1_LAB, COL)
b += img("img/w3-2.png", M, R1_Y, COL, R1_H)
b += img("img/w3-3.png", M+COL+GAP, R1_Y, COL, R1_H)
b += lab("③ FOUR STAGES, END TO END", M, R2_LAB, IMG2)
b += el("shead", M+IMG2+GAP, R2_LAB, CW-IMG2-GAP, 0.20, "&#10022; <u>Technical Approach</u>")
b += img("img/w3-1.png", M, R2_Y, IMG2, R2_H)
b += el("tx", M+IMG2+GAP, R2_Y+0.22, CW-IMG2-GAP, R2_H-0.22, bullets([
  ("Technologies used:",
   "Config collection via <b>Netmiko / NAPALM</b>, upload or a config repo; an <b>open-weight LLM</b> "
   "(NLP + pattern) for parsing, run on-prem; a deterministic rules engine over a <b>control "
   "knowledge base</b> (CIS / NIST 800-53 / STIG / ISO 27001); <b>ReportLab</b> for the per-device "
   "PDF. Built on the Walrus Harness engine."),
  ("Methodology and process:",
   "The orchestrator writes one task per device to a queue; <b>workers pull work</b>, each running "
   "the harness, and a <b>shared live ledger</b> shows who is doing what and lets workers pause on a "
   "clash. When a config cross-references another object such as a nested ACL or a linked device, "
   "it is re-queued and run through the <b>full</b> control set, so coverage never leaks."),
  ("Never miss, never lie:",
   "The knowledge base <b>is</b> the checklist. The fleet must return a verdict for every "
   "applicable control before an audit can close; the model only proposes fields, the engine decides, "
   "and every verdict is backed by an <b>append-only evidence log</b>."),
]))
S.append(slide("TECHNICAL APPROACH", b, 3))

# ------------------------------------------------------------- 4 FEASIBILITY
SLIDE[0]=4
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>Built on proven pieces like the Walrus Harness engine, Netmiko/NAPALM and public benchmarks, and it runs air-gapped, so it fits critical infrastructure.</b>")
b += lab("① RUNS ANYWHERE · EASY TO INTEGRATE", M, R1_LAB, COL)
b += lab("② WHY IT CANNOT HALLUCINATE A VERDICT", M+COL+GAP, R1_LAB, COL)
b += img("img/w4-1.png", M, R1_Y, COL, R1_H)
b += img("img/w4-2.png", M+COL+GAP, R1_Y, COL, R1_H)
b += lab("③ THREE RISKS, THREE ANSWERS", M, R2_LAB, IMG2)
b += el("shead", M+IMG2+GAP, R2_LAB, CW-IMG2-GAP, 0.20, "&#10022; <u>Feasibility and Viability</u>")
b += img("img/w4-3.png", M, R2_Y, IMG2, R2_H)
b += el("tx", M+IMG2+GAP, R2_Y+0.22, CW-IMG2-GAP, R2_H-0.22, bullets([
  ("Feasibility:",
   "The orchestration, evidence and checklist engine already exists (Walrus Harness). Netmiko/NAPALM "
   "and the four frameworks are mature and public; an open-weight model runs on a mid-range GPU "
   "on-prem. Deployable on an <b>air-gapped server, private cloud or a single laptop</b>."),
  ("Potential challenges and risks:",
   "Unseen vendor firmware breaks fixed parsers · an LLM can hallucinate · a 10,000-device fleet is "
   "slow to audit by hand · configs cross-reference each other."),
  ("Strategies for overcoming them:",
   "Unknown vendor → <b>train via GUI, zero code</b>. Hallucination → <b>deterministic check + cited "
   "evidence</b>, no model on the verdict. Scale → <b>queue + worker fleet, in parallel</b>. "
   "Cross-references → re-queued through the full control set. And <b>nothing leaves the building</b> "
   "with no external calls, fit for NCIIPC-class infrastructure."),
]))
S.append(slide("FEASIBILITY AND VIABILITY", b, 4))

# ------------------------------------------------------------- 5 IMPACT
SLIDE[0]=5
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>A manual audit of one device takes an analyst half a day and still skips controls under time pressure. Walrus does the whole fleet in minutes, missing none.</b>")
b += lab("① DAYS → MINUTES · 100% OF CONTROLS, EVERY RUN", M, R1_LAB, COL)
b += lab("② WHAT THE OPERATOR SEES · LIVE FLEET, PER-DEVICE REPORT", M+COL+GAP, R1_LAB, COL)
b += img("img/w5-1.png", M, R1_Y, COL, R1_H)
b += img("img/w5-3.png", M+COL+GAP, R1_Y, COL, R1_H)
b += lab("③ SOVEREIGN, AND IT SCALES", M, R2_LAB, IMG2)
b += el("shead", M+IMG2+GAP, R2_LAB, CW-IMG2-GAP, 0.20, "&#10022; <u>Impact and Benefits</u>")
b += img("img/w5-2.png", M, R2_Y, IMG2, R2_H)
b += el("tx", M+IMG2+GAP, R2_Y+0.22, CW-IMG2-GAP, R2_H-0.22, bullets([
  ("Impact on the target audience:",
   "NOC and security teams, CISOs and <b>critical-infrastructure operators (NCIIPC)</b> get a "
   "continuous, single source of truth for hardening compliance across <b>any</b> vendor, so "
   "the audit that took days now runs before the change window closes."),
  ("Security:",
   "Misconfiguration is the <b>#1 cause of breaches</b>; catching every hardening gap on every device "
   "shrinks exactly the attack surface that causes most of them."),
  ("Economic & environmental:",
   "Replaces expensive vendor-locked suites and days of analyst time; <b>one engine scales 1 → "
   "10,000 devices</b> with no per-vendor licensing. Open-weight and on-prem: no cloud spend, "
   "<b>no data leaves the building</b>."),
]))
S.append(slide("IMPACT AND BENEFITS", b, 5))

# ------------------------------------------------------------- 6 REFERENCES
SLIDE[0]=6
RC = (CW - GAP*2) / 3
b  = el("key", M, KEY_Y, CW, KEY_H,
        "<b>Every control traces to a published standard, and every verdict in the tool cites the exact config line it came from.</b>")
b += el("shead", M, 1.30, CW, 0.20, "&#10022; <u>Research and References</u>")
refs = [
 ("Frameworks &amp; standards", [
  "<b>CIS Benchmarks</b>: per-vendor hardening baselines (Cisco, Juniper, Arista, PAN-OS&hellip;)",
  "<b>NIST SP 800-53 Rev.&nbsp;5</b>: security &amp; privacy controls catalogue",
  "<b>DISA STIGs</b>: hardening guides, per network device",
  "<b>ISO/IEC 27001:2022</b>: Annex&nbsp;A, 93 controls",
  "<a href='https://nciipc.gov.in/'><b>NCIIPC</b></a>: Critical Information Infrastructure protection (PS reference)",
 ]),
 ("Method &amp; tooling", [
  "<b>Netmiko / NAPALM</b>: multi-vendor config collection",
  "<b>Open-weight LLM</b>: on-prem parsing, no external calls",
  "<b>ReportLab</b>: per-device PDF with remediation CLI",
  "<b>Walrus Harness</b>: our engine, evidence log + the &lsquo;miss-nothing&rsquo; checklist gate",
  "<b>Gartner</b>: ~99% of firewall breaches are misconfigurations, not flaws",
 ]),
 ("Our own build", [
  "<b>Live product page + demo</b>: open the link below or scan the code",
  "<b>Runs air-gapped</b>: open-weight model, on-prem, no data leaves",
  "<b>Deterministic verdicts</b>: every finding cites its config line",
  "Part of the <b>Walrus Securitas</b> AI security platform",
 ]),
]
for i, (h_, items) in enumerate(refs):
    x = M + i*(RC+GAP)
    b += lab(h_.replace("&amp;","&"), x, 1.56, RC)
    b += el("rf", x, 1.76, RC, 2.02, "".join(f"<p>{t}</p>" for t in items))
b += el("cta", M, 3.94, CW, 1.04, '''
  <img src="img/qr.png">
  <div class="ctatx">
    <div class="ctah">&#10022; TRY THE LIVE NETWORK COMPLIANCE AUDITOR</div>
    <a href="https://walrussecuritas.com/product/network-compliance-auditor">walrussecuritas.com/product/network-compliance-auditor</a>
    <div class="ctas">Scan the code or open the link for a real audit on sample Cisco / Juniper / Arista configs, in your browser.</div>
  </div>''')
b += lab("FRAMEWORK COVERAGE · ONE NEUTRAL MODEL, FOUR STANDARDS, ANY VENDOR", M, 5.12, CW)
b += el("tbl", M, 5.32, CW, 1.64, """
 <table>
  <tr><th>Framework</th><th>What it hardens</th><th>Example control the engine checks</th><th>In scope</th></tr>
  <tr class="hi"><td><b>CIS Benchmarks</b></td><td>Per-vendor device baselines</td><td>SSH v2 enforced; Telnet / HTTP disabled</td><td>Cisco, Juniper, Arista, PAN-OS, &hellip;</td></tr>
  <tr><td><b>NIST SP 800-53</b></td><td>Access, audit, comms controls</td><td>AC-17 remote access; AU-12 audit logging</td><td>All device classes</td></tr>
  <tr class="hi"><td><b>DISA STIG</b></td><td>DoD hardening, per device</td><td>SNMP community not &lsquo;public&rsquo;; NTP set</td><td>Routers, switches, firewalls</td></tr>
  <tr><td><b>ISO/IEC 27001</b></td><td>Annex A, 93 controls</td><td>A.8.20 network security; A.8.9 config mgmt</td><td>Org-wide baseline</td></tr>
  <tr class="mu"><td><b>New / white-box vendor</b></td><td>Unrecognised CLI</td><td colspan="2">taught once via the low-code training GUI, then checked against all of the above</td></tr>
 </table>""")
S.append(slide("RESEARCH AND REFERENCES", b, 6))

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Aleo:wght@300;400;700&family=Host+Grotesk:wght@400;500;600;700&family=Azeret+Mono:wght@500;600&display=swap');
@page{size:13.333in 7.5in;margin:0}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;padding:0;background:#fff;
 font-family:"Host Grotesk",Arial,Helvetica,sans-serif;color:#141417}
.s{position:relative;width:13.333in;height:7.5in;overflow:hidden;background:#fff;
 page-break-after:always;break-after:page}
.s:last-child{page-break-after:auto}
.ab,.tb,.bar,.ft,.pg,.oval,.slogo{position:absolute}
.tb{left:1.9in;top:0;width:9.53in;height:.9in;display:flex;align-items:center;justify-content:center}
.tb h1{font-family:"Aleo","Times New Roman",serif;font-weight:700;font-size:29pt;margin:0;
 letter-spacing:-.005em;color:#141417;text-align:center}
.oval{left:.30in;top:.22in;width:1.42in;height:.66in;border:.022in solid #FE5301;border-radius:50%;
 display:flex;align-items:center;justify-content:center;text-align:center;
 font-family:"Host Grotesk",Arial,sans-serif;font-size:9.5pt;font-weight:600;line-height:1.14;color:#141417}
.cta{display:flex;align-items:center;gap:.34in;background:#F6F6F4;
 border-radius:.05in;padding:.16in .3in;overflow:hidden}
.cta img{height:.9in;width:.9in;flex:none;background:#fff}
.ctatx{display:flex;flex-direction:column;gap:.07in;overflow:hidden}
.ctah{font-family:"Azeret Mono",monospace;font-size:11.5pt;font-weight:600;letter-spacing:.05em;color:#FE5301}
.cta a{font-family:"Azeret Mono",monospace;font-size:13.5pt;color:#141417;
 text-decoration:underline;text-decoration-color:#FE5301;word-break:break-all}
.ctas{font-size:10pt;line-height:1.3;color:#5A6472}
.slogo{right:.34in;top:.16in;width:1.18in}
.bar{left:0;top:7.10in;width:13.333in;height:.40in;background:#141417}
.ft{left:.30in;top:7.185in;font-family:"Azeret Mono",monospace;font-size:7.4pt;
 color:rgba(255,255,255,.82);letter-spacing:.02em}
.ft b{color:#FE5301;font-weight:600}
.pg{right:.32in;top:7.15in;font-size:12pt;color:#FE5301;font-weight:700;font-family:"Azeret Mono",monospace}
.key{font-size:11pt;line-height:1.24;color:#141417;display:flex;align-items:center;
 padding-left:0}
.key b{font-weight:600}
.shead{font-family:"Azeret Mono",monospace;font-size:8.6pt;font-weight:600;color:#141417;
 letter-spacing:.01em;overflow:hidden;white-space:nowrap;display:flex;align-items:center}
.shead u{text-decoration-color:#FE5301}
.lab{font-family:"Azeret Mono",monospace;font-size:7pt;font-weight:600;letter-spacing:.05em;
 color:#5A6472;text-transform:uppercase;overflow:hidden;white-space:nowrap}
.im{overflow:hidden;border:.008in solid #ECECEC;border-radius:.04in;background:#fff}
.im img{display:block}
.tx{overflow:hidden}
.tx p{margin:0 0 .062in;font-size:var(--txs,8.2pt);line-height:1.32;color:#2b2b30;
 padding-left:.135in;text-indent:-.135in}
.tx p::before{content:"\\25AA  ";color:#FE5301;font-weight:700}
.tx p b{color:#141417;font-weight:600}
.rf{overflow:hidden}
.rf p{margin:0 0 .085in;font-size:10pt;line-height:1.32;color:#2b2b30;
 padding-left:.16in;text-indent:-.16in}
.rf p::before{content:"\\25B8  ";color:#FE5301;font-weight:700}
.rf a,.rf b{color:#141417}.rf a{text-decoration:underline;text-decoration-color:#FE5301}
a{color:#FE5301;text-decoration:underline}
.tbl table{border-collapse:collapse;width:100%}
.tbl th{font-family:"Azeret Mono",monospace;font-size:8pt;text-transform:uppercase;
 letter-spacing:.04em;color:#5A6472;text-align:left;padding:.04in .1in;
 border-bottom:.016in solid #FE5301;font-weight:600}
.tbl td{font-size:9.4pt;padding:.052in .1in;border-bottom:.007in solid #ECECEC;color:#2b2b30}
.tbl td b{color:#141417}
.tbl tr.hi td{background:#FCF2EC}
.tbl tr.mu td{color:#5A6472;font-style:italic;background:#F7F7F7}
.sl2{--txs:8.4pt}.sl3{--txs:8.2pt}.sl4{--txs:8.7pt}.sl5{--txs:9.4pt}
/* ---- title slide ---- */
.title{display:block}
.twm{position:absolute;left:.62in;top:.6in;font-family:"Azeret Mono",monospace;font-size:15pt;
 font-weight:600;letter-spacing:.05em;color:#141417;display:flex;align-items:center}
.twm b{font-weight:600;color:#FE5301;margin-left:.09in}
.twm .sq{width:.22in;height:.22in;background:#FE5301;border-radius:.03in;margin-right:.16in}
.tlogo{position:absolute;right:.5in;top:.5in;width:1.9in}
.tmark{position:absolute;right:.62in;top:2.55in;width:3.15in;opacity:.96}
.tev{position:absolute;left:0;top:1.28in;width:11.6in;text-align:center;margin:0;
 font-family:"Aleo","Times New Roman",serif;font-size:44pt;font-weight:700;color:#141417}
.tsub{position:absolute;left:0;top:2.5in;width:11.6in;text-align:center;
 font-family:"Azeret Mono",monospace;font-size:18pt;font-weight:600;letter-spacing:.14em;color:#FE5301}
.tlist{position:absolute;left:.82in;top:3.2in;width:8.35in;margin:0;padding:0;list-style:none}
.tlist li{font-size:18pt;line-height:1.3;color:#141417;margin-bottom:.17in;
 padding-left:.4in;text-indent:-.4in}
.tlist li::before{content:"\\25AA  ";color:#FE5301;font-weight:700}
.tlist b{font-weight:600}
.tfoot{position:absolute;left:.82in;top:6.5in;font-family:"Azeret Mono",monospace;
 font-size:10pt;letter-spacing:.02em;color:#5A6472}
"""
out = ("<!doctype html><html><head><meta charset='utf-8'><title>Walrus Securitas · SIH26155</title>"
       f"<style>{CSS}</style></head><body>" + "".join(S) + "</body></html>")
pathlib.Path("deck.html").write_text(out)
json.dump(boxes, open("boxes.json","w"), indent=1)

# ---- overlap check (content boxes only, per slide) ----
def overlap(a,b):
    return not (a['x']+a['w']<=b['x'] or b['x']+b['w']<=a['x']
                or a['y']+a['h']<=b['y'] or b['y']+b['h']<=a['y'])
bad=[]
for i in range(len(boxes)):
    for j in range(i+1,len(boxes)):
        if boxes[i]['slide']==boxes[j]['slide'] and overlap(boxes[i],boxes[j]):
            bad.append((boxes[i],boxes[j]))
off=[x for x in boxes if x['x']<0 or x['y']<0 or x['x']+x['w']>W+1e-6 or x['y']+x['h']>H+1e-6]
print(f"deck.html · {len(S)} slides · {len(boxes)} tracked boxes")
print(f"overlaps: {len(bad)} · off-page: {len(off)}")
for a,b_ in bad: print("  OVERLAP s%d %s × %s"%(a['slide'],a['cls'],b_['cls']))
for x in off: print("  OFFPAGE s%d %s @%.2f,%.2f %.2f×%.2f"%(x['slide'],x['cls'],x['x'],x['y'],x['w'],x['h']))
