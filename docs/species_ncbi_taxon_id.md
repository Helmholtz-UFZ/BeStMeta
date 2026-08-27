---
search:
  boost: 5.0
---

# Slot: species_ncbi_taxon_id 


_NCBI Taxonomy ID for the study organism_



<div data-search-exclude markdown="1">



URI: [bstm:species_ncbi_taxon_id](bstm:species_ncbi_taxon_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ExperimentalConditions](ExperimentalConditions.md) |

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
| self | bstm:species_ncbi_taxon_id |
| native | bstm:species_ncbi_taxon_id |
| exact | dwc:taxonID, EDAM-DATA:1179 |




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
- EDAM-DATA:1179
rank: 1000
domain_of:
- ExperimentalConditions
range: string
required: false
recommended: true
pattern: ^\d+$

```
</details></div>