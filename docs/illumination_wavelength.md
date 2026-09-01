---
search:
  boost: 5.0
---

# Slot: illumination_wavelength 


_Peak wavelength of the illumination source in nanometres. Use for non-white-light sources such as infrared or UV._



<div data-search-exclude markdown="1">



URI: [BeStMeta:illumination_wavelength](https://w3id.org/BeStMeta/illumination_wavelength)
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
| ucum_code | nm |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:illumination_wavelength |
| native | BeStMeta:illumination_wavelength |
| exact | AFR:0001159 |
| close | PATO:0001242 |




## LinkML Source

<details>
```yaml
name: illumination_wavelength
description: Peak wavelength of the illumination source in nanometres. Use for non-white-light
  sources such as infrared or UV.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0001159
close_mappings:
- PATO:0001242
rank: 1000
domain_of:
- AcquisitionParameters
range: float
required: false
unit:
  ucum_code: nm

```
</details></div>