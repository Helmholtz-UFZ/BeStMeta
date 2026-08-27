---
search:
  boost: 5.0
---

# Slot: n_individuals_tracked_per_arena 


_Number of individuals actually tracked in a single arena or trial._



<div data-search-exclude markdown="1">



URI: [bstm:n_individuals_tracked_per_arena](bstm:n_individuals_tracked_per_arena)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [TrackingAnalysis](TrackingAnalysis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |








## Notes

* Can be derived from ExperimentalConditions/n_individuals_per_arena.
* Report explicitly if fewer animals were successfully tracked.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:n_individuals_tracked_per_arena |
| native | bstm:n_individuals_tracked_per_arena |
| exact | BeStMeta:n_individuals_per_arena |




## LinkML Source

<details>
```yaml
name: n_individuals_tracked_per_arena
description: Number of individuals actually tracked in a single arena or trial.
notes:
- Can be derived from ExperimentalConditions/n_individuals_per_arena.
- Report explicitly if fewer animals were successfully tracked.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- BeStMeta:n_individuals_per_arena
rank: 1000
domain_of:
- TrackingAnalysis
range: integer
required: false
recommended: true

```
</details></div>