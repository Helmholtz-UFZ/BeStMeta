---
search:
  boost: 5.0
---

# Slot: exposure_route 


_Route of chemical or treatment administration._



<div data-search-exclude markdown="1">



URI: [bstm:exposure_route](bstm:exposure_route)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExposureRouteEnum](ExposureRouteEnum.md) |
| Domain Of | [ExperimentalConditions](ExperimentalConditions.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bstm:exposure_route |
| native | bstm:exposure_route |
| exact | MESH:D004333 |




## LinkML Source

<details>
```yaml
name: exposure_route
description: Route of chemical or treatment administration.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- MESH:D004333
rank: 1000
domain_of:
- ExperimentalConditions
range: ExposureRouteEnum
required: false

```
</details></div>