---
search:
  boost: 5.0
---

# Slot: dataset_license 


_SPDX license identifier or URL (e.g. CC-BY-4.0)_



<div data-search-exclude markdown="1">



URI: [bstm:dataset_license](bstm:dataset_license)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VTADataset](VTADataset.md) | Top-level study and provenance metadata for a VTA dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [VTADataset](VTADataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:dataset_license |
| native | bstm:dataset_license |
| exact | dcterms:license |




## LinkML Source

<details>
```yaml
name: dataset_license
description: SPDX license identifier or URL (e.g. CC-BY-4.0)
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dcterms:license
rank: 1000
domain_of:
- VTADataset
range: string
required: true

```
</details></div>