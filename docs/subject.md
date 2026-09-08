---
search:
  boost: 5.0
---

# Slot: subject 


_Organism identity and biological attributes of the tracked subjects._



<div data-search-exclude markdown="1">



URI: [BeStMeta:subject](https://w3id.org/BeStMeta/subject)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subject](Subject.md) |
| Domain Of | [ExperimentalConditions](ExperimentalConditions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:subject |
| native | BeStMeta:subject |




## LinkML Source

<details>
```yaml
name: subject
description: Organism identity and biological attributes of the tracked subjects.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- ExperimentalConditions
range: Subject
required: true
inlined: true

```
</details></div>