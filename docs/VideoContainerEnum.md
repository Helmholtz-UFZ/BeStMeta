---
search:
  boost: 2.0
---


# Enum: VideoContainerEnum 




_Video file container format._



<div data-search-exclude markdown="1">

URI: [bstm:VideoContainerEnum](bstm:VideoContainerEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| mp4 | None | MPEG-4 container |
| avi | None | Audio Video Interleave |
| mov | None | Apple QuickTime container |
| other | None | Other container format; describe in acquisition_notes |




## Slots

| Name | Description |
| ---  | --- |
| [video_container_format](video_container_format.md) | File container format of the recorded video |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: VideoContainerEnum
description: Video file container format.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  mp4:
    text: mp4
    description: MPEG-4 container.
  avi:
    text: avi
    description: Audio Video Interleave.
  mov:
    text: mov
    description: Apple QuickTime container.
  other:
    text: other
    description: Other container format; describe in acquisition_notes.

```
</details>

</div>