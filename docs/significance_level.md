---
search:
  boost: 5.0
---

# Slot: significance_level 


_Significance threshold used for hypothesis testing (e.g., alpha)._



<div data-search-exclude markdown="1">



URI: [BeStMeta:significance_level](https://w3id.org/BeStMeta/significance_level)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StatisticalAnalysis](StatisticalAnalysis.md) | Information describing the statistical analysis of behavioral data, including... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [StatisticalAnalysis](StatisticalAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 0 |
| Maximum Value | 1 |











## Examples

| Value |
| --- |
| 0.05 |
| 0.01 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:significance_level |
| native | BeStMeta:significance_level |
| exact | NCIT:C41265 |




## LinkML Source

<details>
```yaml
name: significance_level
description: Significance threshold used for hypothesis testing (e.g., alpha).
examples:
- value: '0.05'
- value: '0.01'
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- NCIT:C41265
rank: 1000
domain_of:
- StatisticalAnalysis
range: float
required: false
recommended: true
minimum_value: 0
maximum_value: 1

```
</details></div>