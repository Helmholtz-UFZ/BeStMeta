---
search:
  boost: 5.0
---

# Slot: color_mode 


_Color mode of the recorded video. Affects tracking algorithm behavior and file size._



<div data-search-exclude markdown="1">



URI: [bstm:color_mode](bstm:color_mode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ColorModeEnum](ColorModeEnum.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:color_mode |
| native | bstm:color_mode |




## LinkML Source

<details>
```yaml
name: color_mode
description: Color mode of the recorded video. Affects tracking algorithm behavior
  and file size.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- AcquisitionParameters
range: ColorModeEnum
required: false

```
</details></div>