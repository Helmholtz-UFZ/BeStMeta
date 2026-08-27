---
search:
  boost: 5.0
---

# Slot: recording_end_datetime 


_Date and time at which acquisition of the video recording ended._



<div data-search-exclude markdown="1">



URI: [bstm:recording_end_datetime](bstm:recording_end_datetime)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

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
| self | bstm:recording_end_datetime |
| native | bstm:recording_end_datetime |




## LinkML Source

<details>
```yaml
name: recording_end_datetime
description: Date and time at which acquisition of the video recording ended.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- AcquisitionParameters
range: datetime
required: false
recommended: true

```
</details></div>