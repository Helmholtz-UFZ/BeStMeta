---
search:
  boost: 5.0
---

# Slot: exposure_compound_chebi_id 


_ChEBI identifier for the test substance._



<div data-search-exclude markdown="1">



URI: [bstm:exposure_compound_chebi_id](bstm:exposure_compound_chebi_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ExperimentalConditions](ExperimentalConditions.md) |

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
| self | bstm:exposure_compound_chebi_id |
| native | bstm:exposure_compound_chebi_id |
| exact | EDAM-DATA:1174 |




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
- EDAM-DATA:1174
rank: 1000
domain_of:
- ExperimentalConditions
range: string
required: false
recommended: true
pattern: ^CHEBI:\d+$

```
</details></div>