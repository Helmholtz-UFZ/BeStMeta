---
search:
  boost: 5.0
---

# Slot: assay_type 


_Name of the behavioral assay paradigm or test paradigm._



<div data-search-exclude markdown="1">



URI: [BeStMeta:assay_type](https://w3id.org/BeStMeta/assay_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](Experiment.md) | Defines experimental context in which the subjects were studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Experiment](Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |









## Examples

| Value |
| --- |
| open field test |
| light-dark transition |
| elevated plus maze |
| locomotor activity assay |
| chemobehavioral assay |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:assay_type |
| native | BeStMeta:assay_type |
| broad | OBI:0000070 |




## LinkML Source

<details>
```yaml
name: assay_type
description: Name of the behavioral assay paradigm or test paradigm.
examples:
- value: open field test
- value: light-dark transition
- value: elevated plus maze
- value: locomotor activity assay
- value: chemobehavioral assay
from_schema: https://w3id.org/bestmeta/schema
broad_mappings:
- OBI:0000070
rank: 1000
domain_of:
- Experiment
range: string
required: true

```
</details></div>