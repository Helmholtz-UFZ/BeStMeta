---
search:
  boost: 5.0
---

# Slot: sample_size_analysis 


_Sample size or power analysis method, software, or justification used before the study._



<div data-search-exclude markdown="1">



URI: [bstm:sample_size_analysis](bstm:sample_size_analysis)
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
| power analysis in G*Power |
| calculated using alpha=0.05 and power=0.8 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:sample_size_analysis |
| native | bstm:sample_size_analysis |
| exact | NCIT:C115467 |




## LinkML Source

<details>
```yaml
name: sample_size_analysis
description: Sample size or power analysis method, software, or justification used
  before the study.
examples:
- value: power analysis in G*Power
- value: calculated using alpha=0.05 and power=0.8
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- NCIT:C115467
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>