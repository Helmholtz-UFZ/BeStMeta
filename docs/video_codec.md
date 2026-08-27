---
search:
  boost: 5.0
---

# Slot: video_codec 


_Video compression codec used for recording._



<div data-search-exclude markdown="1">



URI: [bstm:video_codec](bstm:video_codec)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VideoCodecEnum](VideoCodecEnum.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |








## Notes

* Report the codec, not the container format.
* Container format is captured separately in video_container_format.
* mp4 is a container, not a codec — most mp4 files use H264 or H265 as codec.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:video_codec |
| native | bstm:video_codec |
| exact | ebucore:codecName |




## LinkML Source

<details>
```yaml
name: video_codec
description: Video compression codec used for recording.
notes:
- Report the codec, not the container format.
- Container format is captured separately in video_container_format.
- mp4 is a container, not a codec — most mp4 files use H264 or H265 as codec.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- ebucore:codecName
rank: 1000
domain_of:
- AcquisitionParameters
range: VideoCodecEnum
required: false
recommended: true

```
</details></div>