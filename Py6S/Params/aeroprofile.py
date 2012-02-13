from collections import defaultdict
from sixs_exceptions import *


class AeroProfile:
    """Class representing options for Aerosol Profiles"""
    
    NoAerosols = 0
    Continental = 1
    Maritime = 2
    Urban = 3
    Desert = 5
    BiomassBurning = 6
    Stratospheric = 7
    
    @classmethod
    def PredefinedType(cls, type):
      """Use a predefined aerosol type, one of the constants defined in this class"""
      return "%d" % type
    
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

    class UserProfile:
      """User-defined aerosol profile, with types, heights and AOTs"""
      values = []
      aerotype = 0
      
      def __init__(self, atype):
        """Initialises the user-defined aerosol profile to a specific aerosol type"""
        self.aerotype = atype
      
      def add_layer(self, height, optical_thickness):
        """Adds a layer to the user-defined profile. Arguments must be:
        Height of the layer
        Optical thickness of the layer"""
        self.values.append((height, optical_thickness))
      
      def __str__(self):
        res = ""
        for val in self.values:
          res = res + "%f %f %d\n" % (val[0], val[1], self.aerotype)
        
        return res
      