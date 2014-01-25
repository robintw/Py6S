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

import unittest
from Py6S import *
import numpy as np

class Example6STests(unittest.TestCase):

	def test_6s_example1(self):
		s = SixS()
		s.geometry = Geometry.User()
		s.geometry.solar_z = 40
		s.geometry.solar_a = 100
		s.geometry.view_z = 45
		s.geometry.view_a = 50
		s.geometry.month = 7
		s.geometry.day = 23

		s.atmos_profile = AtmosProfile.UserWaterAndOzone(3.0, 3.5)
		s.aero_profile = AeroProfile.User(dust=0.25, water=0.25, oceanic=0.25, soot=0.25)


		s.aot550 = 0.5
		s.altitudes.set_target_custom_altitude(0.2)
		s.altitudes.set_sensor_custom_altitude(3.3, aot=0.25)
		s.wavelength = Wavelength(PredefinedWavelengths.AVHRR_NOAA9_B1)

		s.ground_reflectance = GroundReflectance.HeterogeneousLambertian(0.5, GroundReflectance.ClearWater, GroundReflectance.GreenVegetation)

		s.atmos_corr = AtmosCorr.AtmosCorrBRDFFromReflectance(0.1)
		s.run()
		self.assertAlmostEqual(s.outputs.apparent_radiance, 12.749, delta=0.002)

