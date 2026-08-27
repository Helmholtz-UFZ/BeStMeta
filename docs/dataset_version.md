---
search:
  boost: 5.0
---

# Slot: dataset_version 


_Semantic version string for the dataset (e.g. 1.0.0)_



<div data-search-exclude markdown="1">



URI: [bstm:dataset_version](bstm:dataset_version)
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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[0-9]+\.[0-9]+\.[0-9]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:dataset_version |
| native | bstm:dataset_version |
| exact | pav:version, schema:version |




## LinkML Source

<details>
```yaml
name: dataset_version
description: Semantic version string for the dataset (e.g. 1.0.0)
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- pav:version
- schema:version
rank: 1000
domain_of:
- VTADataset
range: string
required: false
pattern: ^[0-9]+\.[0-9]+\.[0-9]+$

```
</details></div>