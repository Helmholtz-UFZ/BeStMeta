---
search:
  boost: 5.0
---

# Slot: raw_tracking_data_doi 


_DOI of the deposited raw tracking data_



<div data-search-exclude markdown="1">



URI: [bstm:raw_tracking_data_doi](bstm:raw_tracking_data_doi)
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
| self | bstm:raw_tracking_data_doi |
| native | bstm:raw_tracking_data_doi |
| exact | schema:identifier |
| close | dcterms:identifier |




## LinkML Source

<details>
```yaml
name: raw_tracking_data_doi
description: DOI of the deposited raw tracking data
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- schema:identifier
close_mappings:
- dcterms:identifier
rank: 1000
domain_of:
- VTADataset
range: uri
required: false
pattern: ^https://doi\.org/10\.\d{4,9}/[-._;()+/:A-Za-z0-9%]+$

```
</details></div>