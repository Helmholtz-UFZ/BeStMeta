---
search:
  boost: 2.0
---


# Enum: DeviceTypeEnum 




_Category of recording system used to record the videos._



<div data-search-exclude markdown="1">

URI: [BeStMeta:DeviceTypeEnum](https://w3id.org/BeStMeta/DeviceTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| camera | None | A standalone camera system |
| microscope | None | A microscope-integrated imaging system |
| closed_box_system | None | A commercial, integrated/closed-box imaging system where individual camera or... |
| in_house_system | None | A custom-built or lab-assembled imaging system not corresponding to a single ... |




## Slots

| Name | Description |
| ---  | --- |
| [device_type](device_type.md) | Indicates the category of imaging system used; determines which additional ha... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: DeviceTypeEnum
description: Category of recording system used to record the videos.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  camera:
    text: camera
    description: A standalone camera system.
  microscope:
    text: microscope
    description: A microscope-integrated imaging system.
  closed_box_system:
    text: closed_box_system
    description: A commercial, integrated/closed-box imaging system where individual
      camera or microscope specs are not user-accessible (e.g. a proprietary multi-well
      plate-based VTA device used in ecotox screening, such as DanioVision or ZebraBox).
  in_house_system:
    text: in_house_system
    description: A custom-built or lab-assembled imaging system not corresponding
      to a single off-the-shelf camera or microscope product.

```
</details>

</div>