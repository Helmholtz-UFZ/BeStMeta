---
search:
  boost: 5.0
---

# Slot: genotype 


_Genotype identifier of the tracked organism(s)including  strain-specific, mutant, transgenic, or engineered genotypes._



<div data-search-exclude markdown="1">



URI: [BeStMeta:genotype](https://w3id.org/BeStMeta/genotype)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Subject](Subject.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| source_ontology | GENO |




### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:genotype |
| native | BeStMeta:genotype |
| exact | EFO:0000513, GENO:0000536 |




## LinkML Source

<details>
```yaml
name: genotype
annotations:
  source_ontology:
    tag: source_ontology
    value: GENO
description: Genotype identifier of the tracked organism(s)including  strain-specific,
  mutant, transgenic, or engineered genotypes.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- EFO:0000513
- GENO:0000536
rank: 1000
domain_of:
- Subject
range: string
required: false
recommended: true

```
</details></div>