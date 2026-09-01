# BeStMeta Metadata Schema

A cross-domain metadata schema for video tracking assays (VTAs) with focus on ecotoxicology and biomedical research. Designed to improve FAIR compliance by providing structured, machine-readable metadata for VTA datasets and individual trials.

URI: https://w3id.org/bestmeta/schema

Name: bestmeta



## Classes

| Class | Description |
| --- | --- |
| [AcquisitionParameters](AcquisitionParameters.md) | Video acquisition and recording parameters |
| [Experiment](Experiment.md) | Defines experimental context in which the subjects were studied |
| [ExperimentalConditions](ExperimentalConditions.md) | Biological and experimental conditions applicable to all trials in the datase... |
| [Manipulation](Manipulation.md) | Treatment and chemical exposure information decribing pharmacological, toxico... |
| [StatisticalAnalysis](StatisticalAnalysis.md) | Information describing the statistical analysis of behavioral data, including... |
| [Subject](Subject.md) | Biological identity of the organism(s) that is studied |
| [TrackingAnalysis](TrackingAnalysis.md) | Tracking software identity and version, algorithm details, post-tracking comp... |
| [VideoHardware](VideoHardware.md) | Camera systems, optical configuration, and physical recording infrastructure ... |
| [VTADataset](VTADataset.md) | Top-level study and provenance metadata for a VTA dataset |



## Slots

