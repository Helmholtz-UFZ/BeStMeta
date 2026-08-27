---
search:
  boost: 5.0
---

# Slot: strain 


_Organism strain or line_



<div data-search-exclude markdown="1">



URI: [bstm:strain](bstm:strain)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:strain |
| native | bstm:strain |
| exact | EDAM-DATA:2379 |




## LinkML Source

<details>
```yaml
name: strain
description: Organism strain or line
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- EDAM-DATA:2379
rank: 1000
domain_of:
- ExperimentalConditions
range: string
required: false
recommended: true

```
</details></div>