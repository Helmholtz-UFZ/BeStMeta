---
search:
  boost: 5.0
---

# Slot: statistical_software_name 


_Name of the software used for statistical analysis._



<div data-search-exclude markdown="1">



URI: [BeStMeta:statistical_software_name](https://w3id.org/BeStMeta/statistical_software_name)
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
| R |
| GraphPad Prism |
| SPSS |
| SAS |
| Stata |

## Notes

* Use a software/package name rather than a software class or workflow.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:statistical_software_name |
| native | BeStMeta:statistical_software_name |
| exact | AFR:0002802 |




## LinkML Source

<details>
```yaml
name: statistical_software_name
description: Name of the software used for statistical analysis.
notes:
- Use a software/package name rather than a software class or workflow.
examples:
- value: R
- value: GraphPad Prism
- value: SPSS
- value: SAS
- value: Stata
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0002802
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true

```
</details></div>