---
search:
  boost: 2.0
---


# Enum: MicroscopeTypeEnum 




_OME microscope type values._



<div data-search-exclude markdown="1">

URI: [BeStMeta:MicroscopeTypeEnum](https://w3id.org/BeStMeta/MicroscopeTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| upright | None |  |
| inverted | None |  |
| dissection | None |  |
| electrophysiology | None |  |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [microscope_type](microscope_type.md) | Microscope configuration according to the OME microscope type classification |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: MicroscopeTypeEnum
description: OME microscope type values.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- OME:Type
rank: 1000
permissible_values:
  upright:
    text: upright
  inverted:
    text: inverted
  dissection:
    text: dissection
  electrophysiology:
    text: electrophysiology
  other:
    text: other

```
</details>

</div>