---
search:
  boost: 5.0
---

# Slot: frames_without_tracked_bodypart 


_Percentage of frames in which no body part was tracked._



<div data-search-exclude markdown="1">



URI: [BeStMeta:frames_without_tracked_bodypart](https://w3id.org/BeStMeta/frames_without_tracked_bodypart)
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
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |
| Maximum Value | 100 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:frames_without_tracked_bodypart |
| native | BeStMeta:frames_without_tracked_bodypart |




## LinkML Source

<details>
```yaml
name: frames_without_tracked_bodypart
description: Percentage of frames in which no body part was tracked.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: float
required: false
recommended: true
minimum_value: 0
maximum_value: 100

```
</details></div>