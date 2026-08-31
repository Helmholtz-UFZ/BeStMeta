---
search:
  boost: 2.0
---


# Enum: CameraPositionEnum 




_Position of the camera relative to the arena used to record the tracked organism(s)._



<div data-search-exclude markdown="1">

URI: [BeStMeta:CameraPositionEnum](https://w3id.org/BeStMeta/CameraPositionEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| overhead | None | Camera positioned vertically above the arena |
| lateral | None | Camera positioned horizontally from the side |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [camera_position](camera_position.md) | Position of the camera relative to the arena |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: CameraPositionEnum
description: Position of the camera relative to the arena used to record the tracked
  organism(s).
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  overhead:
    text: overhead
    description: Camera positioned vertically above the arena.
  lateral:
    text: lateral
    description: Camera positioned horizontally from the side.
  other:
    text: other

```
</details>

</div>