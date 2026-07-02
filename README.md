# BeStMeta
FAIR metadata schema for video tracking assays

> **Status: DRAFT v0.1.0** — community review invited. Please open a GitHub Issue for field-level feedback.

A LinkML-based metadata schema for **Video Tracking Assays (VTAs)** across ecotoxicology, biomedical / neuroscience, and related biological research domains. The schema is designed to capture dataset, experimental, acquisition, hardware, tracking, and statistical metadata to improve FAIR compliance by providing structured, machine-readable metadata alongside VTA datasets.

## Schema Structure

The schema defines **6 classes** covering the full VTA workflow:

| Class | Description |
|---|---|
| `VTADataset` | Study provenance, identifiers, license, creator information, repository links |
| `ExperimentalConditions` | Organism, treatment, life stage or age, assay design, arena properties, treatment |
| `VideoHardware` | Camera, microscope, optics, illumination |
| `AcquisitionParameters` | recording timing and duration, frame rate, resolution, codec |
| `TrackingAnalysis` | tracking software, algorithm, settings, preprocessing, tracked outputs, endpoints |
| `StatisticalAnalysis` | statistical software, tests, models |

`VTADataset` is the top-level container. 

## Files

```
vta-schema/
├── vta-schema.yaml                              ← Master schema (LinkML)
└── README.md
└── LICENSE


Fields are marked in descriptions as:
- **TIER 1 MANDATORY** — required for basic reproducibility
- **TIER 2 RECOMMENDED** — strongly endorsed by community survey (>70% rated essential)
- Unlabelled fields — optional / domain-specific

### Generate derived formats (requires LinkML)

```bash
pip install linkml

# Validate an example
linkml-validate -s vta-schema.yaml examples/zebrafish-ecotox-example.yaml

# Generate JSON Schema
gen-jsonschema vta-schema.yaml > vta-schema.json

# Generate Markdown documentation
gen-markdown vta-schema.yaml -d docs/

## License

CC-BY 4.0 — see [LICENSE](LICENSE)
EOF
Schema and code: MIT License. Metadata content and documentation: CC-BY 4.0.

