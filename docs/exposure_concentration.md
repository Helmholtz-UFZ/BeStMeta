---
search:
  boost: 5.0
---

# Slot: exposure_concentration 


_Nominal exposure concentration (numeric value only; use unit field)._



<div data-search-exclude markdown="1">



URI: [BeStMeta:exposure_concentration](https://w3id.org/BeStMeta/exposure_concentration)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manipulation](Manipulation.md) | Treatment and chemical exposure information decribing pharmacological, toxico... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Manipulation](Manipulation.md) |

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
| self | BeStMeta:exposure_concentration |
| native | BeStMeta:exposure_concentration |
| exact | EDAM.DATA:2140 |




## LinkML Source

<details>
```yaml
name: exposure_concentration
description: Nominal exposure concentration (numeric value only; use unit field).
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- EDAM.DATA:2140
rank: 1000
domain_of:
- Manipulation
range: float
required: false
recommended: true

```
</details></div>