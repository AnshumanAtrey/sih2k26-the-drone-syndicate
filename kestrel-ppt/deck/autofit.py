import subprocess, re, pymupdf, pathlib, shutil
BAR, TARGET = 7.10, 0.18
src = pathlib.Path("build.py").read_text(encoding="utf-8")
cur = {2:8.1, 3:8.1, 4:8.1, 5:8.1}
def render(sizes):
    t = src
    for k,v in sizes.items(): t = t.replace(f"__S{k}__", f"{v:.2f}pt")
    pathlib.Path("_fit.py").write_text(t, encoding="utf-8")
    subprocess.run(["/Users/atrey/.venvs/qaihub/bin/python","_fit.py"],capture_output=True)
    subprocess.run(["/Applications/Brave Browser.app/Contents/MacOS/Brave Browser","--headless",
        "--disable-gpu","--no-pdf-header-footer","--virtual-time-budget=15000",
        "--print-to-pdf=_fit.pdf",f"file://{pathlib.Path('deck.html').resolve()}"],capture_output=True)
    d=pymupdf.open("_fit.pdf"); out={}
    for i in range(1,5):
        lo=0
        for b in d[i].get_text("dict")["blocks"]:
            for l in b.get("lines",[]):
                for sp in l["spans"]:
                    if sp["text"].strip():
                        y=sp["bbox"][3]/72
                        if y < BAR-0.02 and y > lo: lo=y
        out[i+1]=BAR-lo
    d.close(); return out
for it in range(6):
    gaps = render(cur)
    print(f"iter {it}: " + "  ".join(f"s{k} {cur[k]:.2f}pt gap {gaps[k]:.2f}in" for k in sorted(cur)), flush=True)
    if all(abs(gaps[k]-TARGET) < 0.10 for k in cur): break
    for k in cur:
        if gaps[k] > TARGET + 0.10: cur[k] = min(11.5, cur[k] * (1 + min(0.22,(gaps[k]-TARGET)*0.30)))
        elif gaps[k] < TARGET - 0.10: cur[k] = cur[k] * 0.955
print("FINAL:", {k:round(v,2) for k,v in cur.items()})
final = src
for k,v in cur.items(): final = final.replace(f"__S{k}__", f"{v:.2f}pt")
pathlib.Path("build.py").write_text(final, encoding="utf-8")
