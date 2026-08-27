---
search:
  boost: 5.0
---

# Slot: lens_focal_length_mm 


_Focal length of the imaging lens in millimetres;  applicable to camera or microscope optics when reported._



<div data-search-exclude markdown="1">



URI: [bstm:lens_focal_length_mm](bstm:lens_focal_length_mm)
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
| self | bstm:lens_focal_length_mm |
| native | bstm:lens_focal_length_mm |
| exact | AFQ:0000062 |




## LinkML Source

<details>
```yaml
name: lens_focal_length_mm
description: Focal length of the imaging lens in millimetres;  applicable to camera
  or microscope optics when reported.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFQ:0000062
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