#!/usr/bin/env python3
"""
Reads the BeStMeta LinkML schema and generates a color-coded ER-style SVG diagram,
marking each slot as required / recommended / optional / conditional.

The schema is nested: the root class (VTADataset) references child classes via
inlined slots, and those children may in turn reference further sub-classes
(e.g. ExperimentalConditions -> Subject / Experiment / Manipulation). This script
walks that reference graph recursively and lays the classes out level by level,
so every nesting depth is shown and connected to its parent.

Path resolution
----------------
By default, paths are resolved relative to this script's own location on disk
(via Path(__file__).resolve().parent), NOT the current working directory. That
means it works correctly no matter where you `cd` to before running it, and no
matter whose machine / checkout it lives in.

  project_root/
    bestmeta_schema.yaml   <- default schema location (one level above script)
    diagrams/              <- default output location
    scripts/
      generate_bestmeta_diagram.py   <- this file

If your layout differs, override any of these on the command line:

    python generate_bestmeta_diagram.py --root /path/to/project
    python generate_bestmeta_diagram.py --schema /path/to/bestmeta_schema.yaml
    python generate_bestmeta_diagram.py --outdir /path/to/output/folder
"""

import argparse
from pathlib import Path

from linkml_runtime import SchemaView


ROOT_CLASS = "VTADataset"

# Slots that are conditionally required via rules/any_of → get the "*" status.
# This info isn't captured in a single slot flag, so maintain it manually here.
CONDITIONAL_SLOTS = {
    "developmental_stage", "developmental_stage_value", "developmental_stage_unit",
    "age_value", "age_unit",
    "field_of_view_width", "field_of_view_height", "field_of_view_unit",
    "bit_depth",
}

# ---------------------------------------------------------------------------
# Style tokens
# ---------------------------------------------------------------------------
COL_BG = "#ffffff"
COL_PAGE_BG = "#f7f8fa"
COL_HEADER_BG = "#1f2a44"
COL_HEADER_TEXT = "#ffffff"
COL_BORDER = "#c7cdd6"
COL_ROW_ALT = "#f1f3f6"
COL_TYPE_TEXT = "#7a8390"

COL_REQ = "#c0392b"
COL_REC = "#c8790a"
COL_OPT = "#5b6472"
COL_COND = "#8e5bc0"

FONT_FAMILY = "'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
MONO_FAMILY = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"

ROW_H = 18
HEADER_H = 34
PAD_TOP = 8
PAD_BOTTOM = 10
BOX_W = 310
GAP_X = 34
MARGIN = 40
ROOT_W = 340
ROOT_GAP_Y = 70
LEVEL_GAP_Y = 70          # vertical gap between hierarchy levels
COUNTS_SPACE = 20         # room under a box for its "req/rec/opt" summary line


# ---------------------------------------------------------------------------
# CLI / path resolution
# ---------------------------------------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a color-coded ER-style SVG diagram from the BeStMeta LinkML schema."
    )
    parser.add_argument(
        "--root", type=Path, default=None,
        help="Project root directory (expected to contain bestmeta_schema.yaml and a "
             "diagrams/ folder). Defaults to the parent directory of this script."
    )
    parser.add_argument(
        "--schema", type=Path, default=None,
        help="Explicit path to the schema YAML file. Overrides --root for this purpose."
    )
    parser.add_argument(
        "--outdir", type=Path, default=None,
        help="Directory to write the output SVG into. Overrides --root for this purpose."
    )
    parser.add_argument(
        "--outfile", type=str, default="bestmeta_diagram.svg",
        help="Output SVG filename (default: bestmeta_diagram.svg)."
    )
    return parser.parse_args()


def resolve_paths(args):
    """Figure out schema_path and out_dir from CLI args, always anchored to
    this script's own location on disk (not the caller's cwd) unless the
    person explicitly overrides them."""
    script_dir = Path(__file__).resolve().parent
    root = args.root.resolve() if args.root else script_dir.parent

    schema_path = args.schema.resolve() if args.schema else (root / "bestmeta_schema.yaml").resolve()
    out_dir = args.outdir.resolve() if args.outdir else (root / "diagrams").resolve()

    return schema_path, out_dir


# ---------------------------------------------------------------------------
# Schema-derived helpers (all take `sv` / `all_classes` explicitly now,
# rather than relying on module-level globals, so they're safe to call
# after paths are resolved at runtime)
# ---------------------------------------------------------------------------
def slot_status(slot):
    base = "opt"
    if getattr(slot, "required", False):
        base = "req"
    elif getattr(slot, "recommended", False):
        base = "rec"
    if slot.name in CONDITIONAL_SLOTS:
        return base + "*"
    return base


def slot_range(slot):
    return slot.range if slot.range else "string"


