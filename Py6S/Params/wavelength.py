#from sixs_exceptions import *
import collections

def Wavelength(start_wavelength, end_wavelength=None, filter=None):
    """Select one or more wavelengths for the 6S simulation.
    
    There are a number of ways to do this:
    
    1. Pass a single value of a wavelength in micrometres. The simulation will be performed for just this wavelength::
    
        Wavelength(0.43)
    
    2. Pass a start and end wavelength in micrometres. The simulation will be performed across this wavelength range with a constant filter function (spectral response function) of 1.0::
    
        Wavelength(0.43, 0.50)
    
    3. Pass a start and end wavelength, and a filter given at 2.5nm intervals. The simulation will be performed across this wavelength range using the given filter function::
    
        Wavelength(0.400, 0.410, [0.7, 0.9, 1.0, 0.3])
    
    4. Pass a constant (as defined in this class) for a pre-defined wavelength range::
    
        Wavelength(PredefinedWavelength.LANDSAT_TM_B1)
    
    """
    try:
        wv_id = start_wavelength[0]
        type = "%d (Chosen Band)\n" % (-1 *wv_id)
        data = None
        min_wv = start_wavelength[1]
        max_wv = start_wavelength[2]
    except:
        if end_wavelength == None:
                # It's simply a wavelength value
                if start_wavelength > PredefinedWavelengths.MAX_ALLOWABLE_WAVELENGTH or start_wavelength < PredefinedWavelengths.MIN_ALLOWABLE_WAVELENGTH:
                    raise ParameterError("wavelength", "Wavelength must be between %f and %f" % (PredefinedWavelengths.MIN_ALLOWABLE_WAVELENGTH, PredefinedWavelengths.MAX_ALLOWABLE_WAVELENGTH))
                type = "-1"
                data = "%f" % start_wavelength
                min_wv = None
                max_wv = None
        else:
            if start_wavelength > PredefinedWavelengths.MAX_ALLOWABLE_WAVELENGTH or start_wavelength < PredefinedWavelengths.MIN_ALLOWABLE_WAVELENGTH or end_wavelength > PredefinedWavelengths.MAX_ALLOWABLE_WAVELENGTH or end_wavelength < PredefinedWavelengths.MIN_ALLOWABLE_WAVELENGTH:
                raise ParameterError("wavelength", "Wavelength must be between %f and %f" % (PredefinedWavelengths.MIN_ALLOWABLE_WAVELENGTH, PredefinedWavelengths.MAX_ALLOWABLE_WAVELENGTH))
            min_wv = start_wavelength
            max_wv = end_wavelength
            if filter == None:
                # They haven't given a filter, so assume filter is constant at 1
                type = "0 constant filter function"
                data = "%f %f" % (start_wavelength, end_wavelength)
            else:
                # Filter has been given, so we must use it.
                # We assume filter has been given at 2.5nm intervals
                type = "1 User's defined filtered function"
                data = """%f %f
    %s""" % (start_wavelength, end_wavelength, " ".join(map(str,filter)))
    

    if data == None:
        return_string =  type
    else:
        return_string =  """%s
%s\n""" % (type, data)

    return (return_string, min_wv, max_wv)

