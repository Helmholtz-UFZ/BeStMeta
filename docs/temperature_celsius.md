---
search:
  boost: 5.0
---

# Slot: temperature_celsius 


_Water or ambient temperature during the recording in degrees Celsius_



<div data-search-exclude markdown="1">



URI: [bstm:temperature_celsius](bstm:temperature_celsius)
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
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | Cel |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:temperature_celsius |
| native | bstm:temperature_celsius |




## LinkML Source

<details>
```yaml
name: temperature_celsius
description: Water or ambient temperature during the recording in degrees Celsius
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- ExperimentalConditions
range: float
required: false
recommended: true
unit:
  ucum_code: Cel

```
</details></div>