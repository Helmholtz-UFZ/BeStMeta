---
search:
  boost: 5.0
---

# Slot: subject_type 


_Indicates whether the subject being tracked is a whole organism or a cell/cell culture; determines which biological identity fields are applicable._



<div data-search-exclude markdown="1">



URI: [BeStMeta:subject_type](https://w3id.org/BeStMeta/subject_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SubjectTypeEnum](SubjectTypeEnum.md) |
| Domain Of | [Subject](Subject.md) |

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
| self | BeStMeta:subject_type |
| native | BeStMeta:subject_type |




## LinkML Source

<details>
```yaml
name: subject_type
description: Indicates whether the subject being tracked is a whole organism or a
  cell/cell culture; determines which biological identity fields are applicable.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- Subject
range: SubjectTypeEnum
required: true

```
</details></div>