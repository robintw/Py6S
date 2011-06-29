"""Contains a number of classes for easily setting parameters of the 6S model"""

from aeromodel import AeroModel
from atmoscorr import AtmosCorr
from atmosmodel import AtmosModel
from ground_reflectance import GroundReflectance
from wavelength import WavelengthType

__all__ = ["aeromodel", "atmosmodel", "atmoscorr", "AtmosModel", "AeroModel", "AtmosCorr", "GroundReflectance", "WavelengthType"]