---
search:
  boost: 2.0
---


# Enum: WellPlateFormatEnum 




_Type of well plate used in a closed box system._



<div data-search-exclude markdown="1">

URI: [BeStMeta:WellPlateFormatEnum](https://w3id.org/BeStMeta/WellPlateFormatEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| well_6 | None | 6-well plate |
| well_12 | None | 12-well plate |
| well_24 | None | 24-well plate |
| well_48 | None | 48-well plate |
| well_96 | None | 96-well plate |
| well_384 | None | 384-well plate |
| other | None | Plate format not covered by other enum values |




## Slots

| Name | Description |
| ---  | --- |
| [well_plate_format](well_plate_format.md) | Format of the multi-well plate used in a closed-box imaging system (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: WellPlateFormatEnum
description: Type of well plate used in a closed box system.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  well_6:
    text: well_6
    description: 6-well plate.
  well_12:
    text: well_12
    description: 12-well plate.
  well_24:
    text: well_24
    description: 24-well plate.
  well_48:
    text: well_48
    description: 48-well plate.
  well_96:
    text: well_96
    description: 96-well plate.
  well_384:
    text: well_384
    description: 384-well plate.
  other:
    text: other
    description: Plate format not covered by other enum values.

```
</details>

</div>