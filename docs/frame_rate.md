---
search:
  boost: 5.0
---

# Slot: frame_rate 


_Number of frames captured per second (fps) during video recording._



<div data-search-exclude markdown="1">



URI: [BeStMeta:frame_rate](https://w3id.org/BeStMeta/frame_rate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Acquisition](Acquisition.md) | Video acquisition and recording parameters, including timing encoding and ill... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Acquisition](Acquisition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | Hz |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:frame_rate |
| native | BeStMeta:frame_rate |
| exact | ebucore:frameRate |
| close | ma:frameRate |




## LinkML Source

<details>
```yaml
name: frame_rate
description: Number of frames captured per second (fps) during video recording.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- ebucore:frameRate
close_mappings:
- ma:frameRate
rank: 1000
domain_of:
- Acquisition
range: float
required: true
unit:
  ucum_code: Hz

```
</details></div>