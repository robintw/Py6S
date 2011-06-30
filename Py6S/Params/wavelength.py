from Py6S.sixs_exceptions import *
import collections

class WavelengthType:
    MAX_ALLOWABLE_WAVELENGTH = 4
    MIN_ALLOWABLE_WAVELENGTH = 0.2
    
    @classmethod
    def Wavelength(cls, start_wavelength, end_wavelength=None, filter=None):
        if end_wavelength == None:
            # No end wavelength given, so it's either monochromatic or a pre-defined wavelength
            if start_wavelength < 0:
                # It's a pre-defined wavelength
                type = "%d (Chosen Band)\n" % (-1 *start_wavelength)
                data = None
            else:
                # It's simply a wavelength value
                if start_wavelength > cls.MAX_ALLOWABLE_WAVELENGTH or start_wavelength < cls.MIN_ALLOWABLE_WAVELENGTH:
                    raise ParameterError("wavelength", "Wavelength must be between %f and %f" % (cls.MIN_ALLOWABLE_WAVELENGTH, cls.MAX_ALLOWABLE_WAVELENGTH))
                type = "-1"
                data = "%f" % start_wavelength
        else:
            if start_wavelength > cls.MAX_ALLOWABLE_WAVELENGTH or start_wavelength < cls.MIN_ALLOWABLE_WAVELENGTH or end_wavelength > cls.MAX_ALLOWABLE_WAVELENGTH or end_wavelength < cls.MIN_ALLOWABLE_WAVELENGTH:
                raise ParameterError("wavelength", "Wavelength must be between %f and %f" % (cls.MIN_ALLOWABLE_WAVELENGTH, cls.MAX_ALLOWABLE_WAVELENGTH))
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
            return type
        else:
            return """%s
%s\n""" % (type, data)


    # All of the predefined wavelengths
    METEOSAT_VISIBLE = -2
    GOES_EAST_VISIBLE = -3
    GOES_WEST_VISIBLE = -4
    AVHRR_NOAA6_B1 = -5
    AVHRR_NOAA6_B2 = -6
    AVHRR_NOAA7_B1 = -7
    AVHRR_NOAA7_B2 = -8
    AVHRR_NOAA8_B1 = -9
    AVHRR_NOAA8_B2 = -10
    AVHRR_NOAA9_B1 = -11
    AVHRR_NOAA9_B2 = -12
    AVHRR_NOAA10_B1 = -13
    AVHRR_NOAA10_B2 = -14
    AVHRR_NOAA11_B1 = -15
    AVHRR_NOAA11_B2 = -16
    SPOT_HRV1_B1 = -17
    SPOT_HRV1_B2 = -18
    SPOT_HRV1_B3 = -19
    SPOT_HRV1_PAN = -20
    SPOT_HRV2_B1 = -21
    SPOT_HRV2_B2 = -22
    SPOT_HRV2_B3 = -23
    SPOT_HRV2_PAN = -24
    LANDSAT_TM_B1 = -25
    LANDSAT_TM_B2 = -26
    LANDSAT_TM_B3 = -27
    LANDSAT_TM_B4 = -28
    LANDSAT_TM_B5 = -29
    LANDSAT_TM_B7 = -30
    LANDSAT_MSS_B1 = -31
    LANDSAT_MSS_B2 = -32
    LANDSAT_MSS_B3 = -33
    LANDSAT_MSS_B4 = -34
    ER2_MAS_B1 = -35
    ER2_MAS_B2 = -36
    ER2_MAS_B3 = -37
    ER2_MAS_B4 = -38
    ER2_MAS_B5 = -39
    ER2_MAS_B6 = -40
    ER2_MAS_B7 = -41
    MODIS_B1 = -42
    MODIS_B2 = -43
    MODIS_B3 = -44
    MODIS_B4 = -45
    MODIS_B5 = -46
    MODIS_B6 = -47
    MODIS_B7 = -48
    MODIS_B8 = -49
    AVHRR_NOAA12_B1 = -50
    AVHRR_NOAA12_B2 = -51
    AVHRR_NOAA14_B1 = -52
    AVHRR_NOAA14_B2 = -53
    POLDER_B1 = -54
    POLDER_B2 = -55
    POLDER_B3 = -56
    POLDER_B4 = -57
    POLDER_B5 = -58
    POLDER_B6 = -59
    POLDER_B7 = -60
    POLDER_B8 = -61
    SEAWIFS_B1 = -62
    SEAWIFS_B2 = -63
    SEAWIFS_B3 = -64
    SEAWIFS_B4 = -65
    SEAWIFS_B5 = -66
    SEAWIFS_B6 = -67
    SEAWIFS_B7 = -68
    SEAWIFS_B8 = -69
    AATSR_B1 = -70
    AATSR_B2 = -71
    AATSR_B3 = -72
    AATSR_B4 = -73
    MERIS_B1 = -74
    MERIS_B2 = -75
    MERIS_B3 = -76
    MERIS_B4 = -77
    MERIS_B5 = -78
    MERIS_B6 = -79
    MERIS_B7 = -80
    MERIS_B8 = -81
    MERIS_B9 = -82
    MERIS_B10 = -83
    MERIS_B11 = -84
    MERIS_B12 = -85
    MERIS_B13 = -86
    MERIS_B14 = -87
    MERIS_B15 = -88
    GLI_B1 = -89
    GLI_B2 = -90
    GLI_B3 = -91
    GLI_B4 = -92
    GLI_B5 = -93
    GLI_B6 = -94
    GLI_B7 = -95
    GLI_B8 = -96
    GLI_B9 = -97
    GLI_B10 = -98
    GLI_B11 = -99
    GLI_B12 = -100
    GLI_B13 = -101
    GLI_B14 = -102
    GLI_B15 = -103
    GLI_B16 = -104
    GLI_B17 = -105
    GLI_B18 = -106
    GLI_B19 = -107
    GLI_B20 = -108
    GLI_B21 = -109
    GLI_B22 = -110
    GLI_B23 = -111
    GLI_B24 = -112
    GLI_B25 = -113
    GLI_B26 = -114
    GLI_B27 = -115
    GLI_B28 = -116
    GLI_B29 = -117
    GLI_B30 = -118
    ALI_B1P = -119
    ALI_B1 = -120
    ALI_B2 = -121
    ALI_B3 = -122
    ALI_B4 = -123
    ALI_B4P = -124
    ALI_B5P = -125
    ALI_B5 = -126
    ALI_B7 = -127
    ASTER_B1 = -128
    ASTER_B2 = -129
    ASTER_B3N = -130
    ASTER_B3B = -131
    ASTER_B4 = -132
    ASTER_B5 = -133
    ASTER_B6 = -134
    ASTER_B7 = -135
    ASTER_B8 = -136
    ASTER_B9 = -137
    ETM_B1 = -138
    ETM_B2 = -139
    ETM_B3 = -140
    ETM_B4 = -141
    ETM_B5 = -142
    ETM_B7 = -143
    HYPBLUE_B1 = -144
    HYPBLUE_B2 = -145
    SPOT_VGT_B1 = -146
    SPOT_VGT_B2 = -147
    SPOT_VGT_B3 = -148
    SPOT_VGT_B4 = -149
    VIIRS_BM1 = -150
    VIIRS_BM2 = -151
    VIIRS_BM3 = -152
    VIIRS_BM4 = -153
    VIIRS_BM5 = -154
    VIIRS_BM6 = -155
    VIIRS_BM7 = -156
    VIIRS_BM8 = -157
    VIIRS_BM9 = -158
    VIIRS_BM10 = -159
    VIIRS_BM11 = -160
    VIIRS_BM12 = -161
    VIIRS_BI1 = -162
    VIIRS_BI2 = -163
    VIIRS_BI3 = -164
    VIIRS_BI4 = -165