from Py6S.sixs_exceptions import *
import collections

MAX_ALLOWABLE_WAVELENGTH = 4
MIN_ALLOWABLE_WAVELENGTH = 0.2

class GroundReflectance:
    # Max and Min allowable wavelengths in micrometres

    GreenVegetation = -1
    ClearWater = -2
    Sand = -3
    LakeWater = -4

    
    @classmethod
    def HomogeneousLambertian(cls, ro):
        ro_type, ro_value = cls.GetTargetTypeAndValues(ro)        
        return """0 Homogeneous surface
0 No directional effects
%s
%s\n""" % (ro_type, ro_value)

    @classmethod
    def HeterogeneousLambertian(cls, radius, ro_target, ro_env):
        ro_target_type, ro_target_values = cls.GetTargetTypeAndValues(ro_target)
        ro_env_type, ro_env_values = cls.GetTargetTypeAndValues(ro_env)

        return """1 (Non homogeneous surface)
%s %s %f (ro1 ro2 radius)
%s
%s""" % (ro_target_type, ro_env_type, radius, ro_target_values, ro_env_values)


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