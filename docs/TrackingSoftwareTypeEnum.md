---
search:
  boost: 2.0
---


# Enum: TrackingSoftwareTypeEnum 




_Type of tracking software used._



<div data-search-exclude markdown="1">

URI: [BeStMeta:TrackingSoftwareTypeEnum](https://w3id.org/BeStMeta/TrackingSoftwareTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| standard | None | Commercial or publicly available software package |
| custom | None | Home-developed, in-house, or project-specific software |
| modified_standard | None | Standard software with custom modifications, plugins, or scripts |
| unknown | None | Software type not reported |




## Slots

| Name | Description |
| ---  | --- |
| [tracking_software_type](tracking_software_type.md) | Indicates whether the tracking analysis was performed using a custom software... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: TrackingSoftwareTypeEnum
description: Type of tracking software used.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  standard:
    text: standard
    description: Commercial or publicly available software package.
  custom:
    text: custom
    description: Home-developed, in-house, or project-specific software.
  modified_standard:
    text: modified_standard
    description: Standard software with custom modifications, plugins, or scripts.
  unknown:
    text: unknown
    description: Software type not reported.

```
</details>

</div>