---
search:
  boost: 5.0
---

# Slot: dropped_frames_count 


_Number of video frames lost or omitted during acquisition._



<div data-search-exclude markdown="1">



URI: [bstm:dropped_frames_count](bstm:dropped_frames_count)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |









## Examples

| Value |
| --- |
| 0 |
| 12 |

## Notes

* Report frames missing due to acquisition, recording, or encoding issues.
* A value of 0 indicates no dropped frames were detected.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:dropped_frames_count |
| native | bstm:dropped_frames_count |




## LinkML Source

<details>
```yaml
name: dropped_frames_count
description: Number of video frames lost or omitted during acquisition.
notes:
- Report frames missing due to acquisition, recording, or encoding issues.
- A value of 0 indicates no dropped frames were detected.
examples:
- value: '0'
- value: '12'
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: integer
required: false
recommended: true

```
</details></div>