# Interpolations
FME_INTERPOLATION_AVERAGE16: int
FME_INTERPOLATION_AVERAGE4: int
FME_INTERPOLATION_BICUBIC: int
FME_INTERPOLATION_BILINEAR: int
FME_INTERPOLATION_NEARESTNEIGHBOR: int
FME_INTERPOLATION_SOURCE: int

# Interpretations
FME_INTERPRETATION_ALPHA16: int
FME_INTERPRETATION_ALPHA8: int
FME_INTERPRETATION_BLUE16: int
FME_INTERPRETATION_BLUE8: int
FME_INTERPRETATION_GRAY16: int
FME_INTERPRETATION_GRAY8: int
FME_INTERPRETATION_GREEN16: int
FME_INTERPRETATION_GREEN8: int
FME_INTERPRETATION_INT16: int
FME_INTERPRETATION_INT32: int
FME_INTERPRETATION_INT64: int
FME_INTERPRETATION_INT8: int
FME_INTERPRETATION_NULL: int
FME_INTERPRETATION_REAL32: int
FME_INTERPRETATION_REAL64: int
FME_INTERPRETATION_RED16: int
FME_INTERPRETATION_RED8: int
FME_INTERPRETATION_RGB24: int
FME_INTERPRETATION_RGB48: int
FME_INTERPRETATION_RGBA32: int
FME_INTERPRETATION_RGBA64: int
FME_INTERPRETATION_STRING: int
FME_INTERPRETATION_UINT16: int
FME_INTERPRETATION_UINT32: int
FME_INTERPRETATION_UINT64: int
FME_INTERPRETATION_UINT8: int

# Reinterpretation modes
FME_REINTERPRET_MODE_BAND: int
FME_REINTERPRET_MODE_PALETTE: int
FME_REINTERPRET_MODE_RASTER: int

# Cell resize operations
FME_CELL_RESIZE_PRESERVE_CELL_SHAPE: int
FME_CELL_RESIZE_PRESERVE_NUM_CELLS: int
FME_CELL_RESIZE_SQUARE_CELLS: int

# Calculate Aspect parameters
kFME_CalculateAspect_interpolateNodata: int
kFME_CalculateAspect_algorithm: int
kFME_CalculateAspect_algorithm_Horn: int
kFME_CalculateAspect_algorithm_ZevenbergenThorne: int

# Calculate Slope parameters
kFME_CalculateSlope_interpolateNodata: int
kFME_CalculateSlope_algorithm: int
kFME_CalculateSlope_algorithm_Horn: int
kFME_CalculateSlope_algorithm_ZevenbergenThorne: int

# Interpretation conversion parameters
kFME_ConvertInterpretation_RGBAToRGB: int
kFME_ConvertInterpretation_RGBAToRGB_applyAlpha: int
kFME_ConvertInterpretation_RGBAToRGB_dropAlpha: int
kFME_ConvertInterpretation_RGBToRGBA: int
kFME_ConvertInterpretation_RGBToRGBA_createAlphaFromNodata: int
kFME_ConvertInterpretation_RGBToRGBA_createOpaqueAlpha: int
kFME_ConvertInterpretation_colorNumeric_boundedCast: int
kFME_ConvertInterpretation_colorNumeric_cast: int
kFME_ConvertInterpretation_colorNumeric_dataScale: int
kFME_ConvertInterpretation_colorNumeric_typeScale: int
kFME_ConvertInterpretation_colorToColor: int
kFME_ConvertInterpretation_colorToNumeric: int
kFME_ConvertInterpretation_floatToInteger: int
kFME_ConvertInterpretation_floatToInteger_ceil: int
kFME_ConvertInterpretation_floatToInteger_floor: int
kFME_ConvertInterpretation_floatToInteger_round: int
kFME_ConvertInterpretation_manyToOneBand: int
kFME_ConvertInterpretation_manyToOneBand_average: int
kFME_ConvertInterpretation_numericToColor: int
kFME_ConvertInterpretation_numericToNumeric: int

# Hillshade parameters
kFME_Hillshade_algorithm: int
kFME_Hillshade_algorithm_Horn: int
kFME_Hillshade_algorithm_ZevenbergenThorne: int
kFME_Hillshade_interpolateNodata: int

# Mosaicking parameters
kFME_Mosaic_mergePalettes: int
kFME_Mosaic_nodataOverwrite: int
kFME_Mosaic_overlappingValues: int
kFME_Mosaic_overlappingValues_average: int
kFME_Mosaic_overlappingValues_compositeUsingAlpha: int
kFME_Mosaic_overlappingValues_last: int
kFME_Mosaic_overlappingValues_max: int
kFME_Mosaic_overlappingValues_min: int
kFME_Mosaic_overlappingValues_sum: int

# Nodata mask parameters
kFME_CreateNodataMask_removeNodata: int

# Clip parameters
kFME_Clip_preserveExtents: int

# Resampling parameters
kFME_Resample_snapOffsetX: int
kFME_Resample_snapOffsetY: int

# Scaling parameters
kFME_RasterScale_scaleSpacingOnly: int

# Slope Type Units
FME_SLOPETYPE_DEGREES: int
FME_SLOPETYPE_PERCENTRISE: int

class FMERasterTools:
    pass

class FMEBandTilePopulator:
    pass