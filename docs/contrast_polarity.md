---
search:
  boost: 5.0
---

# Slot: contrast_polarity 


_Contrast relationship between the tracked object and the background; indicates whether the subject appears bright on a dark background or dark on a bright background in the recorded video._



<div data-search-exclude markdown="1">



URI: [BeStMeta:contrast_polarity](https://w3id.org/BeStMeta/contrast_polarity)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VideoHardware](VideoHardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ContrastPolarityEnum](ContrastPolarityEnum.md) |
| Domain Of | [VideoHardware](VideoHardware.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:contrast_polarity |
| native | BeStMeta:contrast_polarity |




## LinkML Source

<details>
```yaml
name: contrast_polarity
description: Contrast relationship between the tracked object and the background;
  indicates whether the subject appears bright on a dark background or dark on a bright
  background in the recorded video.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- VideoHardware
range: ContrastPolarityEnum
required: false
recommended: true

```
</details></div>