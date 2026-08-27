---
search:
  boost: 5.0
---

# Slot: statistical_models 


_Statistical models used to analyse behavioral endpoints._



<div data-search-exclude markdown="1">



URI: [bstm:statistical_models](bstm:statistical_models)
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
| linear mixed-effects model |
| generalized linear model |
| generalized additive model |
| Cox proportional hazards model |
| logistic regression |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:statistical_models |
| native | bstm:statistical_models |
| exact | STATO:0000107 |




## LinkML Source

<details>
```yaml
name: statistical_models
description: Statistical models used to analyse behavioral endpoints.
examples:
- value: linear mixed-effects model
- value: generalized linear model
- value: generalized additive model
- value: Cox proportional hazards model
- value: logistic regression
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- STATO:0000107
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>