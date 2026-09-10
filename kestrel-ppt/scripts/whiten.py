#!/usr/bin/env python3
"""
Clean a tier-2 (light) render so it drops onto the white SIH template with no visible edge.

Two things go wrong with generated "white" backgrounds: the white is #FDFDFC rather than #FFFFFF,
and there is often a faint vignette at the corners. Either one shows up as a grey rectangle on a
white slide. This snaps near-white to pure white, optionally makes it transparent, and trims the
surrounding white so the artwork can be placed tight.

Usage
  python3 scripts/whiten.py images/P5.1-survival-wall.png
  python3 scripts/whiten.py images/*.png --transparent
  python3 scripts/whiten.py images/P4.1-cost-ladder.png --threshold 232 --no-trim

Writes <name>-clean.png next to the input. Never overwrites the original.
"""
import argparse, sys
from pathlib import Path
from PIL import Image

def clean(path: Path, threshold: int, transparent: bool, trim: bool, pad: int) -> Path:
    im = Image.open(path).convert("RGB")
    px = im.load()
    w, h = im.size

    # 1. snap near-white to pure white
    snapped = 0
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if r >= threshold and g >= threshold and b >= threshold:
                if (r, g, b) != (255, 255, 255):
                    px[x, y] = (255, 255, 255)
                    snapped += 1

    # 2. trim the pure-white margin
    if trim:
        bbox = Image.eval(im, lambda v: 255 - v).getbbox()
        if bbox:
            l, t, r_, b_ = bbox
            im = im.crop((max(0, l - pad), max(0, t - pad),
                          min(w, r_ + pad), min(h, b_ + pad)))

    # 3. optional alpha
    if transparent:
        im = im.convert("RGBA")
        d = im.getdata()
        im.putdata([(r, g, b, 0) if (r, g, b) == (255, 255, 255) else (r, g, b, a)
                    for r, g, b, a in d])

    out = path.with_name(path.stem + "-clean.png")
    im.save(out)
    print(f"{path.name:<38} {w}x{h} -> {im.size[0]}x{im.size[1]}  "
          f"snapped {snapped:,}px{'  +alpha' if transparent else ''}")
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--threshold", type=int, default=244,
                    help="channel value at or above which a pixel counts as white (default 244). "
                         "Lower it if a vignette survives; raise it if pale tints get eaten.")
    ap.add_argument("--transparent", action="store_true",
                    help="also make the white transparent (only needed on a non-white slide)")
    ap.add_argument("--no-trim", dest="trim", action="store_false",
                    help="keep the original white margin instead of cropping to the artwork")
    ap.add_argument("--pad", type=int, default=12, help="pixels of white to keep when trimming")
    a = ap.parse_args()

    missing = [f for f in a.files if not f.exists()]
    if missing:
        sys.exit(f"not found: {', '.join(str(m) for m in missing)}")
    for f in a.files:
        clean(f, a.threshold, a.transparent, a.trim, a.pad)

if __name__ == "__main__":
    main()
