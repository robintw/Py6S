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
import os.path

test_dir = os.path.relpath(os.path.dirname(__file__))

class AllWavelengthsTests(unittest.TestCase):
	def test_run_for_landsat_etm(self):
		s = SixS()
		results = SixSHelpers.Wavelengths.run_landsat_etm(s, output_name="apparent_radiance")

		a = np.array([ 138.392,  129.426,  111.635,   75.822,   16.684,    5.532])

		self.assertAlmostEqual(results[0], [0.47750000000000004, 0.56125000000000003, 0.65874999999999995, 0.82624999999999993, 1.6487500000000002, 2.19625], delta=0.002)
		np.testing.assert_allclose(a, results[1], atol=0.1)

	# def test_run_vnir(self):
	# 	s = SixS()

	# 	res1 = np.array([  1.06277000e+02,   1.13830000e+02,   1.15817000e+02,
 #         1.02365000e+02,   1.23245000e+02,   1.42776000e+02,
 #         1.42479000e+02,   1.39744000e+02,   1.45150000e+02,
 #         1.37120000e+02,   1.34632000e+02,   1.37690000e+02,
 #         1.28269000e+02,   1.35603000e+02,   1.31461000e+02,
 #         1.32691000e+02,   1.29116000e+02,   1.26856000e+02,
 #         1.29650000e+02,   1.12563000e+02,   1.24528000e+02,
 #         1.23302000e+02,   1.22705000e+02,   1.17426000e+02,
 #         1.18582000e+02,   1.14522000e+02,   1.12756000e+02,
 #         1.13049000e+02,   1.10981000e+02,   9.94830000e+01,
 #         9.78730000e+01,   1.01459000e+02,   6.77290000e+01,
 #         8.57130000e+01,   9.16280000e+01,   9.55010000e+01,
 #         3.29370000e+01,   9.00900000e+01,   8.99580000e+01,
 #         8.42230000e+01,   8.32780000e+01,   8.23420000e+01,
 #         6.48640000e+01,   7.33550000e+01,   7.63210000e+01,
 #         7.46040000e+01,   7.61020000e+01,   7.33860000e+01,
 #         7.46110000e+01,   7.18570000e+01,   4.98630000e+01,
 #         5.16160000e+01,   6.61430000e+01,   2.99600000e+01,
 #         3.37400000e+01,   9.32600000e+00,   3.12920000e+01,
 #         4.79930000e+01,   4.72160000e+01,   5.76070000e+01,
 #         5.73750000e+01,   5.51640000e+01,   5.46180000e+01,
 #         5.38880000e+01,   5.26510000e+01,   5.13970000e+01,
 #         5.01510000e+01,   4.86360000e+01,   4.55230000e+01,
 #         4.28240000e+01,   4.22910000e+01,   2.89800000e+01,
 #         1.10700000e+01,   2.27380000e+01,   2.28250000e+01,
 #         1.17830000e+01,   2.22660000e+01,   3.40500000e+01,
 #         3.30080000e+01,   3.35820000e+01,   3.24610000e+01,
 #         3.44070000e+01,   3.59620000e+01,   3.58170000e+01,
 #         3.49320000e+01,   3.41050000e+01,   3.23240000e+01,
 #         2.98160000e+01,   3.03150000e+01,   2.84890000e+01,
 #         2.67730000e+01,   2.17160000e+01,   1.84090000e+01,
 #         1.21580000e+01,   1.38780000e+01,   1.05100000e+00,
 #         5.80000000e-02,   1.80000000e-02,   1.30000000e-02,
 #         9.01000000e-01])


	# 	results = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.01, output_name='apparent_radiance')
	# 	np.testing.assert_allclose(results[1], res1, atol=0.1)

class ParallelEquivalenceTests(unittest.TestCase):
	def test_wavelengths_equiv(self):
		s = SixS()
		s.altitudes.set_sensor_satellite_level()
		s.altitudes.set_target_sea_level()

		serial_res = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.05, output_name='apparent_radiance', n=1)
		
		for i in range(2, 10, 2):
			parallel_res = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.05, output_name='apparent_radiance', n=i)
			np.testing.assert_allclose(parallel_res, serial_res)

	def test_after_prev_run(self):
		s = SixS()
		s.run()

		try:
			results = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.05, output_name='apparent_radiance', n=1)
		except OutputParsingError:
			self.fail("OutputParsingError raised by run_vnir after previous SixS.run")

	def test_angles_equiv(self):
		s = SixS()

		serial_res = SixSHelpers.Angles.run360(s, 'view', output_name='apparent_radiance', n=1)
		
		for i in range(2, 10, 2):
			parallel_res = SixSHelpers.Angles.run360(s, 'view', output_name='apparent_radiance', n=i)
			np.testing.assert_allclose(parallel_res[0], serial_res[0])

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


class AERONETImportTest(unittest.TestCase):

  def test_import_aeronet(self):
    s = SixS()
    s = SixSHelpers.Aeronet.import_aeronet_data(s, os.path.join(test_dir, "070101_101231_Marambio.dubovik"), "2008-02-22")
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 137.324, delta=0.002)

  def test_import_empty_file(self):
    s = SixS()
    with self.assertRaises(ParameterError):
      SixSHelpers.Aeronet.import_aeronet_data(s, os.path.join(test_dir, "empty_file"), "2008-02-22")

class RadiosondeImportTest(unittest.TestCase):

	def test_simple_radiosonde_import(self):
		s = SixS()
		s.altitudes.set_sensor_satellite_level()
		s.altitudes.set_target_sea_level()
		s.atmos_profile = SixSHelpers.Radiosonde.import_uow_radiosonde_data("http://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR=2012&MONTH=02&FROM=2712&TO=2712&STNM=03808", AtmosProfile.MidlatitudeWinter)
		s.run()

		self.assertAlmostEqual(s.outputs.apparent_radiance, 164.482, delta=0.02)
