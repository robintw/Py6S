from Py6S.sixs_exceptions import *
import collections

class GroundReflectance:
    """Produces strings for the input file for a number of different ground reflectance scenarios.
    
    Options are:
    
     - Homogeneous
      - Lambertian
      - BRDF
       - Walthall et al. model
       - Rahman et al. model
       - ...
     - Heterogeneous
      - Lambertian
    
    These are combined to give function names like:
    
    C{HomogeneousLambertian}
    
    or
    
    C{HomogenousWalthall}
        
    The standard functions (HomogeneousLambertian and HeterogeneousLambertian) will decide what to do
    based on the types of inputs they are given. For example, HomogeneousLambertian can be used as follows:
    
    >>> model.ground_reflectance = GroundReflectance.HomogeneousLambertian(0.7)
    
    which will represent a spectrally-constant reflectance of 0.7
    
    >>> model.ground_reflectance = GroundReflectance.HomogeneousLambertian(GroundReflectance.GreenVegetation)
    
    which will represent a built-in averaged green vegetation spectrum.
    
    or
    
    >>> model.ground_reflectance = GroundReflectance.HomogeneousLambertian([0.6, 0.8, 0.34, 0.453])
    
    which will represent a user-defined spectrum. This should be given in micrometers, with steps of 2.5nm.
    """
    
    GreenVegetation = -1
    ClearWater = -2
    Sand = -3
    LakeWater = -4

    
    @classmethod
    def HomogeneousLambertian(cls, ro):
        """Provides parameterisation for homogeneous Lambertian (ie. uniform BRDF) surfaces.
        
        The single argument can be either:
         - A single float value (for example, 0.634), in which case it is interpreted as a spectrally-constant
         reflectance value.
         - A constant provided by one of C{GroundReflectance.GreenVegetation}, C{GroundReflectance.ClearWater}, C{GroundReflectance.Sand} or C{GroundReflectance.LakeWater}.
         In which case a built-in spectrum of the specified material is used.
         - An array of values (for example, [0.67, 0.85, 0.34, 0.65]) in which case the values are taken to be reflectances across the whole wavelength range at a spacing of 0.25nm.
        """
        ro_type, ro_value = cls.GetTargetTypeAndValues(ro)        
        return """0 Homogeneous surface
0 No directional effects
%s
%s\n""" % (ro_type, ro_value)

    @classmethod
    def HeterogeneousLambertian(cls, radius, ro_target, ro_env):
        """Provides parameterisation for heterogeneous Lambertian (ie. uniform BRDF) surfaces.
        
        These surfaces are modelled in 6S as a circular target surrounded by a differently reflecting
        environment. Thus three parameters are required:
         - The radius of the target (in km)
         - The reflectance of the target
         - The reflectance of the environment
        
        Both of the reflectances can be set to any of the following:
         - A single float value (for example, 0.634), in which case it is interpreted as a spectrally-constant
         reflectance value.
         - A constant provided by one of C{GroundReflectance.GreenVegetation}, C{GroundReflectance.ClearWater}, C{GroundReflectance.Sand} or C{GroundReflectance.LakeWater}.
         In which case a built-in spectrum of the specified material is used.
         - An array of values (for example, [0.67, 0.85, 0.34, 0.65]) in which case the values are taken to be reflectances across the whole wavelength range at a spacing of 0.25nm.
        """
        ro_target_type, ro_target_values = cls.GetTargetTypeAndValues(ro_target)
        ro_env_type, ro_env_values = cls.GetTargetTypeAndValues(ro_env)

        return """1 (Non homogeneous surface)
%s %s %f (ro1 ro2 radius)
%s
%s""" % (ro_target_type, ro_env_type, radius, ro_target_values, ro_env_values)

    @classmethod
    def HomogeneousWalthall(cls, param1, param2, param3, albedo):
        return """0 Homogeneous surface
1 (directional effects)
4 (Walthall et al. model)
%f %f %f %f""" % (param1, param2, param3, albedo)

    @classmethod
    def HomogeneousHapke(cls, albedo, assymetry, amplitude, width):
        return """0 Homogeneous surface
1 (directional effects)
1 (Hapke model)
%f %f %f %f""" % (albedo, assymetry, amplitude, width)

    @classmethod
    def HomogeneousRoujean(cls, albedo, k1, k2):
        return """0 Homogeneous surface
1 (directional effects)
3 (Roujean model)
%f %f %f""" % (albedo, k1, k2)

    @classmethod
    def HomogeneousMinnaert(cls, par1, par2):
        return """0 Homogeneous surface
1 (directional effects)
5 (Minnaert model)
%f %f""" % (par1, par2)

    @classmethod
    def HomogeneousMODISBRDF(cls, par1, par2, par3):
        return """0 Homogeneous surface
1 (directional effects)
10 (MODIS BRDF model)
%f %f %f""" % (par1, par2, par3)

    @classmethod
    def HomogeneousmOcean(cls, wind_speed, wind_azimuth, salinity, pigment_concentration):
        return """0 Homogeneous surface
1 (directional effects)
6 (MODIS BRDF model)
%f %f %f %f""" % (wind_speed, wind_azimuth, salinity, pigment_concentration)

    @classmethod
    def GetTargetTypeAndValues(cls, target):
        # If it's iterable then it's a list (or tuple), so a spectrum has been given
        if isinstance(target, collections.Iterable):
            target_type = "-1"
            target_value = " ".join(map(str,target))
        else:
            # If it's less than zero then it must be one of the predefined types
            if target < 0:
                target_type = str(-1 * target)
                target_value = ""
            # Otherwise it must be a constant ro
            else:
                target_type = "0"
                target_value = target
        
        return (target_type, target_value)