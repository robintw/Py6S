"""Contains a number of classes for easily setting parameters of the 6S model"""

from aeroprofile import AeroProfile
from atmoscorr import AtmosCorr
from atmosprofile import AtmosProfile
from ground_reflectance import GroundReflectance
from wavelength import Wavelength
from geometry import *

__all__ = ["AtmosProfile", "AeroProfile", "AtmosCorr", "GroundReflectance", "Wavelength", "GeometryUser", "GeometryMeteosat", "GeometryGoesEast", "GeometryGoesWest", "GeometryAVHRR_PM", "GeometryAVHRR_AM", "GeometrySPOT_HRV", "GeometryLandsat_TM"]