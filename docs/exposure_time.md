---
search:
  boost: 5.0
---

# Slot: exposure_time 


_Camera sensor exposure time per frame._



<div data-search-exclude markdown="1">



URI: [bstm:exposure_time](bstm:exposure_time)
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
| Recommended | Yes |
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | ms |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:exposure_time |
| native | bstm:exposure_time |
| exact | REPR:ExposureTime |




## LinkML Source

<details>
```yaml
name: exposure_time
description: Camera sensor exposure time per frame.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- REPR:ExposureTime
rank: 1000
domain_of:
- AcquisitionParameters
range: float
required: false
recommended: true
unit:
  ucum_code: ms

```
</details></div>