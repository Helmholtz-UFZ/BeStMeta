---
search:
  boost: 5.0
---

# Slot: sex 


_Biological sex of the tracked organism(s)._



<div data-search-exclude markdown="1">



URI: [BeStMeta:sex](https://w3id.org/BeStMeta/sex)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SexEnum](SexEnum.md) |
| Domain Of | [Subject](Subject.md) |

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
| self | BeStMeta:sex |
| native | BeStMeta:sex |
| exact | PATO:0000047 |




## LinkML Source

<details>
```yaml
name: sex
description: Biological sex of the tracked organism(s).
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- PATO:0000047
rank: 1000
domain_of:
- Subject
range: SexEnum
required: false
recommended: true

```
</details></div>