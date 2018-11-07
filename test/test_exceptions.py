# This file is part of Py6S.
#
# Copyright 2018 Robin Wilson and contributors listed in the CONTRIBUTORS file.
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

import unittest
from Py6S import *


class ExceptionTests(unittest.TestCase):

  def test_short_output(self):
    with self.assertRaises(OutputParsingError):
        s = SixS()
        s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeSummer)
        s.aero_profile = AeroProfile.PredefinedType(AeroProfile.Continental)
        s.visibility = 23
        altitudes = Altitudes()
        altitudes.set_sensor_satellite_level()
        altitudes.set_target_custom_altitude(-0.05)
        s.altitudes = altitudes
        s.atmos_corr = AtmosCorr.AtmosCorrLambertianFromReflectance(-0.2)
        s.wavelength = Wavelength(PredefinedWavelengths.LANDSAT_TM_B2)
        s.ground_reflectance = GroundReflectance.HomogeneousLambertian(0.3)

        s.geometry = Geometry.Landsat_TM()
        s.geometry.month = 4
        s.geometry.day = 25
        s.geometry.gmt_decimal_hour = 2
        s.geometry.latitude = 39.967
        s.geometry.longtitude = 116.35

        s.run()