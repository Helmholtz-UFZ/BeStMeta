---
search:
  boost: 10.0
---

# Class: EnvironmentalConditions 


_Environmental conditions and husbandry parameters for the experiments._



<div data-search-exclude markdown="1">



URI: [BeStMeta:EnvironmentalConditions](https://w3id.org/BeStMeta/EnvironmentalConditions)





```mermaid
 classDiagram
    class EnvironmentalConditions
    click EnvironmentalConditions href "../EnvironmentalConditions/"
      EnvironmentalConditions : feed_type
        
      EnvironmentalConditions : humidity
        
      EnvironmentalConditions : light_cycle_detail
        
      EnvironmentalConditions : light_cycle_type
        
          
    
        
        
        EnvironmentalConditions --> "0..1 _recommended_" LightCycleTypeEnum : light_cycle_type
        click LightCycleTypeEnum href "../LightCycleTypeEnum/"
    

        
      EnvironmentalConditions : water_ph
        
      EnvironmentalConditions : water_temperature
        
      EnvironmentalConditions : water_temperature_unit
        
          
    
        
        
        EnvironmentalConditions --> "0..1" TemperatureUnitEnum : water_temperature_unit
        click TemperatureUnitEnum href "../TemperatureUnitEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [feed_type](feed_type.md) | 0..1 <br/> [String](String.md) | Type of feed provided to the subject(s) | direct |
| [water_ph](water_ph.md) | 0..1 <br/> [Float](Float.md) | pH of the water in housing/experimnetal conditions | direct |
| [water_temperature](water_temperature.md) | 0..1 <br/> [Float](Float.md) | The temperature of the water during the experiment | direct |
| [water_temperature_unit](water_temperature_unit.md) | 0..1 <br/> [TemperatureUnitEnum](TemperatureUnitEnum.md) | The unit of the water temperature | direct |
| [light_cycle_type](light_cycle_type.md) | 0..1 _recommended_ <br/> [LightCycleTypeEnum](LightCycleTypeEnum.md) | Standardized category of the light-dark cycle | direct |
| [light_cycle_detail](light_cycle_detail.md) | 0..1 _recommended_ <br/> [String](String.md) | Free-text description of the light-dark cycle | direct |
| [humidity](humidity.md) | 0..1 <br/> [Float](Float.md) | Relative humidity where experiment was conducted (or the experiment area) | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Experiment](Experiment.md) | [environmental_conditions](environmental_conditions.md) | range | [EnvironmentalConditions](EnvironmentalConditions.md) |




## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'water_temperature': {'value_presence': 'PRESENT'}}``` |```{'water_temperature_unit': {'required': True}}``` | |



### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'light_cycle_type': {'equals_string': 'cyclic_ld'}}``` |```{'light_cycle_detail': {'required': True}}``` | |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:EnvironmentalConditions |
| native | BeStMeta:EnvironmentalConditions |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalConditions
description: Environmental conditions and husbandry parameters for the experiments.
from_schema: https://w3id.org/bestmeta/schema
slots:
- feed_type
- water_ph
- water_temperature
- water_temperature_unit
- light_cycle_type
- light_cycle_detail
- humidity
rules:
- preconditions:
    slot_conditions:
      water_temperature:
        name: water_temperature
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      water_temperature_unit:
        name: water_temperature_unit
        required: true
  description: water temperature requires water temperature unit
- preconditions:
    slot_conditions:
      light_cycle_type:
        name: light_cycle_type
        equals_string: cyclic_ld
  postconditions:
    slot_conditions:
      light_cycle_detail:
        name: light_cycle_detail
        required: true
  description: If light_cycle_type is cyclic_ld, light_cycle_detail should be provided.

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalConditions
description: Environmental conditions and husbandry parameters for the experiments.
from_schema: https://w3id.org/bestmeta/schema
attributes:
  feed_type:
    name: feed_type
    description: Type of feed provided to the subject(s).
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: EnvironmentalConditions
    domain_of:
    - EnvironmentalConditions
    range: string
  water_ph:
    name: water_ph
    description: pH of the water in housing/experimnetal conditions
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: EnvironmentalConditions
    domain_of:
    - EnvironmentalConditions
    range: float
  water_temperature:
    name: water_temperature
    description: The temperature of the water during the experiment
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: EnvironmentalConditions
    domain_of:
    - EnvironmentalConditions
    range: float
  water_temperature_unit:
    name: water_temperature_unit
    description: The unit of the water temperature.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: EnvironmentalConditions
    domain_of:
    - EnvironmentalConditions
    range: TemperatureUnitEnum
  light_cycle_type:
    name: light_cycle_type
    description: Standardized category of the light-dark cycle.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: EnvironmentalConditions
    domain_of:
    - EnvironmentalConditions
    range: LightCycleTypeEnum
    required: false
    recommended: true
  light_cycle_detail:
    name: light_cycle_detail
    description: Free-text description of the light-dark cycle.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - MESH:D017440
    rank: 1000
    owner: EnvironmentalConditions
    domain_of:
    - EnvironmentalConditions
    range: string
    required: false
    recommended: true
  humidity:
    name: humidity
    description: Relative humidity where experiment was conducted (or the experiment
      area).
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: EnvironmentalConditions
    domain_of:
    - EnvironmentalConditions
    range: float
    required: false
rules:
- preconditions:
    slot_conditions:
      water_temperature:
        name: water_temperature
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      water_temperature_unit:
        name: water_temperature_unit
        required: true
  description: water temperature requires water temperature unit
- preconditions:
    slot_conditions:
      light_cycle_type:
        name: light_cycle_type
        equals_string: cyclic_ld
  postconditions:
    slot_conditions:
      light_cycle_detail:
        name: light_cycle_detail
        required: true
  description: If light_cycle_type is cyclic_ld, light_cycle_detail should be provided.

```
</details></div>