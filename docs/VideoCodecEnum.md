---
search:
  boost: 2.0
---


# Enum: VideoCodecEnum 




_Video compression codec used for recording._



<div data-search-exclude markdown="1">

URI: [BeStMeta:VideoCodecEnum](https://w3id.org/BeStMeta/VideoCodecEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| h264 | None |  |
| h265 | None |  |
| ffv1 | None |  |
| av1 | None |  |
| mjpeg | None |  |
| mpeg4 | None | MPEG-4 Part 2 codec (DivX/Xvid); not to be confused with the mp4 container fo... |
| raw | None | Uncompressed video; no codec applied |
| other | None | Other codec; describe in acquisition_notes |




## Slots

| Name | Description |
| ---  | --- |
| [video_codec](video_codec.md) | Video compression codec used for recording |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: VideoCodecEnum
description: Video compression codec used for recording.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  h264:
    text: h264
  h265:
    text: h265
  ffv1:
    text: ffv1
  av1:
    text: av1
  mjpeg:
    text: mjpeg
  mpeg4:
    text: mpeg4
    description: MPEG-4 Part 2 codec (DivX/Xvid); not to be confused with the mp4
      container format.
  raw:
    text: raw
    description: Uncompressed video; no codec applied.
  other:
    text: other
    description: Other codec; describe in acquisition_notes.

```
</details>

</div>