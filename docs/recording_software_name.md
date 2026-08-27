---
search:
  boost: 5.0
---

# Slot: recording_software_name 


_Name of the software used to record the video._



<div data-search-exclude markdown="1">



URI: [bstm:recording_software_name](bstm:recording_software_name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:recording_software_name |
| native | bstm:recording_software_name |
| exact | AFR:0002802 |




## LinkML Source

<details>
```yaml
name: recording_software_name
description: Name of the software used to record the video.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0002802
rank: 1000
domain_of:
- AcquisitionParameters
range: string
required: true

```
</details></div>