def class_rows(sv, class_name):
    rows = []
    for slot in sv.class_induced_slots(class_name):
        rows.append((slot.name, slot_range(slot), slot_status(slot)))
    return rows


def child_classes_of(sv, all_classes, class_name):
    children = []
    for slot in sv.class_induced_slots(class_name):
        if slot.range in all_classes and slot.range != class_name:
            children.append(slot.range)
    return children


def build_tree(sv, all_classes, class_name, depth, seen):
    node = {
        "name": class_name,
        "rows": class_rows(sv, class_name),
        "depth": depth,
        "children": [],
    }
    if class_name in seen:
        return node
    seen.add(class_name)
    for child in child_classes_of(sv, all_classes, class_name):
        node["children"].append(build_tree(sv, all_classes, child, depth + 1, seen))
    return node


def collect_levels(node, levels):
    levels.setdefault(node["depth"], []).append(node)
    for child in node["children"]:
        collect_levels(child, levels)


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------
def status_color(status):
    if status.endswith("*"):
        return COL_COND
    if status.startswith("req"):
        return COL_REQ
    if status.startswith("rec"):
        return COL_REC
    return COL_OPT


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def box_height(n_rows):
    return HEADER_H + PAD_TOP + n_rows * ROW_H + PAD_BOTTOM


def render_class_box(x, y, title, rows, width=BOX_W, counts=None):
    h = box_height(len(rows))
    svg = ['<g>']
    svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{h}" rx="8" ry="8" '
               f'fill="{COL_BG}" stroke="{COL_BORDER}" stroke-width="1.2"/>')
    svg.append(f'<path d="M {x} {y+8} Q {x} {y} {x+8} {y} '
               f'L {x+width-8} {y} Q {x+width} {y} {x+width} {y+8} '
               f'L {x+width} {y+HEADER_H} L {x} {y+HEADER_H} Z" fill="{COL_HEADER_BG}"/>')
    svg.append(f'<text x="{x+width/2}" y="{y+HEADER_H/2+5}" text-anchor="middle" '
               f'font-family="{FONT_FAMILY}" font-size="13.5" font-weight="700" '
               f'fill="{COL_HEADER_TEXT}">{esc(title)}</text>')
    ry = y + HEADER_H + PAD_TOP
    for i, (name, rtype, status) in enumerate(rows):
        row_y = ry + i * ROW_H
        if i % 2 == 1:
            svg.append(f'<rect x="{x+1}" y="{row_y}" width="{width-2}" height="{ROW_H}" fill="{COL_ROW_ALT}"/>')
        color = status_color(status)
        svg.append(f'<circle cx="{x+14}" cy="{row_y+ROW_H/2}" r="3.4" fill="{color}"/>')
        svg.append(f'<text x="{x+24}" y="{row_y+ROW_H/2+4}" font-family="{MONO_FAMILY}" '
                   f'font-size="10.3" fill="{color}">{esc(name)}</text>')
        svg.append(f'<text x="{x+width-10}" y="{row_y+ROW_H/2+4}" text-anchor="end" '
                   f'font-family="{FONT_FAMILY}" font-size="9.3" font-style="italic" '
                   f'fill="{COL_TYPE_TEXT}">{esc(rtype)}</text>')
    svg.append('</g>')
    if counts:
        cy = y + h + 13
        summary = f"req {counts['req']}  ·  rec {counts['rec']}  ·  opt {counts['opt']}"
        svg.append(f'<text x="{x+width/2}" y="{cy}" text-anchor="middle" '
                   f'font-family="{FONT_FAMILY}" font-size="10" fill="{COL_TYPE_TEXT}">'
                   f'{esc(summary)}</text>')
    return "\n".join(svg), h


def render_legend(x, y):
    items = [
        (COL_REQ, "required"),
        (COL_REC, "recommended"),
        (COL_COND, "conditionally required (see rule/any_of)"),
        (COL_OPT, "optional"),
    ]
    svg = [f'<g font-family="{FONT_FAMILY}" font-size="11.5">']
    cx = x
    for color, label in items:
        svg.append(f'<circle cx="{cx}" cy="{y}" r="5" fill="{color}"/>')
        svg.append(f'<text x="{cx+11}" y="{y+4}" fill="#2a2f3a">{esc(label)}</text>')
        cx += 16 + len(label) * 6.4 + 26
    svg.append('</g>')
    return "\n".join(svg)


def count_status(rows):
    """Count req / rec / opt slots in a class (conditional '*' counts by its base status)."""
    counts = {"req": 0, "rec": 0, "opt": 0}
    for _, _, status in rows:
        base = status.rstrip("*")   # "opt*" → "opt", "rec*" → "rec"
        if base in counts:
            counts[base] += 1
    return counts


