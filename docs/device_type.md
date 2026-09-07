---
search:
  boost: 5.0
---

# Slot: device_type 


_Indicates the category of imaging system used; determines which additional hardware fields are required or recommended._



<div data-search-exclude markdown="1">



URI: [BeStMeta:device_type](https://w3id.org/BeStMeta/device_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hardware](Hardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DeviceTypeEnum](DeviceTypeEnum.md) |
| Domain Of | [Hardware](Hardware.md) |

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
  hardware fields are required or recommended.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- Hardware
range: DeviceTypeEnum
required: true

```
</details></div>