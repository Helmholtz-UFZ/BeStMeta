---
search:
  boost: 5.0
---

# Slot: gain 


_Camera gain setting at the time of recording._



<div data-search-exclude markdown="1">



URI: [bstm:gain](bstm:gain)
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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:gain |
| native | bstm:gain |
| exact | AFQ:0000201 |




## LinkML Source

<details>
```yaml
name: gain
description: Camera gain setting at the time of recording.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- AFQ:0000201
rank: 1000
domain_of:
- AcquisitionParameters
range: string
required: false

```
</details></div>