---
search:
  boost: 5.0
---

# Slot: behavioral_metrics 


_List of behavioral metrics or endpoints extracted from tracking data._



<div data-search-exclude markdown="1">



URI: [bstm:behavioral_metrics](bstm:behavioral_metrics)
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
| total distance moved |
| average velocity |
| time in center zone |
| freezing duration |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:behavioral_metrics |
| native | bstm:behavioral_metrics |




## LinkML Source

<details>
```yaml
name: behavioral_metrics
description: List of behavioral metrics or endpoints extracted from tracking data.
examples:
- value: total distance moved
- value: average velocity
- value: time in center zone
- value: freezing duration
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