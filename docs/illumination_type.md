---
search:
  boost: 5.0
---

# Slot: illumination_type 


_Type of illumination used during recording._



<div data-search-exclude markdown="1">



URI: [bstm:illumination_type](bstm:illumination_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IlluminationTypeEnum](IlluminationTypeEnum.md) |
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
| self | bstm:illumination_type |
| native | bstm:illumination_type |
| exact | MIxS:0000769 |




## LinkML Source

<details>
```yaml
name: illumination_type
description: Type of illumination used during recording.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- MIxS:0000769
rank: 1000
domain_of:
- AcquisitionParameters
range: IlluminationTypeEnum
required: false
recommended: true

```
</details></div>