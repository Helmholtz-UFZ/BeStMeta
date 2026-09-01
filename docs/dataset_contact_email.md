---
search:
  boost: 5.0
---

# Slot: dataset_contact_email 


_Contact email for the dataset maintainer._



<div data-search-exclude markdown="1">



URI: [BeStMeta:dataset_contact_email](https://w3id.org/BeStMeta/dataset_contact_email)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VTADataset](VTADataset.md) | Top-level study and provenance metadata for a VTA dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [VTADataset](VTADataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:dataset_contact_email |
| native | BeStMeta:dataset_contact_email |
| exact | schema:email |




## LinkML Source

<details>
```yaml
name: dataset_contact_email
description: Contact email for the dataset maintainer.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- schema:email
rank: 1000
domain_of:
- VTADataset
range: string
required: false
recommended: true
pattern: ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$

```
</details></div>