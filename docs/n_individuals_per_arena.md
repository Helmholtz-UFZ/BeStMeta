---
search:
  boost: 5.0
---

# Slot: n_individuals_per_arena 


_Number of individuals tested simultaneously in the arena._



<div data-search-exclude markdown="1">



URI: [BeStMeta:n_individuals_per_arena](https://w3id.org/BeStMeta/n_individuals_per_arena)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Defines experimental context in which the subjects were studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 1 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:n_individuals_per_arena |
| native | BeStMeta:n_individuals_per_arena |




## LinkML Source

<details>
```yaml
name: n_individuals_per_arena
description: Number of individuals tested simultaneously in the arena.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- Experiment
range: integer
required: true
minimum_value: 1

```
</details></div>