"""Contains a number of classes for easily setting parameters of the 6S model"""

from aeroprofile import AeroProfile
from atmoscorr import AtmosCorr
from atmosprofile import AtmosProfile
from ground_reflectance import GroundReflectance
from wavelength import Wavelength
from wavelength import PredefinedWavelengths
from altitudes import Altitudes
from geometry import *

__all__ = ["AtmosProfile", "AeroProfile", "AtmosCorr", "GroundReflectance", "Wavelength", "Geometry", "Altitudes", "PredefinedWavelengths"]