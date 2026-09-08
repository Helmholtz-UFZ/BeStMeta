---
search:
  boost: 10.0
---

# Class: ExperimentalConditions 


_Biological and experimental conditions applicable to all trials in the dataset. Covers organism identity, treatment, assay design, and environmental parameters._



<div data-search-exclude markdown="1">



URI: [BeStMeta:ExperimentalConditions](https://w3id.org/BeStMeta/ExperimentalConditions)





```mermaid
 classDiagram
    class ExperimentalConditions
    click ExperimentalConditions href "../ExperimentalConditions/"
      ExperimentalConditions : experiment
        
          
    
        
        
        ExperimentalConditions --> "1" Experiment : experiment
        click Experiment href "../Experiment/"
    

        
      ExperimentalConditions : experiment_notes
        
      ExperimentalConditions : manipulation
        
          
    
        
        
        ExperimentalConditions --> "0..1" Manipulation : manipulation
        click Manipulation href "../Manipulation/"
    

        
      ExperimentalConditions : subject
        
          
    
        
        
        ExperimentalConditions --> "1" Subject : subject
        click Subject href "../Subject/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 1 <br/> [Subject](Subject.md) | Organism identity and biological attributes of the tracked subjects | direct |
| [experiment](experiment.md) | 1 <br/> [Experiment](Experiment.md) | Assay design, arena configuration, and environmental parameters | direct |
| [manipulation](manipulation.md) | 0..1 <br/> [Manipulation](Manipulation.md) | Treatment and chemical exposure applied to the subjects | direct |
| [experiment_notes](experiment_notes.md) | 0..1 <br/> [String](String.md) | Free-text notes on experimental conditions not captured by structured fields | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VTADataset](VTADataset.md) | [experimental_conditions](experimental_conditions.md) | range | [ExperimentalConditions](ExperimentalConditions.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:ExperimentalConditions |
| native | BeStMeta:ExperimentalConditions |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExperimentalConditions
description: Biological and experimental conditions applicable to all trials in the
  dataset. Covers organism identity, treatment, assay design, and environmental parameters.
from_schema: https://w3id.org/bestmeta/schema
slots:
- subject
- experiment
- manipulation
- experiment_notes

```
</details>

### Induced

<details>
```yaml
name: ExperimentalConditions
description: Biological and experimental conditions applicable to all trials in the
  dataset. Covers organism identity, treatment, assay design, and environmental parameters.
from_schema: https://w3id.org/bestmeta/schema
attributes:
  subject:
    name: subject
    description: Organism identity and biological attributes of the tracked subjects.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: ExperimentalConditions
    domain_of:
    - ExperimentalConditions
    range: Subject
    required: true
    inlined: true
  experiment:
    name: experiment
    description: Assay design, arena configuration, and environmental parameters.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: ExperimentalConditions
    domain_of:
    - ExperimentalConditions
    range: Experiment
    required: true
    inlined: true
  manipulation:
    name: manipulation
    description: Treatment and chemical exposure applied to the subjects. Omit this
      sub-class entirely for naive or vehicle-only datasets.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: ExperimentalConditions
    domain_of:
    - ExperimentalConditions
    range: Manipulation
    required: false
    inlined: true
  experiment_notes:
    name: experiment_notes
    description: Free-text notes on experimental conditions not captured by structured
      fields.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: ExperimentalConditions
    domain_of:
    - ExperimentalConditions
    range: string
    required: false

```
</details></div>