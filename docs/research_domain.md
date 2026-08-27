---
search:
  boost: 5.0
---

# Slot: research_domain 


_Primary research domain of this study._



<div data-search-exclude markdown="1">



URI: [bstm:research_domain](bstm:research_domain)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:research_domain |
| native | bstm:research_domain |
| exact | dcterms:subject |




## LinkML Source

<details>
```yaml
name: research_domain
description: Primary research domain of this study.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- dcterms:subject
rank: 1000
domain_of:
- VTADataset
range: string
required: false
recommended: true

```
</details></div>