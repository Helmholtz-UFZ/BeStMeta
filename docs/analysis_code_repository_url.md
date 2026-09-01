---
search:
  boost: 5.0
---

# Slot: analysis_code_repository_url 


_URL of the code repository._



<div data-search-exclude markdown="1">



URI: [BeStMeta:analysis_code_repository_url](https://w3id.org/BeStMeta/analysis_code_repository_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VTADataset](VTADataset.md) | Top-level study and provenance metadata for a VTA dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
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
| self | BeStMeta:analysis_code_repository_url |
| native | BeStMeta:analysis_code_repository_url |
| exact | schema:codeRepository, schema:url |




## LinkML Source

<details>
```yaml
name: analysis_code_repository_url
description: URL of the code repository.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- schema:codeRepository
- schema:url
rank: 1000
domain_of:
- VTADataset
range: uri
required: false

```
</details></div>