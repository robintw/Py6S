# This file is part of Py6S.
#
# Copyright 2012 Robin Wilson and contributors listed in the CONTRIBUTORS file.
#
# Py6S is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Py6S is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Py6S.  If not, see <http://www.gnu.org/licenses/>.

"""Contains a number of classes for easily setting parameters of the 6S model"""

from .aeroprofile import AeroProfile
from .atmoscorr import AtmosCorr
from .atmosprofile import AtmosProfile
from .ground_reflectance import GroundReflectance
from .wavelength import Wavelength
from .wavelength import PredefinedWavelengths
from .altitudes import Altitudes
from .geometry import *

__all__ = ["AtmosProfile", "AeroProfile", "AtmosCorr", "GroundReflectance", "Wavelength", "Geometry", "Altitudes", "PredefinedWavelengths"]
