---
search:
  boost: 5.0
---

# Slot: tracking_software_name 


_Name of the software used for tracking._



<div data-search-exclude markdown="1">



URI: [bstm:tracking_software_name](bstm:tracking_software_name)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:tracking_software_name |
| native | bstm:tracking_software_name |
| exact | AFR:0002802 |




## LinkML Source

<details>
```yaml
name: tracking_software_name
description: Name of the software used for tracking.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0002802
rank: 1000
domain_of:
- TrackingAnalysis
range: string
required: false
recommended: true

```
</details></div>