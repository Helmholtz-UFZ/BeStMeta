---
search:
  boost: 5.0
---

# Slot: compute_hardware 


_Primary compute hardware used for tracking and analysis. Include model information when available._



<div data-search-exclude markdown="1">



URI: [BeStMeta:compute_hardware](https://w3id.org/BeStMeta/compute_hardware)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| GPU (NVIDIA RTX 3090) |
| GPU (NVIDIA A100 80GB) |
| CPU (Intel Xeon Gold 6248) |
| CPU (AMD Ryzen 9 7950X) |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:compute_hardware |
| native | BeStMeta:compute_hardware |




## LinkML Source

<details>
```yaml
name: compute_hardware
description: Primary compute hardware used for tracking and analysis. Include model
  information when available.
examples:
- value: GPU (NVIDIA RTX 3090)
- value: GPU (NVIDIA A100 80GB)
- value: CPU (Intel Xeon Gold 6248)
- value: CPU (AMD Ryzen 9 7950X)
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: string
required: false
recommended: true
multivalued: true

```
</details></div>