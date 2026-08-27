---
search:
  boost: 5.0
---

# Slot: camera_distance_mm 


_Distance from camera lens to the arena floor in millimetres._



<div data-search-exclude markdown="1">



URI: [bstm:camera_distance_mm](bstm:camera_distance_mm)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VideoHardware](VideoHardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [VideoHardware](VideoHardware.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | mm |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:camera_distance_mm |
| native | bstm:camera_distance_mm |




## LinkML Source

<details>
```yaml
name: camera_distance_mm
description: Distance from camera lens to the arena floor in millimetres.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- VideoHardware
range: float
required: false
recommended: true
unit:
  ucum_code: mm

```
</details></div>