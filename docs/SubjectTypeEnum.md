---
search:
  boost: 2.0
---


# Enum: SubjectTypeEnum 




_Indicates whether the tracked subject is a whole organism or a cell/cell culture, since some biological identity fields (e.g. sex, developmental stage) only apply to whole organisms._



<div data-search-exclude markdown="1">

URI: [BeStMeta:SubjectTypeEnum](https://w3id.org/BeStMeta/SubjectTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| organism | None | A whole living organism (e |
| cell | None | A cell, cell culture, or cell line (e |




## Slots

| Name | Description |
| ---  | --- |
| [subject_type](subject_type.md) | Indicates whether the subject being tracked is a whole organism or a cell/cel... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: SubjectTypeEnum
description: Indicates whether the tracked subject is a whole organism or a cell/cell
  culture, since some biological identity fields (e.g. sex, developmental stage) only
  apply to whole organisms.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  organism:
    text: organism
    description: A whole living organism (e.g. zebrafish, mouse, insect).
  cell:
    text: cell
    description: A cell, cell culture, or cell line (e.g. in vitro cell tracking,
      organoid).

```
</details>

</div>