class PredefinedWavelengths:
    MAX_ALLOWABLE_WAVELENGTH = 4
    MIN_ALLOWABLE_WAVELENGTH = 0.2
  
    # All of the predefined wavelengths
    # CONSTANT_NAME = (ID for Constant, Start Wavelength, End Wavelength)
    METEOSAT_VISIBLE = (-2, 0.35, 1.11)
    GOES_EAST_VISIBLE = (-3, 0.49, 0.9)
    GOES_WEST_VISIBLE = (-4, 0.49, 0.9)
    AVHRR_NOAA6_B1 = (-5, 0.55, 0.75)
    AVHRR_NOAA6_B2 = (-6, 0.69, 1.12)
    AVHRR_NOAA7_B1 = (-7, 0.5, 0.8)
    AVHRR_NOAA7_B2 = (-8, 0.64, 1.17)
    AVHRR_NOAA8_B1 = (-9, 0.54, 1.01)
    AVHRR_NOAA8_B2 = (-10, 0.68, 1.12)
    AVHRR_NOAA9_B1 = (-11, 0.53, 0.81)
    AVHRR_NOAA9_B2 = (-12, 0.68, 1.17)
    AVHRR_NOAA10_B1 = (-13, 0.53, 0.78)
    AVHRR_NOAA10_B2 = (-14, 0.6, 1.19)
    AVHRR_NOAA11_B1 = (-15, 0.54, 0.82)
    AVHRR_NOAA11_B2 = (-16, 0.6, 1.12)
    SPOT_HRV1_B1 = (-17, 0.47, 0.65)
    SPOT_HRV1_B2 = (-18, 0.6, 0.72)
    SPOT_HRV1_B3 = (-19, 0.73, 0.93)
    SPOT_HRV1_PAN = (-20, 0.47, 0.79)
    SPOT_HRV2_B1 = (-21, 0.47, 0.65)
    SPOT_HRV2_B2 = (-22, 0.59, 0.73)
    SPOT_HRV2_B3 = (-23, 0.74, 0.94)
    SPOT_HRV2_PAN = (-24, 0.47, 0.79)
    LANDSAT_TM_B1 = (-25, 0.43, 0.56)
    LANDSAT_TM_B2 = (-26, 0.5, 0.65)
    LANDSAT_TM_B3 = (-27, 0.58, 0.74)
    LANDSAT_TM_B4 = (-28, 0.73, 0.95)
    LANDSAT_TM_B5 = (-29, 1.5025, 1.89)
    LANDSAT_TM_B7 = (-30, 1.95, 2.41)
    LANDSAT_MSS_B1 = (-31, 0.475, 0.64)
    LANDSAT_MSS_B2 = (-32, 0.58, 0.75)
    LANDSAT_MSS_B3 = (-33, 0.655, 0.855)
    LANDSAT_MSS_B4 = (-34, 0.785, 1.1)
    ER2_MAS_B1 = (-35, 0.5025, 0.5875)
    ER2_MAS_B2 = (-36, 0.6075, 0.7)
    ER2_MAS_B3 = (-37, 0.83, 0.9125)
    ER2_MAS_B4 = (-38, 0.9, 0.9975)
    ER2_MAS_B5 = (-39, 1.82, 1.9575)
    ER2_MAS_B6 = (-40, 2.0950, 2.1925)
    ER2_MAS_B7 = (-41, 3.58, 3.87)
    MODIS_B1 = (-42, 0.61, 0.685)
    MODIS_B2 = (-43, 0.82, 0.9025)
    MODIS_B3 = (-44, 0.45, 0.4825)
    MODIS_B4 = (-45, 0.54, 0.57)
    MODIS_B5 = (-46, 1.2150, 1.27)
    MODIS_B6 = (-47, 1.6, 1.665)
    MODIS_B7 = (-48, 2.0575, 2.1825)
    MODIS_B8 = (-49, 0.4025, 0.4225)
    AVHRR_NOAA12_B1 = (-50, 0.5, 1.0)
    AVHRR_NOAA12_B2 = (-51, 0.65, 1.12)
    AVHRR_NOAA14_B1 = (-52, 0.5, 1.11)
    AVHRR_NOAA14_B2 = (-53, 0.68, 1.1)
    POLDER_B1 = (-54, 0.4125, 0.4775)
    POLDER_B2 = (-55, 0.41, 0.5225)
    POLDER_B3 = (-56, 0.5325, 0.595)
    POLDER_B4 = (-57, 0.63, 0.7025)
    POLDER_B5 = (-58, 0.745, 0.78)
    POLDER_B6 = (-59, 0.7, 0.83)
    POLDER_B7 = (-60, 0.81, 0.92)
    POLDER_B8 = (-61, 0.8650, 0.94)
    SEAWIFS_B1 = (-62, 0.3825, 0.7)
    SEAWIFS_B2 = (-63, 0.38, 0.58)
    SEAWIFS_B3 = (-64, 0.38, 1.02)
    SEAWIFS_B4 = (-65, 0.38, 1.02)
    SEAWIFS_B5 = (-66, 0.3825, 1.15)
    SEAWIFS_B6 = (-67, 0.3825, 1.05)
    SEAWIFS_B7 = (-68, 0.38, 1.15)
    SEAWIFS_B8 = (-69, 0.38, 1.15)
    AATSR_B1 = (-70, 0.525, 0.5925)
    AATSR_B2 = (-71, 0.6275, 0.6975)
    AATSR_B3 = (-72, 0.8325, 0.9025)
    AATSR_B4 = (-73, 1.4475, 1.7775)
    MERIS_B1 = (-74, 0.412, 0.412+0.00998)
    MERIS_B2 = (-75, 0.442, 0.442+0.00997)
    MERIS_B3 = (-76, 0.489, 0.489+0.00997)
    MERIS_B4 = (-77, 0.509, 0.509+0.00997)
    MERIS_B5 = (-78, 0.559, 0.559+0.00997)
    MERIS_B6 = (-79, 0.619, 0.619+0.00997)
    MERIS_B7 = (-80, 0.664, 0.664+0.00998)
    MERIS_B8 = (-81, 0.681, 0.681+0.00749)
    MERIS_B9 = (-82, 0.708, 0.708+0.00999)
    MERIS_B10 = (-83, 0.753, 0.753+0.00749)
    MERIS_B11 = (-84, 0.760, 0.760+0.00374)
    MERIS_B12 = (-85, 0.778, 0.778+0.00150)
    MERIS_B13 = (-86, 0.865, 0.865+0.002)
    MERIS_B14 = (-87, 0.885, 0.885+0.001)
    MERIS_B15 = (-88, 0.9, 0.9+0.001)
    GLI_B1 = (-89, 0.37, 0.3925)
    GLI_B2 = (-90, 0.3875, 0.4125)
    GLI_B3 = (-91, 0.3975, 0.4275)
    GLI_B4 = (-92, 0.4475, 0.505)
    GLI_B5 = (-93, 0.4475, 0.46)
    GLI_B6 = (-94, 0.475, 0.505)
    GLI_B7 = (-95, 0.5075, 0.5325)
    GLI_B8 = (-96, 0.5265, 0.56)
    GLI_B9 = (-97, 0.5475, 0.5825)
    GLI_B10 = (-98, 0.61, 0.64)
    GLI_B11 = (-99, 0.6525, 0.6825)
    GLI_B12 = (-100, 0.665, 0.695)
    GLI_B13 = (-101, 0.6625, 0.6975)
    GLI_B14 = (-102, 0.6925, 0.7275)
    GLI_B15 = (-103, 0.6925, 0.7275)
    GLI_B16 = (-104, 0.7325, 0.7675)
    GLI_B17 = (-105, 0.75, 0.775)
    GLI_B18 = (-106, 0.84, 0.8925)
    GLI_B19 = (-107, 0.85, 0.88)
    GLI_B20 = (-108, 0.415, 0.5075)
    GLI_B21 = (-109, 0.505, 0.58)
    GLI_B22 = (-110, 0.6075, 0.715)
    GLI_B23 = (-111, 0.745, 0.9075)
    GLI_B24 = (-112, 1.03, 1.07)
    GLI_B25 = (-113, 1.085, 1.19)
    GLI_B26 = (-114, 1.22, 1.2625)
    GLI_B27 = (-115, 1.3475, 1.415)
    GLI_B28 = (-116, 1.515, 1.77)
    GLI_B29 = (-117, 2.055, 2.345)
    GLI_B30 = (-118, 3.22, 4.0)
    ALI_B1P = (-119, 0.4225, 0.4625)
    ALI_B1 = (-120, 0.4325, 0.550)
    ALI_B2 = (-121, 0.5, 0.63)
    ALI_B3 = (-122, 0.5775, 0.750)
    ALI_B4 = (-123, 0.7525, 0.8375)
    ALI_B4P = (-124, 0.8025, 0.935)
    ALI_B5P = (-125, 1.130, 1.345)
    ALI_B5 = (-126, 1.47, 1.820)
    ALI_B7 = (-127, 1.98, 2.53)
    ASTER_B1 = (-128, 0.485, 0.6425)
    ASTER_B2 = (-129, 0.590, 0.730)
    ASTER_B3N = (-130, 0.720, 0.9075)
    ASTER_B3B = (-131, 0.720, 0.9225)
    ASTER_B4 = (-132, 1.57, 1.7675)
    ASTER_B5 = (-133, 2.120, 2.2825)
    ASTER_B6 = (-134, 2.150, 2.295)
    ASTER_B7 = (-135, 2.210, 2.39)
    ASTER_B8 = (-136, 2.250, 2.244)
    ASTER_B9 = (-137, 2.2975, 2.4875)
    LANDSAT_ETM_B1 = (-138, 0.435, 0.52)
    LANDSAT_ETM_B2 = (-139, 0.5, 0.6225)
    LANDSAT_ETM_B3 = (-140, 0.615, 0.7025)
    LANDSAT_ETM_B4 = (-141, 0.74, 0.9125)
    LANDSAT_ETM_B5 = (-142, 1.51, 1.7875)
    LANDSAT_ETM_B7 = (-143, 2.015, 2.3775)
    HYPBLUE_B1 = (-144, 0.4375, 0.5)
    HYPBLUE_B2 = (-145, 0.435, 0.52)
    SPOT_VGT_B1 = (-146, 0.4175, 0.5)
    SPOT_VGT_B2 = (-147, 0.5975, 0.7675)
    SPOT_VGT_B3 = (-148, 0.7325, 0.9575)
    SPOT_VGT_B4 = (-149, 1.5225, 1.8)
    VIIRS_BM1 = (-150, 0.4025, 0.4225)
    VIIRS_BM2 = (-151, 0.4350, 0.4550)
    VIIRS_BM3 = (-152, 0.4775, 0.4975)
    VIIRS_BM4 = (-153, 0.5450, 0.565)
    VIIRS_BM5 = (-154, 0.6625, 0.6825)
    VIIRS_BM6 = (-155, 0.7375, 0.7525)
    VIIRS_BM7 = (-156, 0.8450, 0.8850)
    VIIRS_BM8 = (-157, 1.23, 1.25)
    VIIRS_BM9 = (-158, 1.37, 1.385)
    VIIRS_BM10 = (-159, 1.58, 1.64)
    VIIRS_BM11 = (-160, 2.225, 2.275)
    VIIRS_BM12 = (-161, 3.61, 3.79)
    VIIRS_BI1 = (-162, 0.6, 0.68)
    VIIRS_BI2 = (-163, 0.845, 0.885)
    VIIRS_BI3 = (-164, 1.58, 1.64)
    VIIRS_BI4 = (-165, 3.55, 3.93)