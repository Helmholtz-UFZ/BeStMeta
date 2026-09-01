---
search:
  boost: 5.0
---

# Slot: species_name 


_Scientific (Latin) binomial name of the study organism_



<div data-search-exclude markdown="1">



URI: [BeStMeta:species_name](https://w3id.org/BeStMeta/species_name)
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
| Required | Yes |









## Examples

| Value |
| --- |
| Danio rerio |
| Mus musculus |
| Daphnia magna |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:species_name |
| native | BeStMeta:species_name |
| exact | dwc:scientificName, EDAM.DATA:1045 |




## LinkML Source

<details>
```yaml
name: species_name
description: Scientific (Latin) binomial name of the study organism
examples:
- value: Danio rerio
- value: Mus musculus
- value: Daphnia magna
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dwc:scientificName
- EDAM.DATA:1045
rank: 1000
domain_of:
- Subject
range: string
required: true

```
</details></div>