def connector(cx1, cy1, cx2, cy2):
    """Smooth vertical S-curve from a parent's bottom to a child's top, plus a dot."""
    mid_y = (cy1 + cy2) / 2
    return (f'<path d="M {cx1} {cy1} C {cx1} {mid_y}, {cx2} {mid_y}, {cx2} {cy2}" '
            f'fill="none" stroke="{COL_BORDER}" stroke-width="1.4"/>'
            f'<circle cx="{cx2}" cy="{cy2}" r="3" fill="{COL_HEADER_BG}"/>')


def build(root_node, levels, max_depth):
    # ---- aggregate per-class and total counts ------------------------------
    per_class_counts = {}
    total = {"req": 0, "rec": 0, "opt": 0}
    for depth_nodes in levels.values():
        for node in depth_nodes:
            c = count_status(node["rows"])
            per_class_counts[node["name"]] = c
            for k in total:
                total[k] += c[k]

    # ---- geometry: lay out each level as a centered horizontal row ---------
    def node_w(node):
        return ROOT_W if node["depth"] == 0 else BOX_W

    def level_width(nodes):
        return sum(node_w(n) for n in nodes) + GAP_X * (len(nodes) - 1)

    widest = max(level_width(nodes) for nodes in levels.values())
    total_w = MARGIN * 2 + widest

    header_offset = MARGIN + 78          # space for title/legend/totals at top
    positions = {}                        # node name -> (x, y, w, h)
    level_top = header_offset
    for depth in range(max_depth + 1):
        nodes = levels[depth]
        row_w = level_width(nodes)
        x = MARGIN + (widest - row_w) / 2
        max_h = 0
        for node in nodes:
            w = node_w(node)
            h = box_height(len(node["rows"]))
            positions[node["name"]] = (x, level_top, w, h)
            max_h = max(max_h, h)
            x += w + GAP_X
        level_top += max_h + COUNTS_SPACE + LEVEL_GAP_Y

    total_h = level_top - LEVEL_GAP_Y + MARGIN

    # ---- start assembling the SVG ------------------------------------------
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" '
             f'width="{total_w}" height="{total_h}" font-family="{FONT_FAMILY}">']
    parts.append(f'<rect x="0" y="0" width="{total_w}" height="{total_h}" fill="{COL_PAGE_BG}"/>')
    parts.append(f'<text x="{total_w/2}" y="30" text-anchor="middle" font-size="19" '
                 f'font-weight="700" fill="#1f2a44">BeStMeta Metadata Schema \u2013 Slot Requirement Levels</text>')
    parts.append(render_legend(MARGIN, 52))
    total_line = (f"Total across all classes:   "
                  f"required {total['req']}   ·   "
                  f"recommended {total['rec']}   ·   "
                  f"optional {total['opt']}   ·   "
                  f"sum {total['req']+total['rec']+total['opt']}")
    parts.append(f'<text x="{MARGIN}" y="72" font-family="{FONT_FAMILY}" font-size="12.5" '
                 f'font-weight="600" fill="#1f2a44">{esc(total_line)}</text>')

    # ---- draw connectors first (so boxes sit on top of the lines) ----------
    def draw_edges(node):
        px, py, pw, ph = positions[node["name"]]
        cx1 = px + pw / 2
        cy1 = py + ph
        for child in node["children"]:
            cxx, cyy, cw, ch = positions[child["name"]]
            cx2 = cxx + cw / 2
            cy2 = cyy
            parts.append(connector(cx1, cy1, cx2, cy2))
            draw_edges(child)
    draw_edges(root_node)

    # ---- draw the boxes ----------------------------------------------------
    for depth in range(max_depth + 1):
        for node in levels[depth]:
            x, y, w, h = positions[node["name"]]
            box_svg, _ = render_class_box(x, y, node["name"], node["rows"],
                                          width=w, counts=per_class_counts[node["name"]])
            parts.append(box_svg)

    parts.append('</svg>')
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    args = parse_args()
    schema_path, out_dir = resolve_paths(args)

    if not schema_path.exists():
        raise FileNotFoundError(
            f"Schema not found at: {schema_path}\n"
            f"Pass --schema /path/to/bestmeta_schema.yaml or --root /path/to/project "
            f"to point at the correct location."
        )

    sv = SchemaView(str(schema_path))
    all_classes = set(sv.all_classes().keys())

    root_node = build_tree(sv, all_classes, ROOT_CLASS, 0, set())

    levels = {}
    collect_levels(root_node, levels)
    max_depth = max(levels.keys())

    svg = build(root_node, levels, max_depth)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / args.outfile
    out_path.write_text(svg, encoding="utf-8")

    print("schema read from:", schema_path)
    print("written:", out_path)
    print("length:", len(svg))


if __name__ == "__main__":
    main()
