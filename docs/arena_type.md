---
search:
  boost: 5.0
---

# Slot: arena_type 


_Type of the test arena, e.g., open field, multiwell plate or elevated plus maze._



<div data-search-exclude markdown="1">



URI: [BeStMeta:arena_type](https://w3id.org/BeStMeta/arena_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Defines experimental context in which the subjects were studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ArenaTypeEnum](ArenaTypeEnum.md) |
| Domain Of | [Experiment](Experiment.md) |

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
| self | BeStMeta:arena_type |
| native | BeStMeta:arena_type |




## LinkML Source

<details>
```yaml
name: arena_type
description: Type of the test arena, e.g., open field, multiwell plate or elevated
  plus maze.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- Experiment
range: ArenaTypeEnum
required: false
recommended: true

```
</details></div>