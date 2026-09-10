# vendor/

`scrape_sih_upstream.py` — verbatim copy of `scripts/scrape_sih.py` from
[vedantchalke36/sih-2026-problem-statements](https://github.com/vedantchalke36/sih-2026-problem-statements)
(MIT, © 2026 Vedant Chalke — see `LICENSE-upstream-MIT`).

We reuse its `fetch_html()`, `parse()` and `fix_text()` (mojibake repair table) instead of
writing a parser from scratch. `../build.py` imports those three and adds what upstream
does not capture:

- `ps_id` — the modal's own **Problem Statement ID** field (e.g. `26001`)
- `modal_title` — the title as printed inside the modal (differs from the table link on some rows)

Nothing in this file is executed as a script; only imported. Do not edit it — if upstream
changes, re-copy and re-check `build.py`'s field additions.
