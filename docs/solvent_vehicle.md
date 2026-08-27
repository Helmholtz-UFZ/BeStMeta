---
search:
  boost: 5.0
---

# Slot: solvent_vehicle 


_Solvent or vehicle used to dissolve the test substance._



<div data-search-exclude markdown="1">



URI: [bstm:solvent_vehicle](bstm:solvent_vehicle)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ExperimentalConditions](ExperimentalConditions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| DMSO 0.01% |
| ethanol 0.1% |
| water |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:solvent_vehicle |
| native | bstm:solvent_vehicle |




## LinkML Source

<details>
```yaml
name: solvent_vehicle
description: Solvent or vehicle used to dissolve the test substance.
examples:
- value: DMSO 0.01%
- value: ethanol 0.1%
- value: water
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- ExperimentalConditions
range: string
required: false

```
</details></div>