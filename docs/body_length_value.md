---
search:
  boost: 5.0
---

# Slot: body_length_value 


_Body length numeric value of the tracked organism(s)._



<div data-search-exclude markdown="1">



URI: [BeStMeta:body_length_value](https://w3id.org/BeStMeta/body_length_value)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
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
| self | BeStMeta:body_length_value |
| native | BeStMeta:body_length_value |
| close | EFO:0004339, MESH:D049628 |




## LinkML Source

<details>
```yaml
name: body_length_value
description: Body length numeric value of the tracked organism(s).
from_schema: https://w3id.org/bestmeta/schema
close_mappings:
- EFO:0004339
- MESH:D049628
rank: 1000
domain_of:
- Subject
range: float
required: false
recommended: true

```
</details></div>