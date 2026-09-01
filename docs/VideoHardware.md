---
search:
  boost: 10.0
---

# Class: VideoHardware 


_Camera systems, optical configuration, and physical recording infrastructure used in the VTA. Documents instrument identity and optical specifications._



<div data-search-exclude markdown="1">



URI: [BeStMeta:VideoHardware](https://w3id.org/BeStMeta/VideoHardware)





```mermaid
 classDiagram
    class VideoHardware
    click VideoHardware href "../VideoHardware/"
      VideoHardware : camera_count
        
      VideoHardware : camera_device_type
        
          
    
        
        
        VideoHardware --> "1" CameraDeviceTypeEnum : camera_device_type
        click CameraDeviceTypeEnum href "../CameraDeviceTypeEnum/"
    

        
      VideoHardware : camera_distance_mm
        
      VideoHardware : camera_interface
        
          
    
        
        
        VideoHardware --> "0..1" CameraInterfaceEnum : camera_interface
        click CameraInterfaceEnum href "../CameraInterfaceEnum/"
    

        
      VideoHardware : camera_manufacturer
        
      VideoHardware : camera_model
        
      VideoHardware : camera_position
        
          
    
        
        
        VideoHardware --> "0..1 _recommended_" CameraPositionEnum : camera_position
        click CameraPositionEnum href "../CameraPositionEnum/"
    

        
      VideoHardware : camera_sensor_type
        
          
    
        
        
        VideoHardware --> "0..1 _recommended_" CameraSensorTypeEnum : camera_sensor_type
        click CameraSensorTypeEnum href "../CameraSensorTypeEnum/"
    

        
      VideoHardware : closed_box_system_name
        
          
    
        
        
        VideoHardware --> "0..1" ClosedBoxSystemEnum : closed_box_system_name
        click ClosedBoxSystemEnum href "../ClosedBoxSystemEnum/"
    

        
      VideoHardware : closed_box_system_version
        
      VideoHardware : contrast_polarity
        
          
    
        
        
        VideoHardware --> "0..1 _recommended_" ContrastPolarityEnum : contrast_polarity
        click ContrastPolarityEnum href "../ContrastPolarityEnum/"
    

        
      VideoHardware : field_of_view_height
        
      VideoHardware : field_of_view_unit
        
          
    
        
        
        VideoHardware --> "0..1" LengthUnitEnum : field_of_view_unit
        click LengthUnitEnum href "../LengthUnitEnum/"
    

        
      VideoHardware : field_of_view_width
        
      VideoHardware : hardware_notes
        
      VideoHardware : lens_focal_length_mm
        
      VideoHardware : microscope_lot_number
        
      VideoHardware : microscope_manufacturer
        
      VideoHardware : microscope_model
        
      VideoHardware : microscope_serial_number
        
      VideoHardware : microscope_type
        
          
    
        
        
        VideoHardware --> "0..1" MicroscopeTypeEnum : microscope_type
        click MicroscopeTypeEnum href "../MicroscopeTypeEnum/"
    

        
      VideoHardware : objective_magnification
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [camera_count](camera_count.md) | 1 <br/> [Integer](Integer.md) | Number of cameras used simultaneously | direct |
| [camera_device_type](camera_device_type.md) | 1 <br/> [CameraDeviceTypeEnum](CameraDeviceTypeEnum.md) | General type of imaging device | direct |
| [camera_model](camera_model.md) | 1 <br/> [String](String.md) | Full manufacturer model name of the camera | direct |
| [camera_manufacturer](camera_manufacturer.md) | 1 <br/> [String](String.md) | Manufacturer of the camera | direct |
| [camera_sensor_type](camera_sensor_type.md) | 0..1 _recommended_ <br/> [CameraSensorTypeEnum](CameraSensorTypeEnum.md) | Image sensor technology | direct |
| [camera_distance_mm](camera_distance_mm.md) | 0..1 _recommended_ <br/> [Float](Float.md) | Distance from camera lens to the arena floor in millimetres | direct |
| [camera_position](camera_position.md) | 0..1 _recommended_ <br/> [CameraPositionEnum](CameraPositionEnum.md) | Position of the camera relative to the arena | direct |
| [lens_focal_length_mm](lens_focal_length_mm.md) | 0..1 _recommended_ <br/> [Float](Float.md) | Focal length of the imaging lens in millimetres;  applicable to camera or mic... | direct |
| [objective_magnification](objective_magnification.md) | 0..1 _recommended_ <br/> [Float](Float.md) | Magnification of microscope objective (if applicable) | direct |
| [contrast_polarity](contrast_polarity.md) | 0..1 _recommended_ <br/> [ContrastPolarityEnum](ContrastPolarityEnum.md) | Contrast relationship between the tracked object and the background; indicate... | direct |
| [field_of_view_width](field_of_view_width.md) | 0..1 _recommended_ <br/> [Float](Float.md) | Numeric value of horizontal field of view covered by the camera | direct |
| [field_of_view_height](field_of_view_height.md) | 0..1 _recommended_ <br/> [Float](Float.md) | Numeric value of vertical field of view covered by the camera | direct |
| [field_of_view_unit](field_of_view_unit.md) | 0..1 <br/> [LengthUnitEnum](LengthUnitEnum.md) | Unit of measurement for field_of_view_width and field_of_view_height | direct |
| [camera_interface](camera_interface.md) | 0..1 <br/> [CameraInterfaceEnum](CameraInterfaceEnum.md) | Interface standard used for communication between the camera and the acquisit... | direct |
| [microscope_manufacturer](microscope_manufacturer.md) | 0..1 <br/> [String](String.md) | Manufacturer of the microscope | direct |
| [microscope_model](microscope_model.md) | 0..1 <br/> [String](String.md) | Model name or identifier of the microscope | direct |
| [microscope_type](microscope_type.md) | 0..1 <br/> [MicroscopeTypeEnum](MicroscopeTypeEnum.md) | Microscope configuration according to the OME microscope type classification | direct |
| [microscope_serial_number](microscope_serial_number.md) | 0..1 <br/> [String](String.md) | Serial number of the microscope | direct |
| [microscope_lot_number](microscope_lot_number.md) | 0..1 <br/> [String](String.md) | Lot number of the microscope | direct |
| [closed_box_system_name](closed_box_system_name.md) | 0..1 <br/> [ClosedBoxSystemEnum](ClosedBoxSystemEnum.md) | Name of the integrated commercial closed-box tracking system | direct |
| [closed_box_system_version](closed_box_system_version.md) | 0..1 <br/> [String](String.md) | Hardware version or model number of the closed-box system | direct |
| [hardware_notes](hardware_notes.md) | 0..1 <br/> [String](String.md) | Free-text notes on hardware configuration not captured by structured fields | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [VTADataset](VTADataset.md) | [video_hardware](video_hardware.md) | range | [VideoHardware](VideoHardware.md) |




## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| any_of |```[{'slot_conditions': {'field_of_view_width': {'value_presence': 'PRESENT'}}}, {'slot_conditions': {'field_of_view_height': {'value_presence': 'PRESENT'}}}]``` | | |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BeStMeta:VideoHardware |
| native | BeStMeta:VideoHardware |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VideoHardware
description: Camera systems, optical configuration, and physical recording infrastructure
  used in the VTA. Documents instrument identity and optical specifications.
from_schema: https://w3id.org/bestmeta/schema
slots:
- camera_count
- camera_device_type
- camera_model
- camera_manufacturer
- camera_sensor_type
- camera_distance_mm
- camera_position
- lens_focal_length_mm
- objective_magnification
- contrast_polarity
- field_of_view_width
- field_of_view_height
- field_of_view_unit
- camera_interface
- microscope_manufacturer
- microscope_model
- microscope_type
- microscope_serial_number
- microscope_lot_number
- closed_box_system_name
- closed_box_system_version
- hardware_notes
rules:
- preconditions:
    any_of:
    - slot_conditions:
        field_of_view_width:
          name: field_of_view_width
          value_presence: PRESENT
    - slot_conditions:
        field_of_view_height:
          name: field_of_view_height
          value_presence: PRESENT
  postconditions:
    slot_conditions:
      field_of_view_width:
        name: field_of_view_width
        value_presence: PRESENT
      field_of_view_height:
        name: field_of_view_height
        value_presence: PRESENT
      field_of_view_unit:
        name: field_of_view_unit
        value_presence: PRESENT
  description: Field of view width, height, and unit should be reported together.

```
</details>

### Induced

<details>
```yaml
name: VideoHardware
description: Camera systems, optical configuration, and physical recording infrastructure
  used in the VTA. Documents instrument identity and optical specifications.
from_schema: https://w3id.org/bestmeta/schema
attributes:
  camera_count:
    name: camera_count
    description: Number of cameras used simultaneously.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: integer
    required: true
  camera_device_type:
    name: camera_device_type
    description: General type of imaging device.
    from_schema: https://w3id.org/bestmeta/schema
    broad_mappings:
    - OBI:0000398
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: CameraDeviceTypeEnum
    required: true
  camera_model:
    name: camera_model
    description: Full manufacturer model name of the camera.
    examples:
    - value: Basler acA1300-60gc
    - value: Logitech C920
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: true
  camera_manufacturer:
    name: camera_manufacturer
    description: Manufacturer of the camera.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - schema:manufacturer
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: true
  camera_sensor_type:
    name: camera_sensor_type
    description: Image sensor technology.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: CameraSensorTypeEnum
    required: false
    recommended: true
  camera_distance_mm:
    name: camera_distance_mm
    description: Distance from camera lens to the arena floor in millimetres.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: float
    required: false
    recommended: true
    unit:
      ucum_code: mm
  camera_position:
    name: camera_position
    description: Position of the camera relative to the arena.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: CameraPositionEnum
    required: false
    recommended: true
  lens_focal_length_mm:
    name: lens_focal_length_mm
    description: Focal length of the imaging lens in millimetres;  applicable to camera
      or microscope optics when reported.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - AFQ:0000062
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: float
    required: false
    recommended: true
    unit:
      ucum_code: mm
  objective_magnification:
    name: objective_magnification
    annotations:
      ome_element:
        tag: ome_element
        value: Objective/Magnification
    description: Magnification of microscope objective (if applicable).
    examples:
    - value: '4'
    - value: '10'
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: float
    required: false
    recommended: true
  contrast_polarity:
    name: contrast_polarity
    description: Contrast relationship between the tracked object and the background;
      indicates whether the subject appears bright on a dark background or dark on
      a bright background in the recorded video.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: ContrastPolarityEnum
    required: false
    recommended: true
  field_of_view_width:
    name: field_of_view_width
    description: Numeric value of horizontal field of view covered by the camera.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: float
    required: false
    recommended: true
  field_of_view_height:
    name: field_of_view_height
    description: Numeric value of vertical field of view covered by the camera.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: float
    required: false
    recommended: true
  field_of_view_unit:
    name: field_of_view_unit
    description: Unit of measurement for field_of_view_width and field_of_view_height.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: LengthUnitEnum
  camera_interface:
    name: camera_interface
    description: Interface standard used for communication between the camera and
      the acquisition system.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: CameraInterfaceEnum
    required: false
  microscope_manufacturer:
    name: microscope_manufacturer
    description: Manufacturer of the microscope.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - OME:Manufacturer
    - schema:manufacturer
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: false
  microscope_model:
    name: microscope_model
    description: Model name or identifier of the microscope.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - OME:Model
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: false
  microscope_type:
    name: microscope_type
    description: Microscope configuration according to the OME microscope type classification.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - OME:Type
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: MicroscopeTypeEnum
    required: false
  microscope_serial_number:
    name: microscope_serial_number
    description: Serial number of the microscope.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - OME:SerialNumber
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: false
  microscope_lot_number:
    name: microscope_lot_number
    description: Lot number of the microscope.
    from_schema: https://w3id.org/bestmeta/schema
    exact_mappings:
    - OME:LotNumber
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: false
  closed_box_system_name:
    name: closed_box_system_name
    description: Name of the integrated commercial closed-box tracking system. (e.g.
      ZebraBox, DanioVision, ToxMate, PhenoTyper).
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: ClosedBoxSystemEnum
    required: false
  closed_box_system_version:
    name: closed_box_system_version
    description: Hardware version or model number of the closed-box system.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: false
  hardware_notes:
    name: hardware_notes
    description: Free-text notes on hardware configuration not captured by structured
      fields.
    from_schema: https://w3id.org/bestmeta/schema
    rank: 1000
    owner: VideoHardware
    domain_of:
    - VideoHardware
    range: string
    required: false
rules:
- preconditions:
    any_of:
    - slot_conditions:
        field_of_view_width:
          name: field_of_view_width
          value_presence: PRESENT
    - slot_conditions:
        field_of_view_height:
          name: field_of_view_height
          value_presence: PRESENT
  postconditions:
    slot_conditions:
      field_of_view_width:
        name: field_of_view_width
        value_presence: PRESENT
      field_of_view_height:
        name: field_of_view_height
        value_presence: PRESENT
      field_of_view_unit:
        name: field_of_view_unit
        value_presence: PRESENT
  description: Field of view width, height, and unit should be reported together.

```
</details></div>