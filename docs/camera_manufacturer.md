---
search:
  boost: 5.0
---

# Slot: camera_manufacturer 


_Manufacturer of the camera._



<div data-search-exclude markdown="1">



URI: [bstm:camera_manufacturer](bstm:camera_manufacturer)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:camera_manufacturer |
| native | bstm:camera_manufacturer |
| exact | schema:manufacturer |




## LinkML Source

<details>
```yaml
name: camera_manufacturer
description: Manufacturer of the camera.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- schema:manufacturer
rank: 1000
domain_of:
- VideoHardware
range: string
required: true

```
</details></div>