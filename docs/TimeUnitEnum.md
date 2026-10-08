---
search:
  boost: 2.0
---


# Enum: TimeUnitEnum 




_Unit of time measurement, mapped to UCUM (Unified Code for Units of Measure) codes._



<div data-search-exclude markdown="1">

URI: [BeStMeta:TimeUnitEnum](https://w3id.org/BeStMeta/TimeUnitEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| milliseconds | ms | Milliseconds |
| seconds | s | Seconds |
| minutes | min | Minutes |
| hours | h | Hours |
| days | d | Days |
| weeks | wk | Weeks |
| months | mo | Months |
| years | a | Years |




## Slots

| Name | Description |
| ---  | --- |
| [habituation_duration_unit](habituation_duration_unit.md) | Unit of measurement used to measure habituation duration |
| [exposure_duration_unit](exposure_duration_unit.md) | Unit of measurement used to report exposure duration |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: TimeUnitEnum
description: Unit of time measurement, mapped to UCUM (Unified Code for Units of Measure)
  codes.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  milliseconds:
    text: milliseconds
    description: Milliseconds.
    meaning: ms
  seconds:
    text: seconds
    description: Seconds.
    meaning: s
  minutes:
    text: minutes
    description: Minutes.
    meaning: min
  hours:
    text: hours
    description: Hours.
    meaning: h
  days:
    text: days
    description: Days.
    meaning: d
  weeks:
    text: weeks
    description: Weeks.
    meaning: wk
  months:
    text: months
    description: Months.
    meaning: mo
  years:
    text: years
    description: Years.
    meaning: a

```
</details>

</div>