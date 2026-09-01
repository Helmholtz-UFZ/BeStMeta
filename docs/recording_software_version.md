---
search:
  boost: 5.0
---

# Slot: recording_software_version 


_Version string of the recording software._



<div data-search-exclude markdown="1">



URI: [BeStMeta:recording_software_version](https://w3id.org/BeStMeta/recording_software_version)
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
| self | BeStMeta:recording_software_version |
| native | BeStMeta:recording_software_version |
| exact | AFR:0001700 |




## LinkML Source

<details>
```yaml
name: recording_software_version
description: Version string of the recording software.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0001700
rank: 1000
domain_of:
- AcquisitionParameters
range: string
required: true

```
</details></div>