---
search:
  boost: 5.0
---

# Slot: species_name 


_Scientific (Latin) binomial name of the study organism_



<div data-search-exclude markdown="1">



URI: [bstm:species_name](bstm:species_name)
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
| self | bstm:species_name |
| native | bstm:species_name |
| exact | dwc:scientificName, EDAM-DATA:1045 |




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
- EDAM-DATA:1045
rank: 1000
domain_of:
- ExperimentalConditions
range: string
required: true

```
</details></div>