---
search:
  boost: 5.0
---

# Slot: n_bodyparts_tracked 


_Number of body parts or keypoints tracked per individual._



<div data-search-exclude markdown="1">



URI: [BeStMeta:n_bodyparts_tracked](https://w3id.org/BeStMeta/n_bodyparts_tracked)
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








## Notes

* For centroid tracking, use 1.
* For pose-estimation approaches, report the number of tracked landmarks.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:n_bodyparts_tracked |
| native | BeStMeta:n_bodyparts_tracked |




## LinkML Source

<details>
```yaml
name: n_bodyparts_tracked
description: Number of body parts or keypoints tracked per individual.
notes:
- For centroid tracking, use 1.
- For pose-estimation approaches, report the number of tracked landmarks.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: integer
required: false
recommended: true

```
</details></div>