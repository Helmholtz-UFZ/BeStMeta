---
search:
  boost: 5.0
---

# Slot: treatment_name 


_Short label identifying the experimental treatment group, condition, or regimen._



<div data-search-exclude markdown="1">



URI: [BeStMeta:treatment_name](https://w3id.org/BeStMeta/treatment_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manipulation](Manipulation.md) | Treatment and chemical exposure information decribing pharmacological, toxico... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Manipulation](Manipulation.md) |

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
| self | BeStMeta:treatment_name |
| native | BeStMeta:treatment_name |
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
- Manipulation
range: string
required: false
recommended: true

```
</details></div>