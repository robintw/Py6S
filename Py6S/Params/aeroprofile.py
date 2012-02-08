from collections import defaultdict
from sixs_exceptions import *


class AeroProfile:
    """Stores an enumeration for the pre-specified aerosol model types."""

    @classmethod
    def NoAerosol(cls):
      return "0 (No Aerosol)"

    @classmethod
    def Continental(cls):
      return "1 (Continental)"

    @classmethod
    def Maritime(cls):
      return "2 (Maritime)"
      
    @classmethod      
    def Urban(cls):
      return "3 (Urban)"
    
    @classmethod
    def User(cls, **kwargs):
        d = defaultdict(lambda: 0, kwargs)
        
        dust = d['dust']
        water = d['water']
        oceanic = d['oceanic']
        soot = d['soot']
        
        if (((dust + water + oceanic + soot) - 1) > 0.01):
          raise ParameterError("Aerosol Profile", "User aerosol components don't sum to 1.0")
        
        return "4 (User's Components)\n%f, %f, %f, %f" % (dust, water, oceanic, soot)

    @classmethod
    def Desert(cls):
      return "5 (Desert)"

    @classmethod
    def BiomassBurning(cls):
      return "6 (Biomass Burning)"

    @classmethod
    def Stratospheric(cls):
      return "7 (Stratospheric)"