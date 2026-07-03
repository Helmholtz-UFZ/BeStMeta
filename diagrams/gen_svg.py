#!/usr/bin/env python3

"""
Generates a color-coded ER-style SVG diagram for the BeStMeta metadata schema,
marking each slot as required / recommended / optional.
"""

# ---- Data: (slot_name, range_type, status) ----
# status: "req" | "rec" | "opt"

VTADataset = [
    ("dataset_id", "string", "req"),
    ("dataset_title", "string", "req"),
    ("dataset_description", "string", "rec"),
    ("dataset_version", "string", "opt"),
    ("dataset_license", "string", "req"),
    ("dataset_doi", "uri", "rec"),
    ("publication_doi", "uri", "rec"),
    ("dataset_created_date", "date", "opt"),
    ("dataset_creator_name", "string", "rec"),
    ("dataset_creator_orcid", "uri", "rec"),
    ("dataset_contact_email", "string", "rec"),
    ("research_domain", "DomainEnum", "rec"),
    ("raw_data_repository", "RepositoryEnum", "rec"),
    ("raw_data_repository_url", "uri", "rec"),
    ("raw_tracking_data_format", "RawDataFormatEnum", "rec"),
    ("raw_tracking_data_doi", "uri", "opt"),
    ("analysis_code_repository", "RepositoryEnum", "opt"),
    ("analysis_code_repository_url", "uri", "opt"),
    ("analysis_code_doi", "uri", "opt"),
    ("dataset_notes", "string", "opt"),
    ("experimental_conditions", "ExperimentalConditions", "opt"),
    ("video_hardware", "VideoHardware", "opt"),
    ("acquisition_parameters", "AcquisitionParameters", "opt"),
    ("tracking_analysis", "TrackingAnalysis", "opt"),
    ("statistical_analysis", "StatisticalAnalysis", "opt"),
]

ExperimentalConditions = [
    ("experiment_start_datetime", "datetime", "rec"),
    ("experiment_end_datetime", "datetime", "rec"),
    ("species_name", "string", "req"),
    ("species_ncbi_taxon_id", "string", "rec"),
    ("strain", "string", "rec"),
    ("genotype", "string", "rec"),
    ("sex", "SexEnum", "rec"),
    ("developmental_stage", "DevelopmentalStageEnum", "opt*"),
    ("developmental_stage_value", "float", "opt*"),
    ("developmental_stage_unit", "DevelopmentUnitEnum", "opt*"),
    ("age_value", "float", "opt*"),
    ("age_unit", "DevelopmentUnitEnum", "opt*"),
    ("body_length_value", "float", "rec"),
    ("body_length_unit", "LengthUnitEnum", "rec"),
    ("weight_value", "float", "opt"),
    ("weight_unit", "WeightUnitEnum", "opt"),
    ("n_individuals_total", "integer", "req"),
    ("n_individuals_per_arena", "integer", "req"),
    ("assay_type", "string", "req"),
    ("assay_description", "string", "opt"),
    ("arena_shape", "ArenaShapeEnum", "rec"),
    ("arena_type", "ArenaTypeEnum", "rec"),
    ("arena_length", "float", "rec"),
    ("arena_length_unit", "LengthUnitEnum", "rec"),
    ("arena_width", "float", "rec"),
    ("arena_width_unit", "LengthUnitEnum", "rec"),
    ("arena_height", "float", "rec"),
    ("arena_height_unit", "LengthUnitEnum", "rec"),
    ("plate_well_count", "integer", "rec"),
    ("well_shape_cross_section", "WellCrossSectionShapeEnum", "rec"),
    ("well_shape_bottom", "WellBottomShapeEnum", "opt"),
    ("habituation_duration_min", "float", "opt"),
    ("habituation_protocol", "string", "opt"),
    ("temperature_celsius", "float", "rec"),
    ("light_cycle_type", "LightCycleTypeEnum", "rec"),
    ("light_cycle_detail", "string", "rec"),
    ("housing_conditions", "string", "opt"),
    ("treatment_name", "string", "rec"),
    ("treatment_description", "string", "rec"),
    ("exposure_compound_name", "string", "rec"),
    ("exposure_compound_chebi_id", "string", "rec"),
    ("exposure_concentration", "float", "rec"),
    ("exposure_concentration_unit", "ConcentrationUnitEnum", "rec"),
    ("exposure_route", "ExposureRouteEnum", "opt"),
    ("exposure_duration_h", "float", "opt"),
    ("solvent_vehicle", "string", "opt"),
    ("control_type", "ControlTypeEnum", "opt"),
    ("experiment_notes", "string", "opt"),
]

