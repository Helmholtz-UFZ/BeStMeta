---
search:
  boost: 5.0
---

# Slot: habituation_duration_min 


_Duration of habituation period before recording, in minutes_



<div data-search-exclude markdown="1">



URI: [bstm:habituation_duration_min](bstm:habituation_duration_min)
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
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | min |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:habituation_duration_min |
| native | bstm:habituation_duration_min |




## LinkML Source

<details>
```yaml
name: habituation_duration_min
description: Duration of habituation period before recording, in minutes
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- ExperimentalConditions
range: float
required: false
unit:
  ucum_code: min

```
</details></div>