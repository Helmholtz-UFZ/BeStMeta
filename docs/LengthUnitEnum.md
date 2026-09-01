---
search:
  boost: 2.0
---


# Enum: LengthUnitEnum 




_Units of length, ranging from micrometers to meters._



<div data-search-exclude markdown="1">

URI: [BeStMeta:LengthUnitEnum](https://w3id.org/BeStMeta/LengthUnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| um | UO:0000017 |  |
| mm | UO:0000016 |  |
| cm | UO:0000015 |  |
| meter | UO:0000008 |  |




## Slots

| Name | Description |
| ---  | --- |
| [body_length_unit](body_length_unit.md) | Body length unit of the tracked organism(s) |
| [arena_length_unit](arena_length_unit.md) | Unit of measurement for arena_length |
| [arena_width_unit](arena_width_unit.md) | Unit of measurement for arena_width |
| [arena_height_unit](arena_height_unit.md) | Unit of measurement for arena_height |
| [field_of_view_unit](field_of_view_unit.md) | Unit of measurement for field_of_view_width and field_of_view_height |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: LengthUnitEnum
description: Units of length, ranging from micrometers to meters.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  um:
    text: um
    meaning: UO:0000017
  mm:
    text: mm
    meaning: UO:0000016
  cm:
    text: cm
    meaning: UO:0000015
  meter:
    text: meter
    meaning: UO:0000008
    aliases:
    - m

```
</details>

</div>