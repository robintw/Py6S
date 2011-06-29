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
                pass
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

        return """%s
%s\n""" % (type, data)