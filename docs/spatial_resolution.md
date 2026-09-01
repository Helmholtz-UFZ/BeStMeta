---
search:
  boost: 5.0
---

# Slot: spatial_resolution 


_Physical size represented by one pixel at the observation plane._



<div data-search-exclude markdown="1">



URI: [BeStMeta:spatial_resolution](https://w3id.org/BeStMeta/spatial_resolution)
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
| ucum_code | mm/px |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:spatial_resolution |
| native | BeStMeta:spatial_resolution |
| close | dicom:SpatialResolution |




## LinkML Source

<details>
```yaml
name: spatial_resolution
description: Physical size represented by one pixel at the observation plane.
from_schema: https://w3id.org/bestmeta/schema
close_mappings:
- dicom:SpatialResolution
rank: 1000
domain_of:
- AcquisitionParameters
range: float
required: false
recommended: true
unit:
  ucum_code: mm/px

```
</details></div>