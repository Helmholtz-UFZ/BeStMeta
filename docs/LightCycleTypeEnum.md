---
search:
  boost: 2.0
---


# Enum: LightCycleTypeEnum 




_Standardized light-dark cycle types._



<div data-search-exclude markdown="1">

URI: [bstm:LightCycleTypeEnum](bstm:LightCycleTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| cyclic_ld | None | Cyclic light-dark cycle, e |
| constant_light | None | Continuous light |
| constant_dark | None | Continuous darkness |
| other | None | Other or non-standard light regime |




## Slots

| Name | Description |
| ---  | --- |
| [light_cycle_type](light_cycle_type.md) | Standardized category of the light-dark cycle |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: LightCycleTypeEnum
description: Standardized light-dark cycle types.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  cyclic_ld:
    text: cyclic_ld
    description: Cyclic light-dark cycle, e.g. 14:10 LD.
  constant_light:
    text: constant_light
    description: Continuous light.
  constant_dark:
    text: constant_dark
    description: Continuous darkness.
  other:
    text: other
    description: Other or non-standard light regime.

```
</details>

</div>