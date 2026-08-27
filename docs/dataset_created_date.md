---
search:
  boost: 5.0
---

# Slot: dataset_created_date 


_Date when the dataset was created (YYYY-MM-DD)_



<div data-search-exclude markdown="1">



URI: [bstm:dataset_created_date](bstm:dataset_created_date)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VTADataset](VTADataset.md) | Top-level study and provenance metadata for a VTA dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [VTADataset](VTADataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:dataset_created_date |
| native | bstm:dataset_created_date |
| exact | dcterms:created |




## LinkML Source

<details>
```yaml
name: dataset_created_date
description: Date when the dataset was created (YYYY-MM-DD)
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dcterms:created
rank: 1000
domain_of:
- VTADataset
range: date
required: false

```
</details></div>