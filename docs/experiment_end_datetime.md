---
search:
  boost: 5.0
---

# Slot: experiment_end_datetime 


_Date and time at which the experiment ended._



<div data-search-exclude markdown="1">



URI: [bstm:experiment_end_datetime](bstm:experiment_end_datetime)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](Datetime.md) |
| Domain Of | [ExperimentalConditions](ExperimentalConditions.md) |

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
| self | bstm:experiment_end_datetime |
| native | bstm:experiment_end_datetime |




## LinkML Source

<details>
```yaml
name: experiment_end_datetime
description: Date and time at which the experiment ended.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
domain_of:
- ExperimentalConditions
range: datetime
required: false
recommended: true

```
</details></div>