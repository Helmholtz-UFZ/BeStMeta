#!/usr/bin/env python3
"""
Reads the BeStMeta LinkML schema and generates a color-coded ER-style SVG diagram,
marking each slot as required / recommended / optional / conditional.

The schema is nested: the root class (VTADataset) references child classes via
inlined slots, and those children may in turn reference further sub-classes
(e.g. ExperimentalConditions -> Subject / Experiment / Manipulation). This script
walks that reference graph recursively and lays the classes out level by level,
so every nesting depth is shown and connected to its parent.
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
sv = SchemaView(SCHEMA_PATH) # loads schema and creates a SchemaView for querying it
ALL_CLASSES = set(sv.all_classes().keys()) # creates set of class names

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

# Names of the child classes referenced (via inlined slots) by a given class,
# in schema order, excluding the class itself to avoid trivial self-loops.
def child_classes_of(class_name):
    children = []
    for slot in sv.class_induced_slots(class_name):
        if slot.range in ALL_CLASSES and slot.range != class_name:
            children.append(slot.range)
    return children

# ---------------------------------------------------------------------------
# Build the class hierarchy by walking references recursively.
# Each node: {"name", "rows", "children": [...], "depth"}. A class is only
# expanded once (first occurrence wins) so a shared/reused class can't create
# an infinite loop.
# ---------------------------------------------------------------------------
def build_tree(class_name, depth, seen):
    node = {
        "name": class_name,
        "rows": class_rows(class_name),
        "depth": depth,
        "children": [],
    }
    if class_name in seen:
        return node
    seen.add(class_name)
    for child in child_classes_of(class_name):
        node["children"].append(build_tree(child, depth + 1, seen))
    return node

ROOT_NODE = build_tree(ROOT_CLASS, 0, set())

# Flatten the tree into levels (depth -> list of nodes, left-to-right order).
def collect_levels(node, levels):
    levels.setdefault(node["depth"], []).append(node)
    for child in node["children"]:
        collect_levels(child, levels)

LEVELS = {}
collect_levels(ROOT_NODE, LEVELS)
MAX_DEPTH = max(LEVELS.keys())

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

def connector(cx1, cy1, cx2, cy2):
    """Smooth vertical S-curve from a parent's bottom to a child's top, plus a dot."""
    mid_y = (cy1 + cy2) / 2
    return (f'<path d="M {cx1} {cy1} C {cx1} {mid_y}, {cx2} {mid_y}, {cx2} {cy2}" '
            f'fill="none" stroke="{COL_BORDER}" stroke-width="1.4"/>'
            f'<circle cx="{cx2}" cy="{cy2}" r="3" fill="{COL_HEADER_BG}"/>')

def build():
    # ---- aggregate per-class and total counts ------------------------------
    per_class_counts = {}
    total = {"req": 0, "rec": 0, "opt": 0}
    for depth_nodes in LEVELS.values():
        for node in depth_nodes:
            c = count_status(node["rows"])
            per_class_counts[node["name"]] = c
            for k in total:
                total[k] += c[k]

    # ---- geometry: lay out each level as a centered horizontal row ---------
    # A node's width: root uses ROOT_W, everything else BOX_W.
    def node_w(node):
        return ROOT_W if node["depth"] == 0 else BOX_W

    # Total row width for a level (boxes + gaps between them).
    def level_width(nodes):
        return sum(node_w(n) for n in nodes) + GAP_X * (len(nodes) - 1)

    widest = max(level_width(nodes) for nodes in LEVELS.values())
    total_w = MARGIN * 2 + widest

    # Assign x/y to every node, level by level. Each level is centered.
    # y of a level = previous level y + tallest box on previous level
    #                + room for the counts line + LEVEL_GAP_Y.
    header_offset = MARGIN + 78          # space for title/legend/totals at top
    positions = {}                        # node name -> (x, y, w, h)
    level_top = header_offset
    for depth in range(MAX_DEPTH + 1):
        nodes = LEVELS[depth]
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
    draw_edges(ROOT_NODE)

    # ---- draw the boxes ----------------------------------------------------
    for depth in range(MAX_DEPTH + 1):
        for node in LEVELS[depth]:
            x, y, w, h = positions[node["name"]]
            box_svg, _ = render_class_box(x, y, node["name"], node["rows"],
                                          width=w, counts=per_class_counts[node["name"]])
            parts.append(box_svg)

    parts.append('</svg>')
    return "\n".join(parts)

if __name__ == "__main__":
    svg = build()
    out_path = "diagrams/bestmeta_diagram.svg"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("written:", out_path)
    print("length:", len(svg))