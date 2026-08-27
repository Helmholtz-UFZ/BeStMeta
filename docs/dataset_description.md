---
search:
  boost: 5.0
---

# Slot: dataset_description 


_Free-text description of the dataset and its scientific purpose_



<div data-search-exclude markdown="1">



URI: [bstm:dataset_description](bstm:dataset_description)
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
| Recommended | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:dataset_description |
| native | bstm:dataset_description |
| exact | dcterms:description |




## LinkML Source

<details>
```yaml
name: dataset_description
description: Free-text description of the dataset and its scientific purpose
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dcterms:description
rank: 1000
domain_of:
- VTADataset
range: string
required: false
recommended: true

```
</details></div>