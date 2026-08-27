---
search:
  boost: 5.0
---

# Slot: endpoint_definitions 


_Definitions and calculation criteria used for behavioral endpoints, including thresholds, zone boundaries, event definitions, and other parameters required to reproduce endpoint calculations._



<div data-search-exclude markdown="1">



URI: [bstm:endpoint_definitions](bstm:endpoint_definitions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| Freezing defined as speed < 1 mm/s for ≥ 1 s |
| Center zone defined as central 50% of arena area |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:endpoint_definitions |
| native | bstm:endpoint_definitions |




## LinkML Source

<details>
```yaml
name: endpoint_definitions
description: Definitions and calculation criteria used for behavioral endpoints, including
  thresholds, zone boundaries, event definitions, and other parameters required to
  reproduce endpoint calculations.
examples:
- value: Freezing defined as speed < 1 mm/s for ≥ 1 s
- value: Center zone defined as central 50% of arena area
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>