---
search:
  boost: 5.0
---

# Slot: tracking_confidence_threshold 


_Confidence or likelihood threshold used to accept detections, identities, tracks, or keypoints during tracking analysis._



<div data-search-exclude markdown="1">



URI: [bstm:tracking_confidence_threshold](bstm:tracking_confidence_threshold)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |









## Examples

| Value |
| --- |
| 0.9 |
| 0.3 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:tracking_confidence_threshold |
| native | bstm:tracking_confidence_threshold |




## LinkML Source

<details>
```yaml
name: tracking_confidence_threshold
description: Confidence or likelihood threshold used to accept detections, identities,
  tracks, or keypoints during tracking analysis.
examples:
- value: '0.9'
- value: '0.3'
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: float
required: false
recommended: true

```
</details></div>