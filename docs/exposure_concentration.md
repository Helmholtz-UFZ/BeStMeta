---
search:
  boost: 5.0
---

# Slot: exposure_concentration 


_Nominal exposure concentration (numeric value only; use unit field)._



<div data-search-exclude markdown="1">



URI: [bstm:exposure_concentration](bstm:exposure_concentration)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
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
| self | bstm:exposure_concentration |
| native | bstm:exposure_concentration |
| exact | EDAM-DATA:2140 |




## LinkML Source

<details>
```yaml
name: exposure_concentration
description: Nominal exposure concentration (numeric value only; use unit field).
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- EDAM-DATA:2140
rank: 1000
domain_of:
- ExperimentalConditions
range: float
required: false
recommended: true

```
</details></div>