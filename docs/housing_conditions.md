---
search:
  boost: 5.0
---

# Slot: housing_conditions 


_Free-text description of animal housing conditions prior to assay._



<div data-search-exclude markdown="1">



URI: [BeStMeta:housing_conditions](https://w3id.org/BeStMeta/housing_conditions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |  no  |
| [Manipulation](Manipulation.md) | Treatment and chemical exposure information decribing pharmacological, toxico... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Subject](Subject.md), [Manipulation](Manipulation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:housing_conditions |
| native | BeStMeta:housing_conditions |
| exact | XCO:0000033 |




## LinkML Source

<details>
```yaml
name: housing_conditions
description: Free-text description of animal housing conditions prior to assay.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- XCO:0000033
rank: 1000
domain_of:
- Subject
- Manipulation
range: string
required: false

```
</details></div>