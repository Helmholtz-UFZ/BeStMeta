---
search:
  boost: 5.0
---

# Slot: raw_data_repository 


_Repository where raw tracking data and/or video files are deposited._



<div data-search-exclude markdown="1">



URI: [BeStMeta:raw_data_repository](https://w3id.org/BeStMeta/raw_data_repository)
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
| self | BeStMeta:raw_data_repository |
| native | BeStMeta:raw_data_repository |




## LinkML Source

<details>
```yaml
name: raw_data_repository
description: Repository where raw tracking data and/or video files are deposited.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- VTADataset
range: string
required: false
recommended: true

```
</details></div>