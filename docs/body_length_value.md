---
search:
  boost: 5.0
---

# Slot: body_length_value 


_Body length numeric value of the tracked organism(s)._



<div data-search-exclude markdown="1">



URI: [bstm:body_length_value](bstm:body_length_value)
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
| self | bstm:body_length_value |
| native | bstm:body_length_value |
| close | EFO:0004339, MESH:D049628 |




## LinkML Source

<details>
```yaml
name: body_length_value
description: Body length numeric value of the tracked organism(s).
from_schema: https://w3id.org/bestmeta/schema
close_mappings:
- EFO:0004339
- MESH:D049628
rank: 1000
domain_of:
- ExperimentalConditions
range: float
required: false
recommended: true

```
</details></div>