---
search:
  boost: 2.0
---


# Enum: CameraSensorTypeEnum 




_Image sensor technologies used in cameras._



<div data-search-exclude markdown="1">

URI: [bstm:CameraSensorTypeEnum](bstm:CameraSensorTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ccd | CHMO:0002245 |  |
| cmos | None |  |
| scmos | None |  |
| emccd | None |  |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [camera_sensor_type](camera_sensor_type.md) | Image sensor technology |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: CameraSensorTypeEnum
description: Image sensor technologies used in cameras.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  ccd:
    text: ccd
    meaning: CHMO:0002245
  cmos:
    text: cmos
  scmos:
    text: scmos
  emccd:
    text: emccd
  other:
    text: other

```
</details>

</div>