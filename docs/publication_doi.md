---
search:
  boost: 5.0
---

# Slot: publication_doi 


_DOI of the publication associated with the dataset._



<div data-search-exclude markdown="1">



URI: [bstm:publication_doi](bstm:publication_doi)
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
| Recommended | Yes |
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
| self | bstm:publication_doi |
| native | bstm:publication_doi |
| exact | schema:citation, dcterms:references |




## LinkML Source

<details>
```yaml
name: publication_doi
description: DOI of the publication associated with the dataset.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- schema:citation
- dcterms:references
rank: 1000
domain_of:
- VTADataset
range: uri
required: false
recommended: true
pattern: ^https://doi\.org/10\.\d{4,9}/[-._;()+/:A-Za-z0-9%]+$

```
</details></div>