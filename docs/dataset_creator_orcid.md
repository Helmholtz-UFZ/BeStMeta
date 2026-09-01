---
search:
  boost: 5.0
---

# Slot: dataset_creator_orcid 


_ORCID identifier of the dataset creator._



<div data-search-exclude markdown="1">



URI: [BeStMeta:dataset_creator_orcid](https://w3id.org/BeStMeta/dataset_creator_orcid)
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
| Multivalued | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:dataset_creator_orcid |
| native | BeStMeta:dataset_creator_orcid |
| exact | schema:identifier, dcterms:identifier |




## LinkML Source

<details>
```yaml
name: dataset_creator_orcid
description: ORCID identifier of the dataset creator.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- schema:identifier
- dcterms:identifier
rank: 1000
domain_of:
- VTADataset
range: uri
required: false
recommended: true
multivalued: true
pattern: ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$

```
</details></div>