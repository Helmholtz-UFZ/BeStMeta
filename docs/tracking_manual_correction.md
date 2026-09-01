---
search:
  boost: 5.0
---

# Slot: tracking_manual_correction 


_Whether tracking results were manually reviewed, corrected, or curated after automated tracking._



<div data-search-exclude markdown="1">



URI: [BeStMeta:tracking_manual_correction](https://w3id.org/BeStMeta/tracking_manual_correction)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |









## Examples

| Value |
| --- |
| true |
| false |

## Notes

* Use true if outputs were manually curated, corrected, or quality-checked by a human after automated tracking.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:tracking_manual_correction |
| native | BeStMeta:tracking_manual_correction |




## LinkML Source

<details>
```yaml
name: tracking_manual_correction
description: Whether tracking results were manually reviewed, corrected, or curated
  after automated tracking.
notes:
- Use true if outputs were manually curated, corrected, or quality-checked by a human
  after automated tracking.
examples:
- value: 'true'
- value: 'false'
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- TrackingAnalysis
range: boolean
required: false
recommended: true

```
</details></div>