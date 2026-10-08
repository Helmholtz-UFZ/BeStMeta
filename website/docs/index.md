# Introduction

Welcome to the documentation for the **BeStMeta Metadata Schema** — a
cross-domain metadata schema for **video tracking assays (VTAs)** with a focus
on ecotoxicology and biomedical research.

!!! info "What is this?"
    BeStMeta provides structured, machine-readable metadata for VTA datasets and
    individual trials, so that experiments are easier to find, understand, and
    reuse. It is designed to improve **FAIR** (Findable, Accessible,
    Interoperable, Reusable) compliance.

## How to read these docs

- **Introduction** *(you are here)* — a short orientation to the schema.
- **Overview on the Schema** — one page per class. Each page lists that class's
  **slots** (fields), their data types, whether they are required or
  recommended, and how they map to external ontologies.
- **Enums & Types** — the controlled vocabularies (enumerations) and data types
  used across the schema.

## The schema at a glance

The schema is organised around a top-level `VTADataset` record, which nests a
number of thematic classes:

| Class | What it captures |
| --- | --- |
| **VTADataset** | Study-level, licensing and bibliographic metadata (the root). |
| **ExperimentalConditions** | Organism, treatment, assay design and environment. |
| **VideoHardware** | Cameras, optics and physical recording setup. |
| **AcquisitionParameters** | Video acquisition and recording settings. |
| **TrackingAnalysis** | Tracking software, algorithms and derived metrics. |
| **StatisticalAnalysis** | Statistical tests, models and significance criteria. |

Use the navigation menu on the left to explore each class in detail.

## Reusing the schema

The schema is written in [LinkML](https://linkml.io/). The canonical source
lives in this repository as `bestmeta_schema.yaml`. From it you can generate JSON Schema,
SHACL, OWL, Python classes, and more, using the standard LinkML generators.

---

*This documentation is generated automatically from the LinkML source. To edit
this introduction, change `docs/index.md`. To restyle or rebrand the site, edit
`site.config.yml`.*
The content here needs to change, but can be done later
