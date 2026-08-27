---
search:
  boost: 2.0
---


# Enum: CameraDeviceTypeEnum 




_General types of imaging devices used in VTA setups._



<div data-search-exclude markdown="1">

URI: [bstm:CameraDeviceTypeEnum](bstm:CameraDeviceTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| digital_camera | OBI:0001048 |  |
| usb_camera | None |  |
| microscope_camera | SNOMED:706582001 |  |
| smartphone | SNOMED:733681009 |  |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [camera_device_type](camera_device_type.md) | General type of imaging device |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: CameraDeviceTypeEnum
description: General types of imaging devices used in VTA setups.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  digital_camera:
    text: digital_camera
    meaning: OBI:0001048
  usb_camera:
    text: usb_camera
  microscope_camera:
    text: microscope_camera
    meaning: SNOMED:706582001
  smartphone:
    text: smartphone
    meaning: SNOMED:733681009
  other:
    text: other

```
</details>

</div>