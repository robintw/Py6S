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
      
    def UserWaterAndOzone(cls, water, ozone):
      """Use an atmosphere defined by an amount of water vapour (in g/cm^2) and ozone (in cm-atm)"""
      return "8 (Water Vapour and Ozone)\n%f %f" % (water, ozone)
      