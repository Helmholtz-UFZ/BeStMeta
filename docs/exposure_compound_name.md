---
search:
  boost: 5.0
---

# Slot: exposure_compound_name 


_Name of the chemical, drug, or substance used in the treatment or exposure._



<div data-search-exclude markdown="1">



URI: [BeStMeta:exposure_compound_name](https://w3id.org/BeStMeta/exposure_compound_name)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:exposure_compound_name |
| native | BeStMeta:exposure_compound_name |
| exact | EDAM.DATA:0997 |




## LinkML Source

<details>
```yaml
name: exposure_compound_name
description: Name of the chemical, drug, or substance used in the treatment or exposure.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- EDAM.DATA:0997
rank: 1000
domain_of:
- Manipulation
range: string
required: false
recommended: true

```
</details></div>