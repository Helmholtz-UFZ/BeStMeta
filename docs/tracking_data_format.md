---
search:
  boost: 5.0
---

# Slot: tracking_data_format 


_File format used to store tracking results, including coordinates, keypoints, identities, trajectories, annotations, or derived outputs._



<div data-search-exclude markdown="1">



URI: [BeStMeta:tracking_data_format](https://w3id.org/BeStMeta/tracking_data_format)
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
| CSV |
| HDF5 |
| JSON |
| NWB |
| DeepLabCut .h5 |
| SLEAP .slp |
| ZebraBox PHR |

## Notes

* Report the output format of the tracking results, not the raw video container.
* Use this for coordinate/keypoint files and derived tracking outputs.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:tracking_data_format |
| native | BeStMeta:tracking_data_format |




## LinkML Source

<details>
```yaml
name: tracking_data_format
description: File format used to store tracking results, including coordinates, keypoints,
  identities, trajectories, annotations, or derived outputs.
notes:
- Report the output format of the tracking results, not the raw video container.
- Use this for coordinate/keypoint files and derived tracking outputs.
examples:
- value: CSV
- value: HDF5
- value: JSON
- value: NWB
- value: DeepLabCut .h5
- value: SLEAP .slp
- value: ZebraBox PHR
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