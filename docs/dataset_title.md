---
search:
  boost: 5.0
---

# Slot: dataset_title 


_Descriptive title of the dataset._



<div data-search-exclude markdown="1">



URI: [bstm:dataset_title](bstm:dataset_title)
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
| self | bstm:dataset_title |
| native | bstm:dataset_title |
| exact | dcterms:title |




## LinkML Source

<details>
```yaml
name: dataset_title
description: Descriptive title of the dataset.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dcterms:title
rank: 1000
domain_of:
- VTADataset
range: string
required: true

```
</details></div>