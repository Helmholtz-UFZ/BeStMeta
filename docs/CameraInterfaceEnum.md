---
search:
  boost: 2.0
---


# Enum: CameraInterfaceEnum 




_Data interface used to connect the camera to a recording system._



<div data-search-exclude markdown="1">

URI: [BeStMeta:CameraInterfaceEnum](https://w3id.org/BeStMeta/CameraInterfaceEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| usb2 | None | USB 2 |
| usb3 | None | USB 3 |
| gige | None | Gigabit Ethernet (GigE Vision) interface |
| camera_link | None | Camera Link interface, commonly used in machine vision |
| coaxpress | None | CoaXPress high-speed coaxial interface |
| firewire | None | IEEE 1394 (FireWire) interface |
| hdmi | None | HDMI video output interface |
| wireless | None | Wireless connection (e |
| internal_integrated | None | Camera is internally integrated into the recording device with no external in... |
| other | None | Interface type not covered by other enum values |




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
description: Data interface used to connect the camera to a recording system.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  usb2:
    text: usb2
    description: USB 2.0 interface.
  usb3:
    text: usb3
    description: USB 3.0 / USB 3.1 / USB 3.2 interface.
  gige:
    text: gige
    description: Gigabit Ethernet (GigE Vision) interface.
  camera_link:
    text: camera_link
    description: Camera Link interface, commonly used in machine vision.
  coaxpress:
    text: coaxpress
    description: CoaXPress high-speed coaxial interface.
  firewire:
    text: firewire
    description: IEEE 1394 (FireWire) interface.
  hdmi:
    text: hdmi
    description: HDMI video output interface.
  wireless:
    text: wireless
    description: Wireless connection (e.g. Wi-Fi, Bluetooth).
  internal_integrated:
    text: internal_integrated
    description: Camera is internally integrated into the recording device with no
      external interface (e.g. smartphone camera, closed-box system).
  other:
    text: other
    description: Interface type not covered by other enum values.

```
</details>

</div>