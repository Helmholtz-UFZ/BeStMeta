---
search:
  boost: 5.0
---

# Slot: dataset_id 


_Unique identifier for the dataset or study package._



<div data-search-exclude markdown="1">



URI: [BeStMeta:dataset_id](https://w3id.org/BeStMeta/dataset_id)
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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:dataset_id |
| native | BeStMeta:dataset_id |
| exact | dcterms:identifier |




## LinkML Source

<details>
```yaml
name: dataset_id
description: Unique identifier for the dataset or study package.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dcterms:identifier
rank: 1000
identifier: true
domain_of:
- VTADataset
range: string
required: true

```
</details></div>