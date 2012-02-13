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
      """Set 6S to use a predefined aerosol type, one of the constants defined in this class.
      
      Arguments:
      type -- the predefined aerosol type, one of the constants defined in this class
      
      Example usage:
      s.aeroprofile = AeroProfile.PredefinedType(AeroProfile.Urban)
      
      """
      return "%d" % type
    
    @classmethod
    def User(cls, **kwargs):
        """Set 6S to use a user-defined aerosol profile based on proportions of standard aerosol components.
        
        The profile is set as a mixture of pre-defined components, each given as an optional keyword.
        Not all keywords need to be given, but the values for the keywords given must sum to 1, or a
        ParameterError will be raised.
        
        Optional keywords:
        dust -- The proportion of dust-like aerosols
        water -- The proportion of water-like aerosols
        oceanic -- The proportion of oceanic aerosols
        soot -- The proportion of soot-like aerosols
        
        Example usage:
        s.aeroprofile = AeroProfile.User(dust=0.3, oceanic=0.7)
        
        s.aeroprofile = AeroProfile.User(soot = 0.1, water = 0.3, oceanic = 0.05, dust = 0.55)
        
        """
        d = defaultdict(lambda: 0, kwargs)
        
        dust = d['dust']
        water = d['water']
        oceanic = d['oceanic']
        soot = d['soot']
        
        if (((dust + water + oceanic + soot) - 1) > 0.01):
          raise ParameterError("Aerosol Profile", "User aerosol components don't sum to 1.0")
        
        return "4 (User's Components)\n%f, %f, %f, %f" % (dust, water, oceanic, soot)

    class UserProfile:
      """Set 6S to use a user-defined aerosol profile, with differing AOTs over the height of the profile.
      
      Arguments:
      atype --  Aerosol type to be used for all layers. Must be one of the pre-defined types defined in this class.
      
      Methods:
      add_layer -- Adds a layer to the user-defined aerosol profile, with the specified height and aerosol optical thickness.
      
      Example usage:
      s.aeroprofile = AeroProfile.UserProfile(AeroProfile.Maritime)
      s.aeroprofile.add_layer(5, 0.34) # Add a 5km-thick layer with an AOT of 0.34
      s.aeroprofile.add_layer(10, 0.7) # Add a 10km-thick layer with an AOT of 0.7
      s.aeroprofile.add_layer(100, 0.01) # Add a 100km-thick layer with an AOT of 0.01
      
      """
      values = []
      aerotype = 0
      
      def __init__(self, atype):
        """Initialises the user-defined aerosol profile to a specific aerosol type.
        
        Arguments:
        atype --  Aerosol type to be used for all layers. Must be one of the pre-defined types defined in this class.
        
        """
        self.aerotype = atype
      
      def add_layer(self, height, optical_thickness):
        """Adds a layer to the user-defined profile.
        
        Arguments:
        height - Height of the layer (in km)
        optical_thickness - Optical thickness of the layer
        
        Example usage:
        s.aeroprofile.add_layer(5, 0.34) # Add a 5km-thick layer with an AOT of 0.34
        """
        self.values.append((height, optical_thickness))
      
      def __str__(self):
        res = ""
        for val in self.values:
          res = res + "%f %f %d\n" % (val[0], val[1], self.aerotype)
        
        return res
      