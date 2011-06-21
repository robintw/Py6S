class AtmosModel:
    """Stores a enumeration for the pre-specified atmospheric model types"""
    NO_GASEOUS_ABSORPTION=0 
    TROPICAL=1
    MIDLATITUDE_SUMMER=2
    MIDLATITUDE_WINTER=3
    SUBARCTIC_SUMMER=4
    SUBARCTIC_WINTER=5
    US_STANDARD_1962=6
    
class AeroModel:
    """Stores an enumeration for the pre-specified aerosol model types"""
    NO_AEROSOL=0
    CONTINENTAL=1
    MARITIME=2
    URBAN=3
    USER=4
    DESERT=5
    BIOMASS_BURNING=6
    STRATOSPHERIC=7