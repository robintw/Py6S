from sixs_exceptions import *

class AtmosProfile:
    """Stores a enumeration for the pre-specified atmospheric model types"""
    NoGaseousAbsorption=0 
    Tropical=1
    MidlatitudeSummer=2
    MidlatitudeWinter=3
    SubarcticSummer=4
    SubarcticWinter=5
    USStandard1962=6
    
    @classmethod
    def PredefinedType(cls, type):
      """Use a predefined atmosphere type, one of the constants defined in this class"""
      return "%d" % type
    
    @classmethod
    def UserWaterAndOzone(cls, water, ozone):
      """Use an atmosphere defined by an amount of water vapour (in g/cm^2) and ozone (in cm-atm)"""
      return "8 (Water Vapour and Ozone)\n%f %f" % (water, ozone)
    
    @classmethod
    def RadiosondeProfile(cls, data):
      """Use an atmosphere defined by a profile from a radiosonde measurement. The data argument must be a dictionary with the
      following keys, each of which must be an iterable containing the data:
      altitude
      pressure
      temperature
      water
      ozone
      
      There must be 34 items in each iterable"""
      
      # Check to make sure all iterables have 34 items
      all_lists = [data['altitude'], data['pressure'], data['temperature'], data['water'], data['ozone']]
      if not all(len(x) == 34 for x in all_lists):
        raise ParameterError("radiosonde levels", "There must be 34 values in the lists for each radiosonde attribute (altitude, pressure, temperature, water, ozone)")
      
      result = ""
        
      for i in range(34):
        result = result + "%f %f %f %f %f\n" % (data['altitude'][i], data['pressure'][i], data['temperature'][i], data['water'][i], data['ozone'][i])
      
      return result