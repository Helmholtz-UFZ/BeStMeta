---
search:
  boost: 5.0
---

# Slot: total_frame_count 


_Total number of frames in the video. Can be derived from frame_rate × recording_duration if not explicitly stated._



<div data-search-exclude markdown="1">



URI: [bstm:total_frame_count](bstm:total_frame_count)
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








## Notes

* Prefer direct reporting when available.
* If absent, it may be computed from frame rate and actual trial duration.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:total_frame_count |
| native | bstm:total_frame_count |
| exact | dicom:NumberOfFrames |




## LinkML Source

<details>
```yaml
name: total_frame_count
description: Total number of frames in the video. Can be derived from frame_rate ×
  recording_duration if not explicitly stated.
notes:
- Prefer direct reporting when available.
- If absent, it may be computed from frame rate and actual trial duration.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dicom:NumberOfFrames
rank: 1000
domain_of:
- AcquisitionParameters
range: integer
required: false

```
</details></div>