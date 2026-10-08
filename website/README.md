# BeStMeta documentation website

This folder builds a static documentation website for the LinkML schema at the
**repository root** (`../bestmeta_schema.yaml`) and publishes it to GitHub Pages
via `.github/workflows/docs.yml`.

The site has an **Introduction** page and an **Overview on the Schema** section
with one page per class (each listing its slots), plus an auto-generated
**Enums & Types** reference.

## Build locally
```bash
cd website
python -m venv .venv && source .venv/bin/activate 
pip install -r requirements.txt
python scripts/build_site.py
mkdocs serve
```
Re-run `build_site.py` whenever the schema changes. `mkdocs build --strict`
reproduces exactly what CI does (output in `website/site/`).

## Note on the existing `docs/` folder
This website uses `website/docs/`, which is separate from the repository's
top-level `docs/` folder — nothing there is touched.
