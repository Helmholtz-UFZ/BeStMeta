---
search:
  boost: 5.0
---

# Slot: dataset_creator_name 


_Name(s) of data creators._



<div data-search-exclude markdown="1">



URI: [BeStMeta:dataset_creator_name](https://w3id.org/BeStMeta/dataset_creator_name)
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
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:dataset_creator_name |
| native | BeStMeta:dataset_creator_name |
| exact | dcterms:creator, schema:creator |




## LinkML Source

<details>
```yaml
name: dataset_creator_name
description: Name(s) of data creators.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dcterms:creator
- schema:creator
rank: 1000
domain_of:
- VTADataset
range: string
required: false
recommended: true
multivalued: true

```
</details></div>