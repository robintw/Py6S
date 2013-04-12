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

class SimpleTests(unittest.TestCase):

  def test_inbuilt_test(self):
    result = SixS.test()
    self.assertEqual(result, 0)
    
class VisAOTTests(unittest.TestCase):

  def test_vis_aot_normal(self):
    s = SixS()
    s.run()
    
    self.assertAlmostEqual(s.outputs.visibility, 8.49, delta=0.002)
    self.assertAlmostEqual(s.outputs.aot550, 0.5, delta=0.002)
    
  def test_vis_aot_small(self):
    s = SixS()
    s.aot550 = 0.001
    s.run()
    
    self.assertAlmostEqual(s.outputs.visibility, float("Inf"))
    self.assertAlmostEqual(s.outputs.aot550, 0.001, delta=0.002)   

class WavelengthTests(unittest.TestCase):

  def test_specific_wavelength(self):
    s = SixS()
    s.wavelength = Wavelength(0.567)
    s.run()
    
    self.assertAlmostEqual(s.outputs.apparent_radiance, 129.792, delta=0.002)
  
  def test_wavelength_range(self):
    s = SixS()
    s.wavelength = Wavelength(0.5, 0.7)
    s.run()
    
    self.assertAlmostEqual(s.outputs.apparent_radiance, 122.166, delta=0.002)
   
  def test_wavelength_filter(self):
    s = SixS()
    s.wavelength = Wavelength(0.400, 0.410, [0.7, 0.9, 1.0, 0.3, 1.0])
    s.run()
    
    self.assertAlmostEqual(s.outputs.apparent_radiance, 109.435, delta=0.002)
    
  def test_wavelength_predefined(self):
    s = SixS()
    s.wavelength = Wavelength(PredefinedWavelengths.LANDSAT_TM_B1)
    s.run()
    
    self.assertAlmostEqual(s.outputs.apparent_radiance, 138.126, delta=0.002)
    
    s.wavelength = Wavelength(PredefinedWavelengths.MODIS_B6)
    s.run()
    
    self.assertAlmostEqual(s.outputs.apparent_radiance, 17.917, delta=0.002)
    

  def test_invalid_wavelengths(self):
    with self.assertRaises(ParameterError):
      Wavelength(1000)

    with self.assertRaises(ParameterError):
      Wavelength(0.15)

    with self.assertRaises(ParameterError):
      Wavelength(0.5, 50)

  def test_run_for_all_wvs(self):
    s = SixS()
    results = SixSHelpers.Wavelengths.run_landsat_etm(s, "apparent_radiance")
    
    a = np.array([ 138.392,  129.426,  111.635,   75.822,   16.684,    5.532])
    
    self.assertAlmostEqual(results[0], [0.47750000000000004, 0.56125000000000003, 0.65874999999999995, 0.82624999999999993, 1.6487500000000002, 2.19625], delta=0.002)
    self.assertAlmostEqual(all(a == results[1]), True, delta=0.002)

class AtmosProfileTests(unittest.TestCase):

    def test_atmos_profile(self):

        aps = [AtmosProfile.Tropical,
               AtmosProfile.NoGaseousAbsorption,
               AtmosProfile.UserWaterAndOzone(0.9, 3)]
        results = [0.2723143,
                   0.2747224,
                   0.2476101]

        for i in range(len(aps)):
            s = SixS()
            s.atmos_profile = aps[i]
            s.run()

            self.assertAlmostEqual(s.outputs.apparent_reflectance, results[i], msg="Error in atmos profile with ID %s. Got %f, expected %f." % (str(aps[i]), s.outputs.apparent_reflectance, results[i]), delta=0.002)


class AeroProfileTests(unittest.TestCase):

    def test_aero_profile(self):
        user_ap = AeroProfile.UserProfile(AeroProfile.Maritime)
        user_ap.add_layer(5, 0.34)

        aps = [AeroProfile.Continental,
               AeroProfile.NoAerosols,
               AeroProfile.User(dust=0.3, oceanic=0.7),
               user_ap]
        results = [122.854,
                   140.289,
                   130.866,
                   136.649]

        for i in range(len(aps)):
            s = SixS()
            s.aero_profile = aps[i]
            s.run()

            self.assertAlmostEqual(s.outputs.apparent_radiance, results[i], "Error in aerosol profile with ID %s. Got %f, expected %f." % (str(aps[i]), s.outputs.apparent_radiance, results[i]), delta=0.002)

class AtmosCorrTests(unittest.TestCase):

  def test_atmos_corr_radiance(self):
    s = SixS()
    s.atmos_corr = AtmosCorr.AtmosCorrLambertianFromRadiance(130.1)
    s.run()

    self.assertAlmostEqual(s.outputs.atmos_corrected_reflectance_lambertian, 0.29048, delta=0.002)

class UserDefinedSpectraTest(unittest.TestCase):

  def test_aster_spectra(self):
    s = SixS()
    s.ground_reflectance = GroundReflectance.HomogeneousLambertian(Spectra.import_from_aster("http://speclib.jpl.nasa.gov/speclibdata/jhu.becknic.water.ice.none.solid.ice.spectrum.txt"))
    s.run()
    
    self.assertAlmostEqual(s.outputs.apparent_radiance, 7.753, delta=0.002)


  def test_usgs_spectra(self):
    s = SixS()
    s.ground_reflectance = GroundReflectance.HomogeneousLambertian(Spectra.import_from_usgs("http://speclab.cr.usgs.gov/spectral.lib06/ds231/ASCII/V/cheatgrass_anp92-11a_veg.29744.asc"))
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 29.316, delta=0.002)


  def test_usgs_spectra_from_file(self):
    s = SixS()
    s.ground_reflectance = GroundReflectance.HomogeneousLambertian(Spectra.import_from_usgs("./test/butlerite_gds25.3947.asc"))
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 180.818, delta=0.002)



class AltitudesTest(unittest.TestCase):

  def test_custom_sensor_altitude(self):
    s = SixS()
    s.altitudes.set_sensor_custom_altitude(3, 0.26)
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 147.964, delta=0.002)

  def test_custom_target_altitude(self):
    s = SixS()
    s.altitudes.set_target_custom_altitude(7)
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 139.192, delta=0.002)

  def test_custom_altitudes(self):
    s = SixS()
    s.altitudes.set_target_custom_altitude(7)
    s.altitudes.set_sensor_custom_altitude(50, 0.26)
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 158.101, delta=0.002)

  def test_satellite_level(self):
    s = SixS()
    s.altitudes.set_sensor_satellite_level()
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 165.188, delta=0.002)

  def test_changing_levels(self):
    s = SixS()
    s.altitudes.set_sensor_custom_altitude(1)
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 142.053, delta=0.002)

    s.altitudes.set_sensor_satellite_level()
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 165.188, delta=0.002)

  def test_target_pressure(self):
    s = SixS()
    s.altitudes.set_sensor_satellite_level()
    s.altitudes.set_target_pressure(200)
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 165.188, delta=0.002)

class AERONETImportTest(unittest.TestCase):

  def test_import_aeronet(self):
    s = SixS()
    s = SixSHelpers.Aeronet.import_aeronet_data(s, "./test/070101_101231_Marambio.dubovik", "2008-02-22")
    s.run()

    self.assertAlmostEqual(s.outputs.apparent_radiance, 137.324, delta=0.002)

  def test_import_empty_file(self):
    s = SixS()
    with self.assertRaises(ParameterError):
      SixSHelpers.Aeronet.import_aeronet_data(s, "./test/empty_file", "2008-02-22")

