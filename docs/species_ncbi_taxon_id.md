---
search:
  boost: 5.0
---

# Slot: species_ncbi_taxon_id 


_NCBI Taxonomy ID for the study organism_



<div data-search-exclude markdown="1">



URI: [BeStMeta:species_ncbi_taxon_id](https://w3id.org/BeStMeta/species_ncbi_taxon_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Subject](Subject.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+$` |











## Examples

| Value |
| --- |
| 7955 |
| 10090 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:species_ncbi_taxon_id |
| native | BeStMeta:species_ncbi_taxon_id |
| exact | dwc:taxonID, EDAM.DATA:1179 |




## LinkML Source

<details>
```yaml
name: species_ncbi_taxon_id
description: NCBI Taxonomy ID for the study organism
examples:
- value: '7955'
- value: '10090'
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dwc:taxonID
- EDAM.DATA:1179
rank: 1000
domain_of:
- Subject
range: string
required: false
recommended: true
pattern: ^\d+$

```
</details></div>