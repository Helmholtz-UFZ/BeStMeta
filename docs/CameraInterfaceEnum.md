---
search:
  boost: 2.0
---


# Enum: CameraInterfaceEnum 




_Hardware or connection interface used to transfer data from the camera to the recording system._



<div data-search-exclude markdown="1">

URI: [bstm:CameraInterfaceEnum](bstm:CameraInterfaceEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| usb | None |  |
| ethernet | None |  |
| ip | None |  |
| camera_link | None |  |
| coaxpress | None |  |
| hdmi | None |  |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [camera_interface](camera_interface.md) | Interface standard used for communication between the camera and the acquisit... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: CameraInterfaceEnum
description: Hardware or connection interface used to transfer data from the camera
  to the recording system.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  usb:
    text: usb
  ethernet:
    text: ethernet
  ip:
    text: ip
  camera_link:
    text: camera_link
  coaxpress:
    text: coaxpress
  hdmi:
    text: hdmi
  other:
    text: other

```
</details>

</div>