---
search:
  boost: 5.0
---

# Slot: exposure_compound_chebi_id 


_ChEBI identifier for the test substance._



<div data-search-exclude markdown="1">



URI: [BeStMeta:exposure_compound_chebi_id](https://w3id.org/BeStMeta/exposure_compound_chebi_id)
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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^CHEBI:\d+$` |











## Examples

| Value |
| --- |
| CHEBI:15930 |
| CHEBI:49575 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:exposure_compound_chebi_id |
| native | BeStMeta:exposure_compound_chebi_id |
| exact | EDAM.DATA:1174 |




## LinkML Source

<details>
```yaml
name: exposure_compound_chebi_id
description: ChEBI identifier for the test substance.
examples:
- value: CHEBI:15930
- value: CHEBI:49575
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- EDAM.DATA:1174
rank: 1000
domain_of:
- Manipulation
range: string
required: false
recommended: true
pattern: ^CHEBI:\d+$

```
</details></div>