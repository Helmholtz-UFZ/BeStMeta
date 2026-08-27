---
search:
  boost: 5.0
---

# Slot: exposure_duration_h 


_Duration of chemical or treatment exposure in hours._



<div data-search-exclude markdown="1">



URI: [bstm:exposure_duration_h](bstm:exposure_duration_h)
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
| ucum_code | h |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:exposure_duration_h |
| native | bstm:exposure_duration_h |




## LinkML Source

<details>
```yaml
name: exposure_duration_h
description: Duration of chemical or treatment exposure in hours.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- ExperimentalConditions
range: float
required: false
unit:
  ucum_code: h

```
</details></div>