---
search:
  boost: 5.0
---

# Slot: effect_size_measure 


_Effect size measure reported to quantify the magnitude of observed effects or associations._



<div data-search-exclude markdown="1">



URI: [BeStMeta:effect_size_measure](https://w3id.org/BeStMeta/effect_size_measure)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StatisticalAnalysis](StatisticalAnalysis.md) | Information describing the statistical analysis of behavioral data, including... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StatisticalAnalysis](StatisticalAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| Cohen's d |
| Hedges' g |
| eta-squared |
| partial eta-squared |
| odds ratio |
| Pearson's r |
| Spearman's rho |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:effect_size_measure |
| native | BeStMeta:effect_size_measure |
| close | NCIT:C209463 |




## LinkML Source

<details>
```yaml
name: effect_size_measure
description: Effect size measure reported to quantify the magnitude of observed effects
  or associations.
examples:
- value: Cohen's d
- value: Hedges' g
- value: eta-squared
- value: partial eta-squared
- value: odds ratio
- value: Pearson's r
- value: Spearman's rho
from_schema: https://w3id.org/bestmeta/schema
close_mappings:
- NCIT:C209463
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>