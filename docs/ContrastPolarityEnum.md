---
search:
  boost: 2.0
---


# Enum: ContrastPolarityEnum 




_Polarity of object-to-background contrast in the video._



<div data-search-exclude markdown="1">

URI: [BeStMeta:ContrastPolarityEnum](https://w3id.org/BeStMeta/ContrastPolarityEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| bright_on_dark | None | Tracked object appears brighter than the background (analogous to dark-field ... |
| dark_on_bright | None | Tracked object appears darker than the background (analogous to bright-field ... |
| mixed | None | Polarity varies across regions, frames, or channels |
| unknown | None | Polarity not determined or not reported |




## Slots

| Name | Description |
| ---  | --- |
| [contrast_polarity](contrast_polarity.md) | Contrast relationship between the tracked object and the background; indicate... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: ContrastPolarityEnum
description: Polarity of object-to-background contrast in the video.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  bright_on_dark:
    text: bright_on_dark
    description: Tracked object appears brighter than the background (analogous to
      dark-field imaging).
  dark_on_bright:
    text: dark_on_bright
    description: Tracked object appears darker than the background (analogous to bright-field
      imaging).
  mixed:
    text: mixed
    description: Polarity varies across regions, frames, or channels.
  unknown:
    text: unknown
    description: Polarity not determined or not reported.

```
</details>

</div>