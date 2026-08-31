---
search:
  boost: 5.0
---

# Slot: camera_model 


_Full manufacturer model name of the camera._



<div data-search-exclude markdown="1">



URI: [BeStMeta:camera_model](https://w3id.org/BeStMeta/camera_model)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VideoHardware](VideoHardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [VideoHardware](VideoHardware.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| Basler acA1300-60gc |
| Logitech C920 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:camera_model |
| native | BeStMeta:camera_model |




## LinkML Source

<details>
```yaml
name: camera_model
description: Full manufacturer model name of the camera.
examples:
- value: Basler acA1300-60gc
- value: Logitech C920
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- VideoHardware
range: string
required: true

```
</details></div>