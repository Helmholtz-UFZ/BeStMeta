---
search:
  boost: 5.0
---

# Slot: preprocessing_steps 


_Preprocessing steps applied to video before tracking to enhance quality or isolate features._



<div data-search-exclude markdown="1">



URI: [bstm:preprocessing_steps](bstm:preprocessing_steps)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PreprocessingStepEnum](PreprocessingStepEnum.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:preprocessing_steps |
| native | bstm:preprocessing_steps |




## LinkML Source

<details>
```yaml
name: preprocessing_steps
description: Preprocessing steps applied to video before tracking to enhance quality
  or isolate features.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: PreprocessingStepEnum
required: false
recommended: true
multivalued: true

```
</details></div>