---
search:
  boost: 5.0
---

# Slot: tracking_software_type 


_Indicates whether the tracking analysis was performed using a custom software or a standard package or software_



<div data-search-exclude markdown="1">



URI: [bstm:tracking_software_type](bstm:tracking_software_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TrackingSoftwareTypeEnum](TrackingSoftwareTypeEnum.md) |
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
| self | bstm:tracking_software_type |
| native | bstm:tracking_software_type |




## LinkML Source

<details>
```yaml
name: tracking_software_type
description: Indicates whether the tracking analysis was performed using a custom
  software or a standard package or software
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: TrackingSoftwareTypeEnum
required: false
recommended: true

```
</details></div>