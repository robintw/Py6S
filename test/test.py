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
    
    self.assertEqual(s.outputs.visibility, 8.49)
    self.assertEqual(s.outputs.aot550, 0.5)
    
  def test_vis_aot_small(self):
    s = SixS()
    s.aot550 = 0.001
    s.run()
    
    self.assertEqual(s.outputs.visibility, float("Inf"))
    self.assertEqual(s.outputs.aot550, 0.001)   

class WavelengthTests(unittest.TestCase):

  def test_specific_wavelength(self):
    s = SixS()
    s.wavelength = Wavelength(0.567)
    s.run()
    
    self.assertEqual(s.outputs.apparent_radiance, 129.792)
  
  def test_wavelength_range(self):
    s = SixS()
    s.wavelength = Wavelength(0.5, 0.7)
    s.run()
    
    self.assertEqual(s.outputs.apparent_radiance, 122.166)
   
  def test_wavelength_filter(self):
    s = SixS()
    s.wavelength = Wavelength(0.400, 0.410, [0.7, 0.9, 1.0, 0.3, 1.0])
    s.run()
    
    self.assertEqual(s.outputs.apparent_radiance, 109.435)
    
  def test_wavelength_predefined(self):
    s = SixS()
    s.wavelength = Wavelength(PredefinedWavelengths.LANDSAT_TM_B1)
    s.run()
    
    self.assertEqual(s.outputs.apparent_radiance, 138.126)
    
    s.wavelength = Wavelength(PredefinedWavelengths.MODIS_B6)
    s.run()
    
    self.assertEqual(s.outputs.apparent_radiance, 17.917)
    
  def test_run_for_all_wvs(self):
    s = SixS()
    results = SixSHelpers.Wavelengths.run_landsat_etm(s, "apparent_radiance")
    
    a = np.array([ 138.392,  129.426,  111.635,   75.822,   16.684,    5.532])
    
    self.assertEqual(results[0], [0.47750000000000004, 0.56125000000000003, 0.65874999999999995, 0.82624999999999993, 1.6487500000000002, 2.19625])
    self.assertEqual(all(a == results[1]), True)

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

            self.assertEqual(s.outputs.apparent_reflectance, results[i], "Error in atmos profile with ID %s. Got %f, expected %f." % (str(aps[i]), s.outputs.apparent_reflectance, results[i]))


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

            self.assertEqual(s.outputs.apparent_radiance, results[i], "Error in aerosol profile with ID %s. Got %f, expected %f." % (str(aps[i]), s.outputs.apparent_radiance, results[i]))

class AtmosCorrTests(unittest.TestCase):

  def test_atmos_corr_radiance(self):
    s = SixS()
    s.atmos_corr = AtmosCorr.AtmosCorrLambertianFromRadiance(130.1)
    s.run()

    self.assertEqual(s.outputs.atmos_corrected_reflectance_lambertian, 0.29048)