VideoHardware = [
    ("camera_count", "integer", "req"),
    ("camera_device_type", "CameraDeviceTypeEnum", "req"),
    ("camera_model", "string", "req"),
    ("camera_manufacturer", "string", "req"),
    ("camera_sensor_type", "CameraSensorTypeEnum", "rec"),
    ("camera_interface", "CameraInterfaceEnum", "opt"),
    ("camera_distance_mm", "float", "rec"),
    ("camera_position", "CameraPositionEnum", "rec"),
    ("microscope_manufacturer", "string", "opt"),
    ("microscope_model", "string", "opt"),
    ("microscope_type", "MicroscopeTypeEnum", "opt"),
    ("microscope_serial_number", "string", "opt"),
    ("microscope_lot_number", "string", "opt"),
    ("lens_focal_length_mm", "float", "rec"),
    ("objective_magnification", "float", "rec"),
    ("contrast_polarity", "ContrastPolarityEnum", "rec"),
    ("field_of_view_width", "float", "rec*"),
    ("field_of_view_height", "float", "rec*"),
    ("field_of_view_unit", "LengthUnitEnum", "opt*"),
    ("closed_box_system_name", "ClosedBoxSystemEnum", "opt"),
    ("closed_box_system_version", "string", "opt"),
    ("hardware_notes", "string", "opt"),
]

AcquisitionParameters = [
    ("recording_start_datetime", "datetime", "rec"),
    ("recording_end_datetime", "datetime", "rec"),
    ("recording_duration", "duration", "req"),
    ("recording_software_name", "string", "req"),
    ("recording_software_version", "string", "req"),
    ("illumination_type", "IlluminationTypeEnum", "rec"),
    ("illumination_wavelength", "float", "opt"),
    ("illumination_illuminance", "float", "opt"),
    ("frame_rate", "float", "req"),
    ("total_frame_count", "integer", "opt"),
    ("video_resolution_width", "integer", "req"),
    ("video_resolution_height", "integer", "req"),
    ("bit_depth", "integer", "opt*"),
    ("color_mode", "ColorModeEnum", "opt"),
    ("spatial_resolution", "float", "rec"),
    ("video_container_format", "VideoContainerEnum", "req"),
    ("video_codec", "VideoCodecEnum", "rec"),
    ("gain", "string", "opt"),
    ("exposure_time", "float", "rec"),
    ("noise_reduction_method", "string", "rec"),
    ("acquisition_notes", "string", "opt"),
]

TrackingAnalysis = [
    ("tracking_software_type", "TrackingSoftwareTypeEnum", "rec"),
    ("tracking_software_name", "string", "rec"),
    ("tracking_software_version", "string", "rec"),
    ("tracking_algorithm", "string", "rec"),
    ("tracking_software_settings", "string", "rec"),
    ("tracking_data_format", "string", "rec"),
    ("tracking_confidence_threshold", "float", "rec"),
    ("tracking_manual_correction", "boolean", "rec"),
    ("compute_hardware", "string", "rec"),
    ("preprocessing_steps", "PreprocessingStepEnum", "rec"),
    ("n_individuals_tracked_per_arena", "integer", "rec"),
    ("n_bodyparts_tracked", "integer", "rec"),
    ("dropped_frames_count", "integer", "rec"),
    ("dropped_frames_reason", "string", "opt"),
    ("frames_without_tracked_individual", "integer", "rec"),
    ("frames_without_tracked_bodypart", "integer", "rec"),
    ("behavioral_endpoints", "string", "rec"),
    ("endpoint_definitions", "string", "rec"),
    ("tracking_notes", "string", "opt"),
]

StatisticalAnalysis = [
    ("statistical_software_name", "string", "rec"),
    ("statistical_software_version", "string", "rec"),
    ("statistical_tests", "string", "rec"),
    ("statistical_models", "string", "rec"),
    ("multiple_testing_correction", "string", "rec"),
    ("significance_level", "float", "rec"),
    ("effect_size_measure", "string", "rec"),
    ("confidence_interval_level", "string", "rec"),
    ("sample_size_analysis", "string", "rec"),
    ("statistics_notes", "string", "opt"),
]

CLASSES = [
    ("ExperimentalConditions", ExperimentalConditions),
    ("VideoHardware", VideoHardware),
    ("AcquisitionParameters", AcquisitionParameters),
    ("TrackingAnalysis", TrackingAnalysis),
    ("StatisticalAnalysis", StatisticalAnalysis),
]

# ---- Style tokens ----
COL_BG = "#ffffff"
COL_PAGE_BG = "#f7f8fa"
COL_HEADER_BG = "#1f2a44"      # deep indigo-slate
COL_HEADER_TEXT = "#ffffff"
COL_BORDER = "#c7cdd6"
COL_ROW_ALT = "#f1f3f6"
COL_TYPE_TEXT = "#7a8390"

COL_REQ = "#c0392b"   # required - red
COL_REC = "#c8790a"   # recommended - amber/orange
COL_OPT = "#5b6472"   # optional - slate gray
COL_COND = "#8e5bc0"  # conditionally required (marked with *) - purple

FONT_FAMILY = "'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
MONO_FAMILY = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"

ROW_H = 18
HEADER_H = 34
PAD_TOP = 8
PAD_BOTTOM = 10
BOX_W = 250
GAP_X = 34
MARGIN = 40
ROOT_W = 300
ROOT_GAP_Y = 70

