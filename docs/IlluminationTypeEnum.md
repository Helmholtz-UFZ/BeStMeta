---
search:
  boost: 2.0
---


# Enum: IlluminationTypeEnum 




_Technology type of the light source used during video recording._



<div data-search-exclude markdown="1">

URI: [bstm:IlluminationTypeEnum](bstm:IlluminationTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| white_light | None | Standard broadband visible light |
| infrared | None | Infrared illumination panel or backlight; use illumination_wavelength_nm for ... |
| fluorescent | None | Fluorescent light source |
| led | None | LED-based illumination without further specification |
| ambient | None | Environmental or room lighting without a dedicated source |
| none | None | No active illumination |
| other | None | Other illumination type; describe in acquisition_notes |




## Slots

| Name | Description |
| ---  | --- |
| [illumination_type](illumination_type.md) | Type of illumination used during recording |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: IlluminationTypeEnum
description: Technology type of the light source used during video recording.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  white_light:
    text: white_light
    description: Standard broadband visible light.
  infrared:
    text: infrared
    description: Infrared illumination panel or backlight; use illumination_wavelength_nm
      for exact wavelength.
  fluorescent:
    text: fluorescent
    description: Fluorescent light source.
  led:
    text: led
    description: LED-based illumination without further specification.
  ambient:
    text: ambient
    description: Environmental or room lighting without a dedicated source.
  none:
    text: none
    description: No active illumination.
  other:
    text: other
    description: Other illumination type; describe in acquisition_notes.

```
</details>

</div>