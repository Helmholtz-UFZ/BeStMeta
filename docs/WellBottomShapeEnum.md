---
search:
  boost: 2.0
---


# Enum: WellBottomShapeEnum 




_Geometric bottom shape of the wells of a multiwell plate._



<div data-search-exclude markdown="1">

URI: [BeStMeta:WellBottomShapeEnum](https://w3id.org/BeStMeta/WellBottomShapeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| flat_bottom | None | Flat well bottom; also called F-bottom |
| u_bottom | None | Rounded well bottom; also called round-bottom |
| v_bottom | None | V-shaped or conical well bottom |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [well_shape_bottom](well_shape_bottom.md) | Geometric bottom shape of the wells of a multiwell plate |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: WellBottomShapeEnum
description: Geometric bottom shape of the wells of a multiwell plate.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  flat_bottom:
    text: flat_bottom
    description: Flat well bottom; also called F-bottom.
  u_bottom:
    text: u_bottom
    description: Rounded well bottom; also called round-bottom.
  v_bottom:
    text: v_bottom
    description: V-shaped or conical well bottom.
  other:
    text: other

```
</details>

</div>