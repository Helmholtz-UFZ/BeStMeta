---
search:
  boost: 5.0
---

# Slot: multiple_testing_correction 


_Procedure used to correct for multiple comparisons (if more than one hypothesis was tested).  Include the name of the method and any parameters (e.g., false‑discovery‑rate level)._



<div data-search-exclude markdown="1">



URI: [bstm:multiple_testing_correction](bstm:multiple_testing_correction)
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









## Examples

| Value |
| --- |
| Benjamini‑Hochberg FDR (q = 0.05) |
| Bonferroni (α / n = 0.001) |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:multiple_testing_correction |
| native | bstm:multiple_testing_correction |
| exact | OBI:0200089 |




## LinkML Source

<details>
```yaml
name: multiple_testing_correction
description: Procedure used to correct for multiple comparisons (if more than one
  hypothesis was tested).  Include the name of the method and any parameters (e.g.,
  false‑discovery‑rate level).
examples:
- value: Benjamini‑Hochberg FDR (q = 0.05)
- value: Bonferroni (α / n = 0.001)
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- OBI:0200089
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true

```
</details></div>