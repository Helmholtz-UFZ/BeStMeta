# BeStMeta
FAIR metadata schema for video tracking assays

> **Status: DRAFT v0.1.0** — community review invited. Please open a GitHub Issue for field-level feedback.

A LinkML-based metadata schema for **Video Tracking Assays (VTAs)** across ecotoxicology, biomedical / neuroscience, and related biological research domains. The schema is designed to capture dataset provenance, experimental conditions, video acquisition parameters, tracking analysis, and statistical methods in a standardized, interoperable format.

## Schema Structure

The schema defines **6 classes** covering the full VTA workflow:

| Class | Description |
|---|---|
| `VTADataset` | Study provenance, identifiers, license, creator information, repository links |
| `ExperimentalConditions` | Organism, treatment, life stage or age, assay design, arena properties, treatment |
| `VideoHardware` | Camera, microscope, optics, illumination |
| `AcquisitionParameters` | Recording timing and duration, frame rate, resolution, codec |
| `TrackingAnalysis` | Tracking software, algorithm, settings, preprocessing, tracked outputs, endpoints |
| `StatisticalAnalysis` | Statistical software, tests, models |

`VTADataset` is the top-level container.

## Files and Structure

```
.
├── README.md                          ← This file
├── LICENSE                            ← CC-BY 4.0 license
├── bestmeta_schema.yaml               ← Master schema (LinkML YAML format)
├── bestmeta_schema.json               ← Generated JSON Schema
├── bestmeta.xlsx                      ← Schema in spreadsheet format
├── context.jsonld                     ← JSON-LD context for semantic web
├── diagrams/                          ← Schema diagrams and visualizations
└── docs/                              ← Generated documentation
```

## Field Tier System

Fields are marked in descriptions as:

- **TIER 1 MANDATORY** — Required for basic reproducibility
- **TIER 2 RECOMMENDED** — Strongly endorsed by community survey (>70% rated essential)
- Unlabelled fields — Optional / domain-specific

## Installation & Usage

### Requirements

- LinkML >= 1.5.0
- Python 3.8+

### Setup

```bash
pip install linkml
```

### Validate an Example

```bash
linkml-validate -s bestmeta_schema.yaml examples/zebrafish-ecotox-example.yaml
```

### Generate Derived Formats

```bash
# Generate JSON Schema
gen-jsonschema bestmeta_schema.yaml > bestmeta_schema.json

# Generate Markdown documentation
gen-markdown bestmeta_schema.yaml -d docs/

# Generate RDF
gen-rdf bestmeta_schema.yaml > bestmeta_schema.rdf
```

## License

**Schema and code:** MIT License  
**Metadata content and documentation:** CC-BY 4.0

See [LICENSE](LICENSE) for details.

---

**Questions or Feedback?**  
Please open a GitHub Issue or start a discussion. Community input is invaluable as we refine the schema.
