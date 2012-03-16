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
      """Set 6S to use a predefined atmosphere type.
      
      Arguments:
      
      * ``type`` -- the predefined atmosphere type, one of the constants defined in this class
      
      Example usage::
      
        s.atmosprofile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeSummer)
      
      """
      return "%d" % type
    
    @classmethod
    def UserWaterAndOzone(cls, water, ozone):
      """Set 6S to use an atmosphere defined by an amount of water vapour and ozone.
      
      Arguments:
      
      * ``water`` -- The total amount of water in a vertical path through the atmosphere (in g/cm^2)
      * ``ozone`` -- The total amount of ozone in a vertical path through the atmosphere (in cm-atm)
      
      Example usage::
      
        s.atmosprofile = AtmosProfile.UserWaterAndOzone(3.6, 0.9)
      
      """
      return "8 (Water Vapour and Ozone)\n%f %f" % (water, ozone)
    
    @classmethod
    def RadiosondeProfile(cls, data):
      """Set 6S to use an atmosphere defined by a profile from a radiosonde measurements.
      
      Arguments:
      
      * ``data`` -- A dictionary containing five iterables (eg. lists) with the radiosonde measurements in them. The dictionary must have the following keys:
          * ``altitude`` -- in km
          * ``pressure`` -- in mb
          * ``temperature`` -- in k
          * ``water`` -- in g/m^3
          * ``ozone`` -- in g/m^3

      There must be 34 items in each iterable, or a :class:`ParameterExeception` will be thrown.
      
      """
      
      # Check to make sure all iterables have 34 items
      all_lists = [data['altitude'], data['pressure'], data['temperature'], data['water'], data['ozone']]
      if not all(len(x) == 34 for x in all_lists):
        raise ParameterError("radiosonde levels", "There must be 34 values in the lists for each radiosonde attribute (altitude, pressure, temperature, water, ozone)")
      
      result = ""
        
      for i in range(34):
        result = result + "%f %f %f %f %f\n" % (data['altitude'][i], data['pressure'][i], data['temperature'][i], data['water'][i], data['ozone'][i])
      
      return "7 User's data base profile\n" + result