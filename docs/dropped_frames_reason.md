---
search:
  boost: 5.0
---

# Slot: dropped_frames_reason 


_Reason for dropped or omitted frames during acquisition, recording, encoding, or quality control._



<div data-search-exclude markdown="1">



URI: [BeStMeta:dropped_frames_reason](https://w3id.org/BeStMeta/dropped_frames_reason)
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









## Examples

| Value |
| --- |
| Camera buffer overflow |
| Temporary USB bandwidth limitation |
| Corrupted frames removed during quality control |
| Frames dropped due to encoder performance limitations |
| Network transmission interruption |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:dropped_frames_reason |
| native | BeStMeta:dropped_frames_reason |




## LinkML Source

<details>
```yaml
name: dropped_frames_reason
description: Reason for dropped or omitted frames during acquisition, recording, encoding,
  or quality control.
examples:
- value: Camera buffer overflow
- value: Temporary USB bandwidth limitation
- value: Corrupted frames removed during quality control
- value: Frames dropped due to encoder performance limitations
- value: Network transmission interruption
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: string
required: false

```
</details></div>