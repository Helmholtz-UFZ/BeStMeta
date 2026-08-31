---
search:
  boost: 5.0
---

# Slot: statistical_tests 


_Statistical tests applied to behavioral endpoints for hypothesis testing or inference._



<div data-search-exclude markdown="1">



URI: [BeStMeta:statistical_tests](https://w3id.org/BeStMeta/statistical_tests)
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
| Student's t-test |
| Mann-Whitney U test |
| one-way ANOVA |
| two-way ANOVA |
| repeated-measures ANOVA |
| Kruskal-Wallis test |
| Wilcoxon signed-rank test |
| Chi-square test |

## Notes

* Multiple tests may be listed if different endpoints were analysed with different methods.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:statistical_tests |
| native | BeStMeta:statistical_tests |
| exact | NCIT:C53228 |




## LinkML Source

<details>
```yaml
name: statistical_tests
description: Statistical tests applied to behavioral endpoints for hypothesis testing
  or inference.
notes:
- Multiple tests may be listed if different endpoints were analysed with different
  methods.
examples:
- value: Student's t-test
- value: Mann-Whitney U test
- value: one-way ANOVA
- value: two-way ANOVA
- value: repeated-measures ANOVA
- value: Kruskal-Wallis test
- value: Wilcoxon signed-rank test
- value: Chi-square test
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- NCIT:C53228
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>