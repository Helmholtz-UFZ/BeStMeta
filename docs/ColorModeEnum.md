---
search:
  boost: 2.0
---


# Enum: ColorModeEnum 




_Color mode of the video recording._



<div data-search-exclude markdown="1">

URI: [bstm:ColorModeEnum](bstm:ColorModeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| grayscale | None | Single-channel intensity image |
| rgb | None | Three-channel red-green-blue color image |
| other | None | Other color mode; describe in acquisition_notes |




## Slots

| Name | Description |
| ---  | --- |
| [color_mode](color_mode.md) | Color mode of the recorded video |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: ColorModeEnum
description: Color mode of the video recording.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  grayscale:
    text: grayscale
    description: Single-channel intensity image.
  rgb:
    text: rgb
    description: Three-channel red-green-blue color image.
  other:
    text: other
    description: Other color mode; describe in acquisition_notes.

```
</details>

</div>