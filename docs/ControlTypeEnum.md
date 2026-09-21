---
search:
  boost: 2.0
---


# Enum: ControlTypeEnum 




_Type of control condition used in the experiment for comparison against treated groups._



<div data-search-exclude markdown="1">

URI: [BeStMeta:ControlTypeEnum](https://w3id.org/BeStMeta/ControlTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| solvent_control | None | Control receiving only the solvent used to dissolve the test compound (e |
| vehicle_control | None | Control receiving the full delivery vehicle/formulation used to administer th... |
| naive_control | None | Control never subjected to any procedural handling, injection, or manipulatio... |
| sham_control | None | Control subjected to the same surgical or procedural intervention as treated ... |
| positive_control | None | Control using a treatment already known to produce the effect under investiga... |
| negative_control | None | Control condition not expected to produce the effect or response under invest... |
| untreated_control | None | Control subjected to the same handling and procedural context as treated subj... |
| historical_control | None | Control data drawn from a previous, non-concurrent cohort or study rather tha... |
| other | None | Control type not described by other values |




## Slots

| Name | Description |
| ---  | --- |
| [control_type](control_type.md) | Type of control group used |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: ControlTypeEnum
description: Type of control condition used in the experiment for comparison against
  treated groups.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  solvent_control:
    text: solvent_control
    description: Control receiving only the solvent used to dissolve the test compound
      (e.g. DMSO, ethanol), without the active compound.
  vehicle_control:
    text: vehicle_control
    description: Control receiving the full delivery vehicle/formulation used to administer
      the treatment (which may include the solvent plus additional excipients or carriers),
      without the active compound.
  naive_control:
    text: naive_control
    description: Control never subjected to any procedural handling, injection, or
      manipulation beyond standard housing; a fully unmanipulated baseline.
  sham_control:
    text: sham_control
    description: Control subjected to the same surgical or procedural intervention
      as treated subjects (e.g. anesthesia and incision without lesion or implant),
      used to isolate the effect of the procedure itself.
  positive_control:
    text: positive_control
    description: Control using a treatment already known to produce the effect under
      investigation, used to confirm that the assay is capable of detecting a true
      response when one is present.
  negative_control:
    text: negative_control
    description: Control condition not expected to produce the effect or response
      under investigation. Depending on field-specific convention, may refer to an
      untreated/vehicle baseline, or to a comparator compound delivered identically
      but known to lack the relevant activity.
  untreated_control:
    text: untreated_control
    description: Control subjected to the same handling and procedural context as
      treated subjects (e.g. timing, injection procedure), but receiving no active
      compound, solvent, or vehicle.
  historical_control:
    text: historical_control
    description: Control data drawn from a previous, non-concurrent cohort or study
      rather than run alongside the current treatment group.
  other:
    text: other
    description: Control type not described by other values

```
</details>

</div>