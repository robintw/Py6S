from collections import defaultdict
from sixs_exceptions import *


class AeroProfile:
    """Class representing options for Aerosol Profiles"""

    @classmethod
    def NoAerosol(cls):
      """No aerosols"""
      return "0 (No Aerosol)"

    @classmethod
    def Continental(cls):
      """Continental aerosol profile"""
      return "1 (Continental)"

    @classmethod
    def Maritime(cls):
      """Maritime aerosol profile"""
      return "2 (Maritime)"
      
    @classmethod      
    def Urban(cls):
      """Urban aerosol profile"""
      return "3 (Urban)"
    
    @classmethod
    def User(cls, **kwargs):
        """User specified aerosol profile, as a mixture of pre-defined components. Call using keyword arguments for the
        components of: dust, water, oceanic and soot. For example AeroProfile.User(dust=0.3, oceanic=0.7)."""
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
      """Desert aerosol profile"""
      return "5 (Desert)"

    @classmethod
    def BiomassBurning(cls):
      """Biomass Burning aerosol profile"""
      return "6 (Biomass Burning)"

    @classmethod
    def Stratospheric(cls):
      """Stratospheric aerosol profile"""
      return "7 (Stratospheric)"