---
search:
  boost: 5.0
---

# Slot: strain 


_Organism strain or line_



<div data-search-exclude markdown="1">



URI: [BeStMeta:strain](https://w3id.org/BeStMeta/strain)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | BeStMeta:strain |
| native | BeStMeta:strain |
| exact | EDAM.DATA:2379 |




## LinkML Source

<details>
```yaml
name: strain
description: Organism strain or line
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- EDAM.DATA:2379
rank: 1000
domain_of:
- Subject
range: string
required: false
recommended: true

```
</details></div>