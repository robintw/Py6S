from Py6S.sixs_exceptions import *

MAX_ALLOWABLE_WAVELENGTH = 4
MIN_ALLOWABLE_WAVELENGTH = 0.2

class GroundReflectance:
    # Max and Min allowable wavelengths in micrometres

    GreenVegetation = -1
    ClearWater = -2
    Sand = -3
    LakeWater = -4

    
    @classmethod
    def HomogeneousLambertianConstant(cls, ro):
        if ro > MAX_ALLOWABLE_WAVELENGTH or ro < MIN_ALLOWABLE_WAVELENGTH:
            raise ParameterError("ro", "Wavelength must be between %f and %f" (MIN_ALLOWABLE_WAVELENGTH, MAX_ALLOWABLE_WAVELENGTH))
        return """0 Homogeneous surface
0 No directional effects
0 constant value for ro
%f\n""" % ro

    @classmethod
    def HeterogeneousLambertianConstant(cls, radius, ro_target, ro_env):
        if ro_target > MAX_ALLOWABLE_WAVELENGTH or ro_target < MIN_ALLOWABLE_WAVELENGTH:
            raise ParameterError("ro_target", "Wavelength must be between %f and %f" (MIN_ALLOWABLE_WAVELENGTH, MAX_ALLOWABLE_WAVELENGTH))
        if ro_env > MAX_ALLOWABLE_WAVELENGTH or ro_env < MIN_ALLOWABLE_WAVELENGTH:
            raise ParameterError("ro_env", "Wavelength must be between %f and %f" (MIN_ALLOWABLE_WAVELENGTH, MAX_ALLOWABLE_WAVELENGTH))
        return """1 (Non homogeneous surface)
0 0 %f (ro1 ro2 radius)
%f
%f""" % (radius, ro_target, ro_env)


    @classmethod  
    def HomogenousLambertianSpectra(cls, spectra):
        # We assume here that the array was given in 2.5nm steps
        if max(spectra) > MAX_ALLOWABLE_WAVELENGTH or min(spectra) < MIN_ALLOWABLE_WAVELENGTH:
            raise ParameterError("spectra", "Wavelength must be between %f and %f" % (MIN_ALLOWABLE_WAVELENGTH, MAX_ALLOWABLE_WAVELENGTH))
        
        return """0 Homogeneous surface
0 No directional effects
-1 (ro by step of 2.5nm)
%f %f
%s""" % (min(spectra), max(spectra), " ".join(map(str,spectra)))

    @classmethod  
    def HomogenousLambertianPredefinedSpectra(cls, spectra_type):
        if spectra_type > 0:
            raise ParameterError("spectra_type", "Undefined mean spectra selected")
        value = -1 * spectra_type
        return """0 Homogeneous surface
0 No directional effects
%d (mean spectral value)""" % value