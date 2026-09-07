---
search:
  boost: 2.0
---


# Enum: CameraTypeEnum 




_Type of camera used to record the videos._



<div data-search-exclude markdown="1">

URI: [BeStMeta:CameraTypeEnum](https://w3id.org/BeStMeta/CameraTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| machine_vision_camera | None | Industrial/scientific machine vision camera (e |
| webcam | None | Consumer-grade webcam |
| smartphone_camera | None | Camera integrated into a smartphone or tablet |
| action_camera | None | Ruggedized action camera (e |
| dslr_mirrorless_camera | None | DSLR or mirrorless consumer/prosumer camera |
| thermal_camera | None | Infrared/thermal imaging camera |
| other | None | Camera type not covered by other enum values |




## Slots

| Name | Description |
| ---  | --- |
| [camera_type](camera_type.md) | General type of imaging device |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: CameraTypeEnum
description: Type of camera used to record the videos.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  machine_vision_camera:
    text: machine_vision_camera
    description: Industrial/scientific machine vision camera (e.g. Basler, FLIR).
  webcam:
    text: webcam
    description: Consumer-grade webcam.
  smartphone_camera:
    text: smartphone_camera
    description: Camera integrated into a smartphone or tablet.
  action_camera:
    text: action_camera
    description: Ruggedized action camera (e.g. GoPro-type device).
  dslr_mirrorless_camera:
    text: dslr_mirrorless_camera
    description: DSLR or mirrorless consumer/prosumer camera.
  thermal_camera:
    text: thermal_camera
    description: Infrared/thermal imaging camera.
  other:
    text: other
    description: Camera type not covered by other enum values.

```
</details>

</div>