| Slot | Description |
| --- | --- |
| [acquisition_notes](acquisition_notes.md) | Free-text notes on acquisition settings |
| [acquisition_parameters](acquisition_parameters.md) | Video acquisition and recording settings |
| [age_unit](age_unit.md) | Age unit of the tracked organism(s) |
| [age_value](age_value.md) | Numeric age value of the tracked organism(s) |
| [analysis_code_doi](analysis_code_doi.md) | DOI of the deposited analysis code |
| [analysis_code_repository](analysis_code_repository.md) | Repository where analysis code is hosted |
| [analysis_code_repository_url](analysis_code_repository_url.md) | URL of the code repository |
| [arena_height](arena_height.md) | Height of the arena, when applicable |
| [arena_height_unit](arena_height_unit.md) | Unit of measurement for arena_height |
| [arena_length](arena_length.md) | Length of the arena along one axis |
| [arena_length_unit](arena_length_unit.md) | Unit of measurement for arena_length |
| [arena_shape](arena_shape.md) | Geometric shape of the test arena |
| [arena_type](arena_type.md) | Type of the test arena, e |
| [arena_width](arena_width.md) | Width of the arena along one axis |
| [arena_width_unit](arena_width_unit.md) | Unit of measurement for arena_width |
| [assay_description](assay_description.md) | Free-text description of the assay protocol |
| [assay_type](assay_type.md) | Name of the behavioral assay paradigm or test paradigm |
| [behavioral_metrics](behavioral_metrics.md) | List of behavioral metrics or endpoints extracted from tracking data |
| [bit_depth](bit_depth.md) | Bit depth per pixel channel of the recorded video |
| [body_length_unit](body_length_unit.md) | Body length unit of the tracked organism(s) |
| [body_length_value](body_length_value.md) | Body length numeric value of the tracked organism(s) |
| [camera_count](camera_count.md) | Number of cameras used simultaneously |
| [camera_device_type](camera_device_type.md) | General type of imaging device |
| [camera_distance_mm](camera_distance_mm.md) | Distance from camera lens to the arena floor in millimetres |
| [camera_interface](camera_interface.md) | Interface standard used for communication between the camera and the acquisit... |
| [camera_manufacturer](camera_manufacturer.md) | Manufacturer of the camera |
| [camera_model](camera_model.md) | Full manufacturer model name of the camera |
| [camera_position](camera_position.md) | Position of the camera relative to the arena |
| [camera_sensor_type](camera_sensor_type.md) | Image sensor technology |
| [closed_box_system_name](closed_box_system_name.md) | Name of the integrated commercial closed-box tracking system |
| [closed_box_system_version](closed_box_system_version.md) | Hardware version or model number of the closed-box system |
| [color_mode](color_mode.md) | Color mode of the recorded video |
| [compute_hardware](compute_hardware.md) | Primary compute hardware used for tracking and analysis |
| [confidence_interval_level](confidence_interval_level.md) | Confidence interval reported for statistical results |
| [contrast_polarity](contrast_polarity.md) | Contrast relationship between the tracked object and the background; indicate... |
| [control_type](control_type.md) | Type of control group used |
| [dataset_contact_email](dataset_contact_email.md) | Contact email for the dataset maintainer |
| [dataset_created_date](dataset_created_date.md) | Date when the dataset was created (YYYY-MM-DD) |
| [dataset_creator_name](dataset_creator_name.md) | Name(s) of data creators |
| [dataset_creator_orcid](dataset_creator_orcid.md) | ORCID identifier of the dataset creator |
| [dataset_description](dataset_description.md) | Free-text description of the dataset and its scientific purpose |
| [dataset_doi](dataset_doi.md) | DOI of the deposited dataset (assigned by repository) |
| [dataset_id](dataset_id.md) | Unique identifier for the dataset or study package |
| [dataset_license](dataset_license.md) | SPDX license identifier or URL (e |
| [dataset_notes](dataset_notes.md) | Free-text notes on the dataset not captured by structured fields |
| [dataset_title](dataset_title.md) | Descriptive title of the dataset |
| [dataset_version](dataset_version.md) | Semantic version string for the dataset (e |
| [developmental_stage](developmental_stage.md) | Developmental stage of the tracked organism(s) |
| [developmental_stage_unit](developmental_stage_unit.md) | Unit for developmental stage value of the tracked organism(s) |
| [developmental_stage_value](developmental_stage_value.md) | Numeric developmental stage value (e |
| [dropped_frames_count](dropped_frames_count.md) | Number of video frames lost or omitted during acquisition |
| [dropped_frames_reason](dropped_frames_reason.md) | Reason for dropped or omitted frames during acquisition, recording, encoding,... |
| [effect_size_measure](effect_size_measure.md) | Effect size measure reported to quantify the magnitude of observed effects or... |
| [endpoint_definitions](endpoint_definitions.md) | Definitions and calculation criteria used for behavioral endpoints, including... |
| [experiment](experiment.md) | Assay design, arena configuration, and environmental parameters |
| [experiment_end_datetime](experiment_end_datetime.md) | Date and time at which the experiment ended |
| [experiment_notes](experiment_notes.md) | Free-text notes on experimental conditions not captured by structured fields |
| [experiment_start_datetime](experiment_start_datetime.md) | Date and time at which the experiment began |
| [experimental_conditions](experimental_conditions.md) | Biological and experimental conditions for this dataset |
| [exposure_compound_chebi_id](exposure_compound_chebi_id.md) | ChEBI identifier for the test substance |
| [exposure_compound_name](exposure_compound_name.md) | Name of the chemical, drug, or substance used in the treatment or exposure |
| [exposure_concentration](exposure_concentration.md) | Nominal exposure concentration (numeric value only; use unit field) |
| [exposure_concentration_unit](exposure_concentration_unit.md) | Unit for exposure concentration |
| [exposure_duration_h](exposure_duration_h.md) | Duration of chemical or treatment exposure in hours |
| [exposure_route](exposure_route.md) | Route of chemical or treatment administration |
| [exposure_time](exposure_time.md) | Camera sensor exposure time per frame |
| [field_of_view_height](field_of_view_height.md) | Numeric value of vertical field of view covered by the camera |
| [field_of_view_unit](field_of_view_unit.md) | Unit of measurement for field_of_view_width and field_of_view_height |
| [field_of_view_width](field_of_view_width.md) | Numeric value of horizontal field of view covered by the camera |
| [frame_rate](frame_rate.md) | Number of frames captured per second (fps) during video recording |
| [frames_without_tracked_bodypart](frames_without_tracked_bodypart.md) | Percentage of frames in which no body part was tracked |
| [frames_without_tracked_individual](frames_without_tracked_individual.md) | Percentage of frames in which no individual was tracked |
| [gain](gain.md) | Camera gain setting at the time of recording |
| [genotype](genotype.md) | Genotype identifier of the tracked organism(s)including  strain-specific, mut... |
| [habituation_duration_min](habituation_duration_min.md) | Duration of habituation period before recording, in minutes |
| [habituation_protocol](habituation_protocol.md) | Description of habituation or acclimation prior to testing |
| [hardware_notes](hardware_notes.md) | Free-text notes on hardware configuration not captured by structured fields |
| [housing_conditions](housing_conditions.md) | Free-text description of animal housing conditions prior to assay |
| [illumination_illuminance](illumination_illuminance.md) | Illuminance at the recording arena or observation surface |
| [illumination_type](illumination_type.md) | Type of illumination used during recording |
| [illumination_wavelength](illumination_wavelength.md) | Peak wavelength of the illumination source in nanometres |
| [lens_focal_length_mm](lens_focal_length_mm.md) | Focal length of the imaging lens in millimetres;  applicable to camera or mic... |
| [light_cycle_detail](light_cycle_detail.md) | Free-text description of the light-dark cycle |
| [light_cycle_type](light_cycle_type.md) | Standardized category of the light-dark cycle |
| [manipulation](manipulation.md) | Treatment and chemical exposure applied to the subjects |
| [microscope_lot_number](microscope_lot_number.md) | Lot number of the microscope |
| [microscope_manufacturer](microscope_manufacturer.md) | Manufacturer of the microscope |
| [microscope_model](microscope_model.md) | Model name or identifier of the microscope |
| [microscope_serial_number](microscope_serial_number.md) | Serial number of the microscope |
| [microscope_type](microscope_type.md) | Microscope configuration according to the OME microscope type classification |
| [multiple_testing_correction](multiple_testing_correction.md) | Procedure used to correct for multiple comparisons (if more than one hypothes... |
| [n_bodyparts_tracked](n_bodyparts_tracked.md) | Number of body parts or keypoints tracked per individual |
| [n_individuals_per_arena](n_individuals_per_arena.md) | Number of individuals tested simultaneously in the arena |
| [n_individuals_total](n_individuals_total.md) | Total number of individuals used in the experiment |
| [n_individuals_tracked_per_arena](n_individuals_tracked_per_arena.md) | Number of individuals actually tracked in a single arena or trial |
| [noise_reduction_method](noise_reduction_method.md) | Method or algorithm used to reduce image noise during acquisition or immediat... |
| [objective_magnification](objective_magnification.md) | Magnification of microscope objective (if applicable) |
| [plate_well_count](plate_well_count.md) | Number of wells in the multiwell plate |
| [preprocessing_steps](preprocessing_steps.md) | Preprocessing steps applied to video before tracking to enhance quality or is... |
| [publication_doi](publication_doi.md) | DOI of the publication associated with the dataset |
| [raw_data_repository](raw_data_repository.md) | Repository where raw tracking data and/or video files are deposited |
| [raw_data_repository_url](raw_data_repository_url.md) | URL of the repository record or landing page |
| [raw_tracking_data_doi](raw_tracking_data_doi.md) | DOI of the deposited raw tracking data |
| [raw_tracking_data_format](raw_tracking_data_format.md) | File format of the raw tracking data |
| [recording_duration](recording_duration.md) | Total duration of the video recording in ISO 8601 duration format |
| [recording_end_datetime](recording_end_datetime.md) | Date and time at which acquisition of the video recording ended |
| [recording_software_name](recording_software_name.md) | Name of the software used to record the video |
| [recording_software_version](recording_software_version.md) | Version string of the recording software |
| [recording_start_datetime](recording_start_datetime.md) | Date and time at which acquisition of the video recording began |
| [research_domain](research_domain.md) | Primary research domain of this study |
| [sample_size_analysis](sample_size_analysis.md) | Sample size or power analysis method, software, or justification used before ... |
| [sex](sex.md) | Biological sex of the tracked organism(s) |
| [significance_level](significance_level.md) | Significance threshold used for hypothesis testing (e |
| [solvent_vehicle](solvent_vehicle.md) | Solvent or vehicle used to dissolve the test substance |
| [spatial_resolution](spatial_resolution.md) | Physical size represented by one pixel at the observation plane |
| [species_name](species_name.md) | Scientific (Latin) binomial name of the study organism |
| [species_ncbi_taxon_id](species_ncbi_taxon_id.md) | NCBI Taxonomy ID for the study organism |
| [statistical_analysis](statistical_analysis.md) | Statistical analysis for this dataset |
| [statistical_models](statistical_models.md) | Statistical models used to analyse behavioral endpoints |
| [statistical_software_name](statistical_software_name.md) | Name of the software used for statistical analysis |
| [statistical_software_version](statistical_software_version.md) | Version string of the software used for statistical analysis |
| [statistical_tests](statistical_tests.md) | Statistical tests applied to behavioral endpoints for hypothesis testing or i... |
| [statistics_notes](statistics_notes.md) | Free-text notes on the statistical analysis not captured by structured fields |
| [strain](strain.md) | Organism strain or line |
| [subject](subject.md) | Organism identity and biological attributes of the tracked subjects |
| [temperature_celsius](temperature_celsius.md) | Water or ambient temperature during the recording in degrees Celsius |
| [total_frame_count](total_frame_count.md) | Total number of frames in the video |
| [tracking_algorithm](tracking_algorithm.md) | Algorithmic approach used to detect, identify, and track organisms in video r... |
| [tracking_analysis](tracking_analysis.md) | Tracking software and analysis configuration |
| [tracking_confidence_threshold](tracking_confidence_threshold.md) | Confidence or likelihood threshold used to accept detections, identities, tra... |
| [tracking_data_format](tracking_data_format.md) | File format used to store tracking results, including coordinates, keypoints,... |
| [tracking_manual_correction](tracking_manual_correction.md) | Whether tracking results were manually reviewed, corrected, or curated after ... |
| [tracking_notes](tracking_notes.md) | Free-text notes on the tracking analysis not captured by structured fields |
| [tracking_software_name](tracking_software_name.md) | Name of the software used for tracking |
| [tracking_software_settings](tracking_software_settings.md) | Key tracking configuration parameters used during analysis, including softwar... |
| [tracking_software_type](tracking_software_type.md) | Indicates whether the tracking analysis was performed using a custom software... |
| [tracking_software_version](tracking_software_version.md) | Version string of the tracking software |
| [treatment_description](treatment_description.md) | Full description of the treatment protocol |
| [treatment_name](treatment_name.md) | Short label identifying the experimental treatment group, condition, or regim... |
| [video_codec](video_codec.md) | Video compression codec used for recording |
| [video_container_format](video_container_format.md) | File container format of the recorded video |
| [video_hardware](video_hardware.md) | Camera and hardware configuration |
| [video_resolution_height](video_resolution_height.md) | Vertical pixel count of the recorded video |
| [video_resolution_width](video_resolution_width.md) | Horizontal pixel count of the recorded video |
| [weight_unit](weight_unit.md) | Body weight unit of the tracked organism(s) |
| [weight_value](weight_value.md) | Body weight numeric value of the tracked organism(s) |
| [well_shape_bottom](well_shape_bottom.md) | Geometric bottom shape of the wells of a multiwell plate |
| [well_shape_cross_section](well_shape_cross_section.md) | Geometric cross section shape of the wells of a multiwell plate |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [ArenaShapeEnum](ArenaShapeEnum.md) | Geometric shape of the test arena |
| [ArenaTypeEnum](ArenaTypeEnum.md) | Type of the test arena, e |
| [CameraDeviceTypeEnum](CameraDeviceTypeEnum.md) | General types of imaging devices used in VTA setups |
| [CameraInterfaceEnum](CameraInterfaceEnum.md) | Hardware or connection interface used to transfer data from the camera to the... |
| [CameraPositionEnum](CameraPositionEnum.md) | Position of the camera relative to the arena used to record the tracked organ... |
| [CameraSensorTypeEnum](CameraSensorTypeEnum.md) | Image sensor technologies used in cameras |
| [ClosedBoxSystemEnum](ClosedBoxSystemEnum.md) | Commercial closed-box system used for recording and tracking the organism(s) ... |
| [ColorModeEnum](ColorModeEnum.md) | Color mode of the video recording |
| [ConcentrationUnitEnum](ConcentrationUnitEnum.md) | Units of concentration used to express the amount of a substance per volume o... |
| [ContrastPolarityEnum](ContrastPolarityEnum.md) | Polarity of object-to-background contrast in the video |
| [ControlTypeEnum](ControlTypeEnum.md) | Type of control condition used in the experiment for comparison against treat... |
| [DevelopmentalStageEnum](DevelopmentalStageEnum.md) | Controlled vocabulary of developmental stages of an organism |
| [DevelopmentUnitEnum](DevelopmentUnitEnum.md) | Units of time used to express the developmental age of an organism |
| [ExposureRouteEnum](ExposureRouteEnum.md) | Route of chemical or treatment exposure |
| [IlluminationTypeEnum](IlluminationTypeEnum.md) | Technology type of the light source used during video recording |
| [LengthUnitEnum](LengthUnitEnum.md) | Units of length, ranging from micrometers to meters |
| [LightCycleTypeEnum](LightCycleTypeEnum.md) | Standardized light-dark cycle types |
| [MicroscopeTypeEnum](MicroscopeTypeEnum.md) | OME microscope type values |
| [PreprocessingStepEnum](PreprocessingStepEnum.md) | Type of preprocessing step applied to the video data prior to tracking or ana... |
| [SexEnum](SexEnum.md) | Biological sex of the study subjects |
| [TrackingSoftwareTypeEnum](TrackingSoftwareTypeEnum.md) | Type of tracking software used |
| [VideoCodecEnum](VideoCodecEnum.md) | Video compression codec used for recording |
| [VideoContainerEnum](VideoContainerEnum.md) | Video file container format |
| [WeightUnitEnum](WeightUnitEnum.md) | Units of mass used to express weight measurements, ranging from micrograms to... |
| [WellBottomShapeEnum](WellBottomShapeEnum.md) | Geometric bottom shape of the wells of a multiwell plate |
| [WellCrossSectionShapeEnum](WellCrossSectionShapeEnum.md) | Geometric cross section shape of the wells of a multiwell plate |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Duration](Duration.md) | A time duration in ISO 8601 format |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
