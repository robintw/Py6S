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

    @classmethod
    def MultimodalLogNormalDistribution(cls, rmin, rmax):
      return AerosolDistribution(rmin, rmax, 8)
      
    @classmethod
    def ModifiedGammaDistribution(cls, rmin, rmax):
      return AerosolDistribution(rmin, rmax, 9)
      
    @classmethod
    def JungePowerLawDistribution(cls, rmin, rmax):
      return AerosolDistribution(rmin, rmax, 10)
    
    class AerosolDistribution:
      """Stores data regarding a specific Aerosol Distribution.
      
      Used by the following methods:
      MultimodalLogNormalDistribution
      ModifiedGammaDistribution
      JungePowerLawDistribution
      
      """
      numtype = 0
      rmin = 0
      rmax = 0
      values = []
      
      def __init__(self, rmin, rmax, numtype):
        """Initialise an Aerosol Distribution with various parameters.
        
        Should not be called directly - use one of the methods like AeroProfile.MultimodalLogNormalDistribution() instead.
        
        Arguments:
        rmin -- The minimum aerosol radius
        rmax -- The maximum aerosol radius
        numtype -- The type of aerosol distribution (eg. 8 for Multimodal Log Normal)
        
        """
        self.rmin = rmin
        self.rmax = rmax
        self.numtype = numtype
        
      def add_component(self, rmean, sigma, percentage_density, refr_real, refr_imag):
        """Adds a component to the aerosol distribution.
        
        For the arguments that are wavelength-dependent, 20 values should be given at the following wavelengths:
        !!!! PUT WAVELENGTHS HERE
        
        Arguments:
        rmean -- The mean radius of the aerosols
        sigma -- Sigma, as defined by the distribution (Log Normal etc)
        percentage_density -- The percentage density of the aerosol
        refr_real -- A 20-element iterable giving the real part of the refractive indices at the specified wavelengths (see above)
        refr_imag -- A 20-element iterable giving the imaginary part of the refractive indices at the specified wavelengths (see above)
        
        """
        if len(self.values) >= 4:
          raise ParameterError("Aerosol Distribution components", "You can only add a maximum of 4 components")
        
        if len(refr_real) != 20:
          raise ParameterError("Aerosol Distribution Real Refractive Index", "You must specify the real part of the Refractive Index at 20 wavelengths.")
        
        if len(refr_imag) != 20:
          raise ParameterError("Aerosol Distribution Imaginary Refractive Index", "You must specify the imaginary part of the Refractive Index at 20 wavelengths.")
        
        comp = "%f %f %f\n" % (rmean, sigma, percentage_density)
        real = map(str, refr_real)
        imag = map(str, refr_imag)
        comp += ' '.join(real) + '\n'
        comp += ' '.join(imag) + '\n'
        
        self.values.append(comp)
        
      def __str__(self):
        result = "%d\n%f %f %d\n" % (self.numtype, self.rmin, self.rmax, len(self.values))
        components = ''.join(self.values)
        return result + components
    
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
      