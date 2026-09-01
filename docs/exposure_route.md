---
search:
  boost: 5.0
---

# Slot: exposure_route 


_Route of chemical or treatment administration._



<div data-search-exclude markdown="1">



URI: [BeStMeta:exposure_route](https://w3id.org/BeStMeta/exposure_route)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Manipulation](Manipulation.md) | Treatment and chemical exposure information decribing pharmacological, toxico... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExposureRouteEnum](ExposureRouteEnum.md) |
| Domain Of | [Manipulation](Manipulation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:exposure_route |
| native | BeStMeta:exposure_route |
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
- Manipulation
range: ExposureRouteEnum
required: false

```
</details></div>