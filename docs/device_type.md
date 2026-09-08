---
search:
  boost: 5.0
---

# Slot: device_type 


_Indicates the category of imaging system used; determines which additional hardware or tracking fields are required or recommended._



<div data-search-exclude markdown="1">



URI: [BeStMeta:device_type](https://w3id.org/BeStMeta/device_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeviceTypeMixin](DeviceTypeMixin.md) | Reusable slot bundle providing device_type, allowing multiple classes (e |  no  |
| [Hardware](Hardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |  no  |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DeviceTypeEnum](DeviceTypeEnum.md) |
| Domain Of | [DeviceTypeMixin](DeviceTypeMixin.md) |

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
| self | BeStMeta:device_type |
| native | BeStMeta:device_type |




## LinkML Source

<details>
```yaml
name: device_type
description: Indicates the category of imaging system used; determines which additional
  hardware or tracking fields are required or recommended.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- DeviceTypeMixin
range: DeviceTypeEnum
required: true

```
</details></div>