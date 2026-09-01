---
search:
  boost: 5.0
---

# Slot: raw_data_repository_url 


_URL of the repository record or landing page._



<div data-search-exclude markdown="1">



URI: [BeStMeta:raw_data_repository_url](https://w3id.org/BeStMeta/raw_data_repository_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VTADataset](VTADataset.md) | Top-level study and provenance metadata for a VTA dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [VTADataset](VTADataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:raw_data_repository_url |
| native | BeStMeta:raw_data_repository_url |
| exact | schema:url, dcterms:source |




## LinkML Source

<details>
```yaml
name: raw_data_repository_url
description: URL of the repository record or landing page.
from_schema: https://w3id.org/bestmeta/schema
exact_mappings:
- schema:url
- dcterms:source
rank: 1000
domain_of:
- VTADataset
range: uri
required: false
recommended: true

```
</details></div>