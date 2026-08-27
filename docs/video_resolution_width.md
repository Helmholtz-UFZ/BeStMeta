---
search:
  boost: 5.0
---

# Slot: video_resolution_width 


_Horizontal pixel count of the recorded video._



<div data-search-exclude markdown="1">



URI: [bstm:video_resolution_width](bstm:video_resolution_width)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | px |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:video_resolution_width |
| native | bstm:video_resolution_width |
| close | ebucore:width |




## LinkML Source

<details>
```yaml
name: video_resolution_width
description: Horizontal pixel count of the recorded video.
from_schema: https://w3id.org/bestmeta/schema
close_mappings:
- ebucore:width
rank: 1000
domain_of:
- AcquisitionParameters
range: integer
required: true
unit:
  ucum_code: px

```
</details></div>