---
search:
  boost: 2.0
---


# Enum: PreprocessingStepEnum 




_Type of preprocessing step applied to the video data prior to tracking or analysis._



<div data-search-exclude markdown="1">

URI: [bstm:PreprocessingStepEnum](bstm:PreprocessingStepEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| background_subtraction | None | Removal of static background elements |
| brightness_normalization | None | Adjustment of brightness levels |
| contrast_enhancement | None | Improvement of contrast |
| spatial_filtering | None | Spatial domain filtering, for example Gaussian blur |
| temporal_filtering | None | Temporal smoothing across frames |
| roi_masking | None | Restriction to a region of interest |
| noise_reduction | None | Denoising applied to the video |
| frame_averaging | None | Averaging multiple frames |
| perspective_correction | None | Geometric correction of image perspective |
| colour_space_conversion | None | Conversion between color spaces |
| thresholding | None | Segmentation of objects using intensity or color thresholds |
| image_stabilization | None | Correction of camera movement between frames |
| other | None | Other preprocessing step, describe in notes |




## Slots

| Name | Description |
| ---  | --- |
| [preprocessing_steps](preprocessing_steps.md) | Preprocessing steps applied to video before tracking to enhance quality or is... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/bestmeta/schema






## LinkML Source

<details>
```yaml
name: PreprocessingStepEnum
description: Type of preprocessing step applied to the video data prior to tracking
  or analysis.
from_schema: https://w3id.org/bestmeta/schema
rank: 1000
permissible_values:
  background_subtraction:
    text: background_subtraction
    description: Removal of static background elements.
  brightness_normalization:
    text: brightness_normalization
    description: Adjustment of brightness levels.
  contrast_enhancement:
    text: contrast_enhancement
    description: Improvement of contrast.
  spatial_filtering:
    text: spatial_filtering
    description: Spatial domain filtering, for example Gaussian blur.
  temporal_filtering:
    text: temporal_filtering
    description: Temporal smoothing across frames.
  roi_masking:
    text: roi_masking
    description: Restriction to a region of interest.
  noise_reduction:
    text: noise_reduction
    description: Denoising applied to the video.
  frame_averaging:
    text: frame_averaging
    description: Averaging multiple frames.
  perspective_correction:
    text: perspective_correction
    description: Geometric correction of image perspective.
  colour_space_conversion:
    text: colour_space_conversion
    description: Conversion between color spaces.
  thresholding:
    text: thresholding
    description: Segmentation of objects using intensity or color thresholds.
  image_stabilization:
    text: image_stabilization
    description: Correction of camera movement between frames.
  other:
    text: other
    description: Other preprocessing step, describe in notes.

```
</details>

</div>