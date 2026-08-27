---
search:
  boost: 5.0
---

# Slot: treatment_name 


_Short label identifying the experimental treatment group, condition, or regimen._



<div data-search-exclude markdown="1">



URI: [bstm:treatment_name](bstm:treatment_name)
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
| Recommended | Yes |









## Examples

| Value |
| --- |
| diazepam 1 mg/kg |
| atrazine 10 ug/L |
| vehicle control |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:treatment_name |
| native | bstm:treatment_name |
| exact | NCIT:C82542 |




## LinkML Source

<details>
```yaml
name: treatment_name
description: Short label identifying the experimental treatment group, condition,
  or regimen.
examples:
- value: diazepam 1 mg/kg
- value: atrazine 10 ug/L
- value: vehicle control
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- NCIT:C82542
rank: 1000
domain_of:
- ExperimentalConditions
range: string
required: false
recommended: true

```
</details></div>