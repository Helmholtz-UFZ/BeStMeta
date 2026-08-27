---
search:
  boost: 5.0
---

# Slot: statistical_software_version 


_Version string of the software used for statistical analysis._



<div data-search-exclude markdown="1">



URI: [bstm:statistical_software_version](bstm:statistical_software_version)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:statistical_software_version |
| native | bstm:statistical_software_version |
| exact | AFR:0001700 |




## LinkML Source

<details>
```yaml
name: statistical_software_version
description: Version string of the software used for statistical analysis.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0001700
rank: 1000
domain_of:
- StatisticalAnalysis
range: string
required: false
recommended: true

```
</details></div>