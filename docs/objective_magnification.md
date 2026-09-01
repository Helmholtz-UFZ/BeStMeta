---
search:
  boost: 5.0
---

# Slot: objective_magnification 


_Magnification of microscope objective (if applicable)._



<div data-search-exclude markdown="1">



URI: [BeStMeta:objective_magnification](https://w3id.org/BeStMeta/objective_magnification)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VideoHardware](VideoHardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [VideoHardware](VideoHardware.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |









## Examples

| Value |
| --- |
| 4 |
| 10 |



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| ome_element | Objective/Magnification |




### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:objective_magnification |
| native | BeStMeta:objective_magnification |




## LinkML Source

<details>
```yaml
name: objective_magnification
annotations:
  ome_element:
    tag: ome_element
    value: Objective/Magnification
description: Magnification of microscope objective (if applicable).
examples:
- value: '4'
- value: '10'
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- VideoHardware
range: float
required: false
recommended: true

```
</details></div>