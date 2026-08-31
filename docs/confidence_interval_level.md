---
search:
  boost: 5.0
---

# Slot: confidence_interval_level 


_Confidence interval reported for statistical results._



<div data-search-exclude markdown="1">



URI: [BeStMeta:confidence_interval_level](https://w3id.org/BeStMeta/confidence_interval_level)
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
| 95% CI |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:confidence_interval_level |
| native | BeStMeta:confidence_interval_level |
| exact | STATO:0000196 |




## LinkML Source

<details>
```yaml
name: confidence_interval_level
description: Confidence interval reported for statistical results.
examples:
- value: 95% CI
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- STATO:0000196
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>