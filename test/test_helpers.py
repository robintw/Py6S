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

class ParallelEquivalenceTests(unittest.TestCase):
	def test_wavelengths_equiv(self):
		s = SixS()
		s.altitudes.set_sensor_satellite_level()
		s.altitudes.set_target_sea_level()

		serial_res = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.05, output_name='apparent_radiance', n=1)
		
		for i in range(2, 10, 2):
			parallel_res = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.05, output_name='apparent_radiance', n=i)
			np.testing.assert_allclose(parallel_res, serial_res)

	def test_angles_equiv(self):
		s = SixS()

		serial_res = SixSHelpers.Angles.run360(s, 'view', output_name='apparent_radiance', n=1)
		
		for i in range(2, 10, 2):
			parallel_res = SixSHelpers.Angles.run360(s, 'view', output_name='apparent_radiance', n=i)
			np.testing.assert_allclose(parallel_res, serial_res)

class AllWavelengthsTests(unittest.TestCase):
	def test_run_for_all_wvs(self):
	  s = SixS()
	  results = SixSHelpers.Wavelengths.run_landsat_etm(s, output_name="apparent_radiance")
	  
	  a = np.array([ 138.392,  129.426,  111.635,   75.822,   16.684,    5.532])
	  
	  self.assertAlmostEqual(results[0], [0.47750000000000004, 0.56125000000000003, 0.65874999999999995, 0.82624999999999993, 1.6487500000000002, 2.19625], delta=0.002)
	  self.assertAlmostEqual(all(a == results[1]), True, delta=0.002)


class AllAnglesTests(unittest.TestCase):
	def test_run360(self):
		s = SixS()

		res0 = np.array([ 163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685,
		        163.599,  160.769,  152.359,  138.612,  119.949,   97.014,
		         70.809,   43.092,   17.56 ,    0.685,  163.599,  160.769,
		        152.359,  138.612,  119.949,   97.014,   70.809,   43.092,
		         17.56 ,    0.685,  163.599,  160.769,  152.359,  138.612,
		        119.949,   97.014,   70.809,   43.092,   17.56 ,    0.685])

		results = SixSHelpers.Angles.run360(s, 'solar', output_name='apparent_radiance')

		np.testing.assert_allclose(results[0], res0)
