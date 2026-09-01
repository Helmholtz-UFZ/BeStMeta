---
search:
  boost: 2.0
---


# Enum: SexEnum 




_Biological sex of the study subjects_



<div data-search-exclude markdown="1">

URI: [BeStMeta:SexEnum](https://w3id.org/BeStMeta/SexEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| male | None |  |
| female | None |  |
| mixed | None | Mixed male and female in same group |
| unknown | None |  |
| not_applicable | None | e |




## Slots

| Name | Description |
| ---  | --- |
| [sex](sex.md) | Biological sex of the tracked organism(s) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: SexEnum
description: Biological sex of the study subjects
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  male:
    text: male
  female:
    text: female
  mixed:
    text: mixed
    description: Mixed male and female in same group.
  unknown:
    text: unknown
  not_applicable:
    text: not_applicable
    description: e.g. asexual organisms, embryos

```
</details>

</div>