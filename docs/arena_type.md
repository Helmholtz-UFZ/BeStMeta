---
search:
  boost: 5.0
---

# Slot: arena_type 


_Type of the test arena, e.g., open field, multiwell plate or elevated plus maze._



<div data-search-exclude markdown="1">



URI: [bstm:arena_type](bstm:arena_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ArenaTypeEnum](ArenaTypeEnum.md) |
| Domain Of | [ExperimentalConditions](ExperimentalConditions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:arena_type |
| native | bstm:arena_type |




## LinkML Source

<details>
```yaml
name: arena_type
description: Type of the test arena, e.g., open field, multiwell plate or elevated
  plus maze.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- ExperimentalConditions
range: ArenaTypeEnum
required: false
recommended: true

```
</details></div>