---
search:
  boost: 5.0
---

# Slot: bit_depth 


_Bit depth per pixel channel of the recorded video._



<div data-search-exclude markdown="1">



URI: [bstm:bit_depth](bstm:bit_depth)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [AcquisitionParameters](AcquisitionParameters.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 8 |
| 16 |

## Notes

* Common values are 8-bit and 16-bit.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:bit_depth |
| native | bstm:bit_depth |
| exact | ebucore:bitDepth |




## LinkML Source

<details>
```yaml
name: bit_depth
description: Bit depth per pixel channel of the recorded video.
notes:
- Common values are 8-bit and 16-bit.
examples:
- value: '8'
- value: '16'
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- ebucore:bitDepth
rank: 1000
domain_of:
- AcquisitionParameters
range: integer
required: false

```
</details></div>