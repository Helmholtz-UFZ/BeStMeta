---
search:
  boost: 2.0
---


# Enum: ExposureRouteEnum 




_Route of chemical or treatment exposure._



<div data-search-exclude markdown="1">

URI: [bstm:ExposureRouteEnum](bstm:ExposureRouteEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| waterborne | None |  |
| dietary | None |  |
| injection_ip | None | Intraperitoneal injection |
| injection_iv | None | Intravenous injection |
| gavage | None |  |
| topical | None |  |
| inhalation | None |  |
| other | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [exposure_route](exposure_route.md) | Route of chemical or treatment administration |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: ExposureRouteEnum
description: Route of chemical or treatment exposure.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  waterborne:
    text: waterborne
  dietary:
    text: dietary
  injection_ip:
    text: injection_ip
    description: Intraperitoneal injection
  injection_iv:
    text: injection_iv
    description: Intravenous injection
  gavage:
    text: gavage
  topical:
    text: topical
  inhalation:
    text: inhalation
  other:
    text: other

```
</details>

</div>