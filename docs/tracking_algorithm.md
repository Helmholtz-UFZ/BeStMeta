---
search:
  boost: 5.0
---

# Slot: tracking_algorithm 


_Algorithmic approach used to detect, identify, and track organisms in video recordings. Multiple values may be provided when tracking is performed using a pipeline of methods._



<div data-search-exclude markdown="1">



URI: [bstm:tracking_algorithm](bstm:tracking_algorithm)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| background subtraction |
| centroid tracking |
| YOLO object detection |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:tracking_algorithm |
| native | bstm:tracking_algorithm |




## LinkML Source

<details>
```yaml
name: tracking_algorithm
description: Algorithmic approach used to detect, identify, and track organisms in
  video recordings. Multiple values may be provided when tracking is performed using
  a pipeline of methods.
examples:
- value: background subtraction
- value: centroid tracking
- value: YOLO object detection
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>