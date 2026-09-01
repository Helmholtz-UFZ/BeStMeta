---
search:
  boost: 5.0
---

# Slot: tracking_software_settings 


_Key tracking configuration parameters used during analysis, including software-specific settings required to reproduce tracking results._



<div data-search-exclude markdown="1">



URI: [BeStMeta:tracking_software_settings](https://w3id.org/BeStMeta/tracking_software_settings)
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









## Examples

| Value |
| --- |
| Detection threshold=25; minimum blob size=50 px |
| DeepLabCut likelihood threshold=0.9 |
| Interpolation enabled; gap length=5 frames |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:tracking_software_settings |
| native | BeStMeta:tracking_software_settings |




## LinkML Source

<details>
```yaml
name: tracking_software_settings
description: Key tracking configuration parameters used during analysis, including
  software-specific settings required to reproduce tracking results.
examples:
- value: Detection threshold=25; minimum blob size=50 px
- value: DeepLabCut likelihood threshold=0.9
- value: Interpolation enabled; gap length=5 frames
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: string
required: false
recommended: true

```
</details></div>