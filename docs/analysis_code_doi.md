---
search:
  boost: 5.0
---

# Slot: analysis_code_doi 


_DOI of the deposited analysis code._



<div data-search-exclude markdown="1">



URI: [BeStMeta:analysis_code_doi](https://w3id.org/BeStMeta/analysis_code_doi)
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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^https://doi\.org/10\.\d{4,9}/[-._;()+/:A-Za-z0-9%]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:analysis_code_doi |
| native | BeStMeta:analysis_code_doi |




## LinkML Source

<details>
```yaml
name: analysis_code_doi
description: DOI of the deposited analysis code.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- VTADataset
range: uri
required: false
pattern: ^https://doi\.org/10\.\d{4,9}/[-._;()+/:A-Za-z0-9%]+$

```
</details></div>