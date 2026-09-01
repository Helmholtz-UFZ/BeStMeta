---
search:
  boost: 5.0
---

# Slot: recording_duration 


_Total duration of the video recording in ISO 8601 duration format._



<div data-search-exclude markdown="1">



URI: [BeStMeta:recording_duration](https://w3id.org/BeStMeta/recording_duration)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Duration](Duration.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| PT30M |
| PT1H15M30S |
| PT45S |

## Notes

* Use ISO 8601 duration format.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:recording_duration |
| native | BeStMeta:recording_duration |
| exact | AFR:0000951 |
| close | schema:duration |




## LinkML Source

<details>
```yaml
name: recording_duration
description: Total duration of the video recording in ISO 8601 duration format.
notes:
- Use ISO 8601 duration format.
examples:
- value: PT30M
  description: 30 minutes
- value: PT1H15M30S
  description: 1 hour, 15 minutes, 30 seconds
- value: PT45S
  description: 45 seconds
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFR:0000951
close_mappings:
- schema:duration
rank: 1000
domain_of:
- AcquisitionParameters
range: duration
required: true

```
</details></div>