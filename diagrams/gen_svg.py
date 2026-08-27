#!/usr/bin/env python3
"""
Reads the BeStMeta LinkML schema and generates a color-coded ER-style SVG diagram,
marking each slot as required / recommended / optional / conditional.
"""

from linkml_runtime import SchemaView
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = str(SCRIPT_DIR.parent / "bestmeta_schema.yaml")
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
# load schema and derive slots
# ---------------------------------------------------------------------------
sv = SchemaView(SCHEMA_PATH)

# derive requirement level
def slot_status(slot):
    base = "opt"
    if getattr(slot, "required", False):
        base = "req"
    elif getattr(slot, "recommended", False):
        base = "rec"
    if slot.name in CONDITIONAL_SLOTS:
        return base + "*" 
    return base

# return slot range
def slot_range(slot):
    return slot.range if slot.range else "string"

# Return a list of (name, range, status) tuples for all slots of a class, in schema order.
def class_rows(class_name):
    rows = []
    for slot in sv.class_induced_slots(class_name):
        rows.append((slot.name, slot_range(slot), slot_status(slot)))
    return rows

# root class
VTADataset = class_rows(ROOT_CLASS)

# automatically find child classes: all ranges of the root that are themselves classes
all_classes = set(sv.all_classes().keys())
CLASSES = []
for slot in sv.class_induced_slots(ROOT_CLASS):
    if slot.range in all_classes and slot.range != ROOT_CLASS:
        CLASSES.append((slot.range, class_rows(slot.range)))

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

# counts requirement levels of slots
def count_status(rows):
    """Count req / rec / opt slots in a class (conditional '*' counts by its base status)."""
    counts = {"req": 0, "rec": 0, "opt": 0}
    for _, _, status in rows:
        base = status.rstrip("*")   # "opt*" → "opt", "rec*" → "rec"
        if base in counts:
            counts[base] += 1
    return counts

def build():
    all_boxes = [(ROOT_CLASS, VTADataset)] + CLASSES
    total = {"req": 0, "rec": 0, "opt": 0}
    per_class_counts = {}
    for name, rows in all_boxes:
        c = count_status(rows)
        per_class_counts[name] = c
        for k in total:
            total[k] += c[k]
    col_heights = [box_height(len(rows)) for _, rows in CLASSES]
    n = len(CLASSES)
    total_w = MARGIN * 2 + n * BOX_W + (n - 1) * GAP_X
    max_col_h = max(col_heights) if col_heights else 0

    root_h = box_height(len(VTADataset))
    root_x = (total_w - ROOT_W) / 2
    root_y = MARGIN + 78
    children_y = root_y + root_h + ROOT_GAP_Y
    total_h = children_y + max_col_h + MARGIN

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
    root_svg,root_h = render_class_box(root_x, root_y, ROOT_CLASS, VTADataset,
                                        width=ROOT_W, counts=per_class_counts[ROOT_CLASS])
    parts.append(root_svg)

    x = MARGIN
    for (title, rows), h in zip(CLASSES, col_heights):
        cx1 = root_x + ROOT_W / 2
        cy1 = root_y + root_h
        cx2 = x + BOX_W / 2
        cy2 = children_y
        mid_y = (cy1 + cy2) / 2
        parts.append(f'<path d="M {cx1} {cy1} C {cx1} {mid_y}, {cx2} {mid_y}, {cx2} {cy2}" '
                     f'fill="none" stroke="{COL_BORDER}" stroke-width="1.4"/>')
        parts.append(f'<circle cx="{cx2}" cy="{cy2}" r="3" fill="{COL_HEADER_BG}"/>')
        box_svg, _ = render_class_box(x, children_y, title, rows,
                                      counts=per_class_counts[title])
        parts.append(box_svg)
        x += BOX_W + GAP_X

    parts.append('</svg>')
    return "\n".join(parts)

if __name__ == "__main__":
    svg = build()
    out_path = "diagrams/bestmeta_diagram.svg"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("written:", out_path)
    print("length:", len(svg))