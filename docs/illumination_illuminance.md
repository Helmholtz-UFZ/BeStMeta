---
search:
  boost: 5.0
---

# Slot: illumination_illuminance 


_Illuminance at the recording arena or observation surface._



<div data-search-exclude markdown="1">



URI: [bstm:illumination_illuminance](bstm:illumination_illuminance)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | lx |

</details>










## Examples

| Value |
| --- |
| 0 |
| 100 |
| 1000 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:illumination_illuminance |
| native | bstm:illumination_illuminance |
| exact | OM:Illuminance |




## LinkML Source

<details>
```yaml
name: illumination_illuminance
description: Illuminance at the recording arena or observation surface.
examples:
- value: '0'
  description: Dark condition
- value: '100'
  description: Dim illumination
- value: '1000'
  description: Bright laboratory illumination
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- OM:Illuminance
rank: 1000
domain_of:
- AcquisitionParameters
range: float
required: false
unit:
  ucum_code: lx

```
</details></div>