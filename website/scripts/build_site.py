#!/usr/bin/env python3
"""
Build the static documentation site for a LinkML schema.

Steps:
  1. Read personalization from site.config.yml
  2. Run LinkML's `gen-doc` to turn the schema into Markdown pages
  3. Split the generated pages into "Classes" and "Enums & Types" (reference)
  4. Auto-generate a navigation menu:
        - Introduction        (docs/index.md, hand-written)
        - Overview on the Schema
              <one entry per class>
        - Enums & Types        (reference section, optional)
  5. Emit a fully-populated mkdocs.yml

Nothing here is schema-specific: point `schema_file` at any LinkML schema
and it works.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "site.config.yml"
DOCS_DIR = ROOT / "docs"
# All LinkML-generated pages live together in one flat folder so that the
# relative cross-links gen-doc emits (Class -> slot -> enum) keep working.
GEN_DIR = DOCS_DIR / "schema"
MKDOCS_PATH = ROOT / "mkdocs.yml"


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def read_schema(schema_file: Path) -> dict:
    with open(schema_file, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def run_gen_doc(schema_file: Path, out_dir: Path) -> None:
    """Generate Markdown documentation from the LinkML schema."""
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "gen-doc",
        str(schema_file),
        "-d",
        str(out_dir),
        "--truncate-descriptions",
        "false",
    ]
    print("  $", " ".join(cmd))
    subprocess.run(cmd, check=True)


def title_from_md(md_path: Path, fallback: str) -> str:
    """Pull the first level-1 heading from a Markdown file for a nice nav label."""
    try:
        for line in md_path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^#\s+(.*?)\s*$", line)
            if m:
                # e.g. "Class: VTADataset" -> "VTADataset",
                #      "Enum: ArenaShapeEnum" -> "ArenaShapeEnum"
                label = m.group(1)
                for prefix in ("Class:", "Enum:", "Slot:", "Type:", "Subset:"):
                    label = label.replace(prefix, "")
                return label.strip()
    except FileNotFoundError:
        pass
    return fallback


def split_generated(schema: dict, raw_dir: Path) -> tuple[list[str], list[str]]:
    """
    Keep every generated page together in docs/schema/ (so gen-doc's relative
    links resolve), but classify them into class pages vs. reference pages
    (enums / types / slots) purely for building the navigation menu.

    Returns (class_files, ref_files) — file names, not full paths.
    """
    class_names = list((schema.get("classes") or {}).keys())

    if GEN_DIR.exists():
        shutil.rmtree(GEN_DIR)
    shutil.move(str(raw_dir), str(GEN_DIR))

    class_files: list[str] = []
    ref_files: list[str] = []

    for md in sorted(GEN_DIR.glob("*.md")):
        name = md.stem
        if name == "index":
            # gen-doc's schema landing page becomes the reference overview.
            continue
        if name in class_names:
            class_files.append(md.name)
        else:
            ref_files.append(md.name)

    # Order class pages the way they appear in the schema, tree_root first.
    def class_sort_key(fname: str):
        cname = fname[:-3]
        cls = (schema.get("classes") or {}).get(cname, {})
        is_root = bool(cls.get("tree_root"))
        return (0 if is_root else 1,
                class_names.index(cname) if cname in class_names else 999)

    class_files.sort(key=class_sort_key)
    ref_files.sort()
    return class_files, ref_files


def build_class_nav(class_files: list[str]) -> list:
    nav = []
    for fname in class_files:
        label = title_from_md(GEN_DIR / fname, fname[:-3])
        nav.append({label: f"schema/{fname}"})
    return nav


def build_reference_nav(ref_files: list[str]) -> list:
    """Group reference pages into Enums / Types / Slots for a tidy menu."""
    enums, types, slots = [], [], []
    for fname in ref_files:
        label = title_from_md(GEN_DIR / fname, fname[:-3])
        entry = {label: f"schema/{fname}"}
        if fname.lower().endswith("enum.md"):
            enums.append(entry)
        elif fname[:-3] in TYPE_HINTS:
            types.append(entry)
        else:
            slots.append(entry)
    # gen-doc's index.md is a good schema-wide overview page.
    section: list = [{"Overview": "schema/index.md"}]
    if enums:
        section.append({"Enumerations": enums})
    if slots:
        section.append({"Slots": slots})
    if types:
        section.append({"Types": types})
    return section


# Built-in LinkML types that gen-doc always emits; used to bucket them as "Types".
TYPE_HINTS = {
    "Boolean", "Curie", "Date", "DateOrDatetime", "Datetime", "Decimal",
    "Double", "Duration", "Float", "Integer", "Jsonpath", "Jsonpointer",
    "Ncname", "Nodeidentifier", "Objectidentifier", "Sparqlpath", "String",
    "Time", "Uri", "Uriorcurie",
}


def theme_block(cfg: dict) -> dict:
    palette = []
    primary = cfg.get("theme_primary_color", "indigo")
    accent = cfg.get("theme_accent_color", "indigo")
    if cfg.get("enable_dark_mode_toggle", True):
        palette = [
            {
                "media": "(prefers-color-scheme: light)",
                "scheme": "default",
                "primary": primary,
                "accent": accent,
                "toggle": {
                    "icon": "material/weather-night",
                    "name": "Switch to dark mode",
                },
            },
            {
                "media": "(prefers-color-scheme: dark)",
                "scheme": "slate",
                "primary": primary,
                "accent": accent,
                "toggle": {
                    "icon": "material/weather-sunny",
                    "name": "Switch to light mode",
                },
            },
        ]
    else:
        palette = [{"scheme": "default", "primary": primary, "accent": accent}]

    theme = {
        "name": "material",
        "custom_dir": "docs/overrides",
        "palette": palette,
        "features": [
            "navigation.instant",
            "navigation.tracking",
            "navigation.sections",
            "navigation.top",
            "navigation.indexes",
            "toc.follow",
            "search.suggest",
            "search.highlight",
            "content.code.copy",
        ],
        "icon": {"repo": "fontawesome/brands/github"},
    }

    logo = (cfg.get("logo") or "").strip()
    favicon = (cfg.get("favicon") or "").strip()
    if logo:
        theme["logo"] = logo
    else:
        theme.setdefault("icon", {})["logo"] = cfg.get("logo_icon", "material/database")
    if favicon:
        theme["favicon"] = favicon
    elif logo:
        theme["favicon"] = logo

    fonts = {}
    if cfg.get("font_text"):
        fonts["text"] = cfg["font_text"]
    if cfg.get("font_code"):
        fonts["code"] = cfg["font_code"]
    if fonts:
        theme["font"] = fonts

    return theme


def build_mkdocs(cfg: dict, schema: dict, class_files: list[str], ref_files: list[str]) -> dict:
    intro_label = cfg.get("intro_nav_label", "Introduction")
    schema_label = cfg.get("schema_nav_label", "Overview on the Schema")

    ref_label = cfg.get("reference_nav_label", "Enums & Types")

    nav = [
        {intro_label: "index.md"},
        {schema_label: build_class_nav(class_files)},
    ]
    # Reference section (enums, slots, types) — shown unless disabled.
    if ref_files and cfg.get("show_reference_section", True):
        nav.append({ref_label: build_reference_nav(ref_files)})

    mkdocs = {
        "site_name": cfg.get("site_name", "Schema Documentation"),
        "site_description": cfg.get("site_description", ""),
        "site_author": cfg.get("site_author", ""),
        "site_url": cfg.get("site_url", ""),
        "repo_url": cfg.get("repo_url", ""),
        "repo_name": cfg.get("repo_name", ""),
        "copyright": cfg.get("copyright", ""),
        "docs_dir": "docs",
        "nav": nav,
        "theme": theme_block(cfg),
        "extra": {},
        "markdown_extensions": [
            "admonition",
            "attr_list",
            "md_in_html",
            "tables",
            "footnotes",
            "toc",
            {"pymdownx.highlight": {"anchor_linenums": True}},
            "pymdownx.inlinehilite",
            "pymdownx.snippets",
            "pymdownx.details",
            {
                "pymdownx.superfences": {
                    "custom_fences": [
                        {
                            "name": "mermaid",
                            "class": "mermaid",
                            "format": "!!python/name:pymdownx.superfences.fence_code_format",
                        }
                    ]
                }
            },
            {"pymdownx.tabbed": {"alternate_style": True}},
        ],
        "plugins": ["search"],
        "extra_css": ["assets/extra.css"],
    }

    # Social links in footer
    social = cfg.get("social_links") or []
    if social:
        mkdocs["extra"]["social"] = social

    # Analytics
    ga = (cfg.get("google_analytics") or "").strip()
    if ga:
        mkdocs["extra"]["analytics"] = {"provider": "google", "property": ga}

    if not mkdocs["extra"]:
        del mkdocs["extra"]

    # Drop empty top-level keys to keep the file clean
    return {k: v for k, v in mkdocs.items() if v not in ("", None)}


# The mermaid fence needs the literal YAML tag
#   !!python/name:pymdownx.superfences.fence_code_format
# which PyYAML's safe dumper will not emit cleanly. We therefore dump the rest
# of the document with PyYAML and substitute this one value via a placeholder.
_FENCE_PLACEHOLDER = "__MERMAID_FENCE_FORMAT__"
_FENCE_TAG = "!!python/name:pymdownx.superfences.fence_code_format"


def dump_mkdocs(mkdocs: dict) -> None:
    # Replace the format value with a placeholder string before dumping.
    for ext in mkdocs.get("markdown_extensions", []):
        if isinstance(ext, dict) and "pymdownx.superfences" in ext:
            for f in ext["pymdownx.superfences"]["custom_fences"]:
                if isinstance(f.get("format"), str) and f["format"].startswith("!!python/name:"):
                    f["format"] = _FENCE_PLACEHOLDER

    body = yaml.dump(
        mkdocs, sort_keys=False, default_flow_style=False, allow_unicode=True
    )
    # Swap the quoted placeholder for the real (unquoted) YAML tag.
    body = body.replace(f"'{_FENCE_PLACEHOLDER}'", _FENCE_TAG)
    body = body.replace(_FENCE_PLACEHOLDER, _FENCE_TAG)

    with open(MKDOCS_PATH, "w", encoding="utf-8") as fh:
        fh.write("# ==========================================================\n")
        fh.write("#  AUTO-GENERATED by scripts/build_site.py\n")
        fh.write("#  Do not edit by hand — change site.config.yml instead.\n")
        fh.write("# ==========================================================\n\n")
        fh.write(body)


def main() -> int:
    print("==> Loading site.config.yml")
    cfg = load_config()

    schema_file = (ROOT / cfg["schema_file"]).resolve()
    if not schema_file.exists():
        print(f"ERROR: schema file not found: {schema_file}", file=sys.stderr)
        return 1
    schema = read_schema(schema_file)

    print("==> Generating Markdown docs with LinkML gen-doc")
    raw_dir = DOCS_DIR / "_generated"
    run_gen_doc(schema_file, raw_dir)

    print("==> Organising pages into Classes / Reference")
    class_files, ref_files = split_generated(schema, raw_dir)
    print(f"    {len(class_files)} classes, {len(ref_files)} reference pages")

    print("==> Writing mkdocs.yml")
    mkdocs = build_mkdocs(cfg, schema, class_files, ref_files)
    dump_mkdocs(mkdocs)

    print("==> Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
