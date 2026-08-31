---
search:
  boost: 5.0
---

# Slot: plate_well_count 


_Number of wells in the multiwell plate._



<div data-search-exclude markdown="1">



URI: [BeStMeta:plate_well_count](https://w3id.org/BeStMeta/plate_well_count)
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
| Recommended | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 1 |











## Examples

| Value |
| --- |
| 24 |
| 96 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:plate_well_count |
| native | BeStMeta:plate_well_count |
| exact | AFR:0002231 |




## LinkML Source

<details>
```yaml
name: plate_well_count
description: Number of wells in the multiwell plate.
examples:
- value: '24'
- value: '96'
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0002231
rank: 1000
domain_of:
- Experiment
range: integer
required: false
recommended: true
minimum_value: 1

```
</details></div>