def status_color(status):
    # conditional statuses (marked with a trailing "*") must be checked FIRST,
    # otherwise "rec*"/"opt*" would incorrectly match the "rec"/"opt" prefixes below
    if status.endswith("*"):
        return COL_COND
    if status.startswith("req"):
        return COL_REQ
    if status.startswith("rec"):
        return COL_REC
    if status == "opt":
        return COL_OPT
    return COL_OPT

def status_label(status):
    if status == "req":
        return "required"
    if status == "rec":
        return "recommended"
    if status == "opt":
        return "optional"
    if status == "rec*":
        return "recommended (conditional)"
    if status == "opt*":
        return "optional (conditionally required)"
    return status

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def box_height(n_rows):
    return HEADER_H + PAD_TOP + n_rows * ROW_H + PAD_BOTTOM

def render_class_box(x, y, title, rows, width=BOX_W):
    h = box_height(len(rows))
    svg = []
    # container
    svg.append(f'<g>')
    svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{h}" rx="8" ry="8" '
                f'fill="{COL_BG}" stroke="{COL_BORDER}" stroke-width="1.2"/>')
    # header
    svg.append(f'<path d="M {x} {y+8} '
                f'Q {x} {y} {x+8} {y} '
                f'L {x+width-8} {y} '
                f'Q {x+width} {y} {x+width} {y+8} '
                f'L {x+width} {y+HEADER_H} L {x} {y+HEADER_H} Z" '
                f'fill="{COL_HEADER_BG}"/>')
    svg.append(f'<text x="{x+width/2}" y="{y+HEADER_H/2+5}" text-anchor="middle" '
                f'font-family="{FONT_FAMILY}" font-size="13.5" font-weight="700" '
                f'fill="{COL_HEADER_TEXT}">{esc(title)}</text>')
    # rows
    ry = y + HEADER_H + PAD_TOP
    for i, (name, rtype, status) in enumerate(rows):
        row_y = ry + i * ROW_H
        if i % 2 == 1:
            svg.append(f'<rect x="{x+1}" y="{row_y}" width="{width-2}" height="{ROW_H}" fill="{COL_ROW_ALT}"/>')
        color = status_color(status)
        # status dot
        svg.append(f'<circle cx="{x+14}" cy="{row_y+ROW_H/2}" r="3.4" fill="{color}"/>')
        # slot name
        svg.append(f'<text x="{x+24}" y="{row_y+ROW_H/2+4}" font-family="{MONO_FAMILY}" '
                    f'font-size="10.3" fill="{color}">{esc(name)}</text>')
        # type, right-aligned
        svg.append(f'<text x="{x+width-10}" y="{row_y+ROW_H/2+4}" text-anchor="end" '
                    f'font-family="{FONT_FAMILY}" font-size="9.3" font-style="italic" '
                    f'fill="{COL_TYPE_TEXT}">{esc(rtype)}</text>')
    svg.append('</g>')
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


def build():
    # compute column heights
    col_heights = [box_height(len(rows)) for _, rows in CLASSES]
    n = len(CLASSES)
    total_w = MARGIN * 2 + n * BOX_W + (n - 1) * GAP_X
    max_col_h = max(col_heights)

    root_h = box_height(len(VTADataset))
    root_x = (total_w - ROOT_W) / 2
    root_y = MARGIN + 60  # room for title + legend

    children_y = root_y + root_h + ROOT_GAP_Y
    total_h = children_y + max_col_h + MARGIN

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" '
                 f'width="{total_w}" height="{total_h}" font-family="{FONT_FAMILY}">')
    parts.append(f'<rect x="0" y="0" width="{total_w}" height="{total_h}" fill="{COL_PAGE_BG}"/>')

    # Title
    parts.append(f'<text x="{total_w/2}" y="30" text-anchor="middle" font-size="19" '
                 f'font-weight="700" fill="#1f2a44">BeStMeta Metadata Schema \u2013 Slot Requirement Levels</text>')

    # Legend
    legend_svg = render_legend(MARGIN, 52)
    parts.append(legend_svg)

    # Root box
    root_svg, _ = render_class_box(root_x, root_y, "VTADataset", VTADataset, width=ROOT_W)
    parts.append(root_svg)

    # Children boxes + connectors
    x = MARGIN
    for (title, rows), h in zip(CLASSES, col_heights):
        # connector line from bottom-center of root to top-center of child
        cx1 = root_x + ROOT_W / 2
        cy1 = root_y + root_h
        cx2 = x + BOX_W / 2
        cy2 = children_y
        mid_y = (cy1 + cy2) / 2
        parts.append(f'<path d="M {cx1} {cy1} C {cx1} {mid_y}, {cx2} {mid_y}, {cx2} {cy2}" '
                     f'fill="none" stroke="{COL_BORDER}" stroke-width="1.4"/>')
        parts.append(f'<circle cx="{cx2}" cy="{cy2}" r="3" fill="{COL_HEADER_BG}"/>')

        box_svg, _ = render_class_box(x, children_y, title, rows)
        parts.append(box_svg)
        x += BOX_W + GAP_X

    parts.append('</svg>')
    return "\n".join(parts)


if __name__ == "__main__":
    svg = build()
    out_path = "bestmeta_diagram.svg"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print("written:", out_path)
    print("length:", len(svg))
