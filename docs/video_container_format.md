---
search:
  boost: 5.0
---

# Slot: video_container_format 


_File container format of the recorded video._



<div data-search-exclude markdown="1">



URI: [bstm:video_container_format](bstm:video_container_format)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VideoContainerEnum](VideoContainerEnum.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |








## Notes

* Report the container format, not the codec.
* Codec is captured separately in video_codec.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:video_container_format |
| native | bstm:video_container_format |
| exact | ebucore:hasContainerFormat |




## LinkML Source

<details>
```yaml
name: video_container_format
description: File container format of the recorded video.
notes:
- Report the container format, not the codec.
- Codec is captured separately in video_codec.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- ebucore:hasContainerFormat
rank: 1000
domain_of:
- AcquisitionParameters
range: VideoContainerEnum
required: true

```
</details></div>