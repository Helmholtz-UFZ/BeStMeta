---
search:
  boost: 2.0
---


# Enum: DevelopmentUnitEnum 




_Units of time used to express the developmental age of an organism._



<div data-search-exclude markdown="1">

URI: [bstm:DevelopmentUnitEnum](bstm:DevelopmentUnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| hpf | None | Hours post fertilization |
| dpf | None | Days post fertilization |
| days | UO:0000033 |  |
| weeks | UO:0000034 |  |
| months | UO:0000035 |  |
| years | UO:0000036 |  |




## Slots

| Name | Description |
| ---  | --- |
| [developmental_stage_unit](developmental_stage_unit.md) | Unit for developmental stage value of the tracked organism(s) |
| [age_unit](age_unit.md) | Age unit of the tracked organism(s) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: DevelopmentUnitEnum
description: Units of time used to express the developmental age of an organism.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  hpf:
    text: hpf
    description: Hours post fertilization
  dpf:
    text: dpf
    description: Days post fertilization
  days:
    text: days
    meaning: UO:0000033
  weeks:
    text: weeks
    meaning: UO:0000034
  months:
    text: months
    meaning: UO:0000035
  years:
    text: years
    meaning: UO:0000036

```
</details>

</div>