---
search:
  boost: 5.0
---

# Slot: microscope_type 


_Microscope configuration according to the OME microscope type classification._



<div data-search-exclude markdown="1">



URI: [bstm:microscope_type](bstm:microscope_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VideoHardware](VideoHardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MicroscopeTypeEnum](MicroscopeTypeEnum.md) |
| Domain Of | [VideoHardware](VideoHardware.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:microscope_type |
| native | bstm:microscope_type |
| exact | OME:Type |




## LinkML Source

<details>
```yaml
name: microscope_type
description: Microscope configuration according to the OME microscope type classification.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- OME:Type
rank: 1000
domain_of:
- VideoHardware
range: MicroscopeTypeEnum
required: false

```
</details></div>