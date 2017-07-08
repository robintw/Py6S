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

    def test_from_lat_and_date(self):
        ap = AtmosProfile.FromLatitudeAndDate(53, '2015-07-14')

        assert ap == AtmosProfile.PredefinedType(AtmosProfile.SubarcticSummer)


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

    def test_aero_profile_errors(self):
      with self.assertRaises(ParameterError):
        ap = AeroProfile.User(dust=0.8, oceanic=0.4)

    def test_sun_photo_dist_errors1(self):
      with self.assertRaises(ParameterError):
        # Different numbers of elements for first two arguments
        ap = AeroProfile.SunPhotometerDistribution([0.050000001, 0.065604001, 0.086076997,
      0.112939   , 0.148184001, 0.194428995, 0.255104989, 0.334715992, 0.439173013, 0.576227009,
      0.756052017, 0.99199599 , 1.30157101 , 1.707757   , 2.24070191 , 2.93996596 , 3.85745192 ,
      5.06126022 , 6.64074516 , 8.71314526],
      [0.001338098,0.007492487,0.026454749, 0.058904506,0.082712278,0.073251031,0.040950641,
      0.014576218,0.003672085,0.001576356,0.002422644,0.004472982,0.007452302,0.011037065,
      0.014523974,0.016981738,0.017641816,0.016284294,0.01335547,0.009732267,0.006301342,
      0.003625077,],
      [1.47]*20,
      [0.0093]*20)

    def test_sun_photo_dist_errors2(self):
      with self.assertRaises(ParameterError):
        # Different numbers of elements for first two arguments
        ap = AeroProfile.SunPhotometerDistribution([0.050000001, 0.065604001, 0.086076997,
      0.112939   , 0.148184001, 0.194428995, 0.255104989, 0.334715992, 0.439173013, 0.576227009,
      0.756052017, 0.99199599 , 1.30157101 , 1.707757   , 2.24070191 , 2.93996596 , 3.85745192 ,
      5.06126022 , 6.64074516 , 8.71314526 , 11.4322901 , 15],
      [0.001338098,0.007492487,0.026454749, 0.058904506,0.082712278,0.073251031,0.040950641,
      0.014576218,0.003672085,0.001576356,0.002422644,0.004472982,0.007452302,0.011037065,
      0.014523974,0.016981738,0.017641816,0.016284294,0.01335547,0.009732267,0.006301342,
      0.003625077,],
      [1.47]*15,
      [0.0093]*20)

    def test_sun_photo_dist_errors3(self):
      # Different numbers of elements for first two arguments
      ap1 = AeroProfile.SunPhotometerDistribution([0.050000001, 0.065604001, 0.086076997,
      0.112939   , 0.148184001, 0.194428995, 0.255104989, 0.334715992, 0.439173013, 0.576227009,
      0.756052017, 0.99199599 , 1.30157101 , 1.707757   , 2.24070191 , 2.93996596 , 3.85745192 ,
      5.06126022 , 6.64074516 , 8.71314526 , 11.4322901 , 15],
      [0.001338098,0.007492487,0.026454749, 0.058904506,0.082712278,0.073251031,0.040950641,
      0.014576218,0.003672085,0.001576356,0.002422644,0.004472982,0.007452302,0.011037065,
      0.014523974,0.016981738,0.017641816,0.016284294,0.01335547,0.009732267,0.006301342,
      0.003625077,],
      [1.47]*20,
      [2.3]*20)

      ap2 = AeroProfile.SunPhotometerDistribution([0.050000001, 0.065604001, 0.086076997,
      0.112939   , 0.148184001, 0.194428995, 0.255104989, 0.334715992, 0.439173013, 0.576227009,
      0.756052017, 0.99199599 , 1.30157101 , 1.707757   , 2.24070191 , 2.93996596 , 3.85745192 ,
      5.06126022 , 6.64074516 , 8.71314526 , 11.4322901 , 15],
      [0.001338098,0.007492487,0.026454749, 0.058904506,0.082712278,0.073251031,0.040950641,
      0.014576218,0.003672085,0.001576356,0.002422644,0.004472982,0.007452302,0.011037065,
      0.014523974,0.016981738,0.017641816,0.016284294,0.01335547,0.009732267,0.006301342,
      0.003625077,],
      1.47,
      2.3)

      self.assertEqual(ap1, ap2)

    def test_multimodal_dist_errors1(self):
      with self.assertRaises(ParameterError):
        ap = AeroProfile.MultimodalLogNormalDistribution(0.001, 20)
        # Add > 4 components
        ap.add_component(0.05, 2.03, 0.538, [1.508,1.500,1.500,1.500,1.500,
          1.500,1.500,1.500,1.495,1.490,1.490,1.490,1.486,1.480,1.470,1.460,1.456,
          1.443,1.430,1.470], [3.24E-07,3.0E-08,2.86E-08,2.51E-08,2.2E-08,2.0E-08,
          1.0E-08,1.0E-08,1.48E-08,2.0E-08,6.85E-08,1.0E-07,1.25E-06,3.0E-06,3.5E-04,
          6.0E-04,6.86E-04,1.7E-03,4.0E-03,1.4E-03])
        ap.add_component(0.0695, 2.03, 0.457, [1.452,1.440,1.438,1.433,
          1.432,1.431,1.431,1.430,1.429,1.429,1.429,1.428,1.427,1.425,1.411,1.401,
          1.395,1.385,1.364,1.396], [1.0E-08,1.0E-08,1.0E-08,1.0E-08,1.0E-08,1.0E-08,
          1.0E-08,1.0E-08,1.38E-08,1.47E-08,1.68E-08,1.93E-08,4.91E-08,1.75E-07,9.66E-06,
          1.94E-04,3.84E-04,1.12E-03,2.51E-03,1.31E-01])
        ap.add_component(0.4, 2.03, 0.005, [1.508,1.500,1.500,1.500,1.500,
          1.500,1.500,1.500,1.495,1.490,1.490,1.490,1.486,1.480,1.470,1.460,1.456,
          1.443,1.430,1.470], [3.24E-07,3.0E-08,2.86E-08,2.51E-08,2.2E-08,2.0E-08,1.0E-08,
          1.0E-08,1.48E-08,2.0E-08,6.85E-08,1.0E-07,1.25E-06,3.0E-06,3.5E-04,6.0E-04,6.86E-04,
          1.7E-03,4.0E-03,1.4E-03])
        ap.add_component(0.4, 2.03, 0.005, [1.508,1.500,1.500,1.500,1.500,
          1.500,1.500,1.500,1.495,1.490,1.490,1.490,1.486,1.480,1.470,1.460,1.456,
          1.443,1.430,1.470], [3.24E-07,3.0E-08,2.86E-08,2.51E-08,2.2E-08,2.0E-08,1.0E-08,
          1.0E-08,1.48E-08,2.0E-08,6.85E-08,1.0E-07,1.25E-06,3.0E-06,3.5E-04,6.0E-04,6.86E-04,
          1.7E-03,4.0E-03,1.4E-03])
        ap.add_component(0.4, 2.03, 0.005, [1.508,1.500,1.500,1.500,1.500,
          1.500,1.500,1.500,1.495,1.490,1.490,1.490,1.486,1.480,1.470,1.460,1.456,
          1.443,1.430,1.470], [3.24E-07,3.0E-08,2.86E-08,2.51E-08,2.2E-08,2.0E-08,1.0E-08,
          1.0E-08,1.48E-08,2.0E-08,6.85E-08,1.0E-07,1.25E-06,3.0E-06,3.5E-04,6.0E-04,6.86E-04,
          1.7E-03,4.0E-03,1.4E-03])

    def test_multimodal_dist_errors2(self):
      with self.assertRaises(ParameterError):
        ap = AeroProfile.MultimodalLogNormalDistribution(0.001, 20)
        ap.add_component(0.05, 2.03, 0.538, [1.508,1.500,1.500,1.500,1.500,
          1.500,1.500,1.500,1.495,1.490,1.490,1.490,1.486,1.480,1.470,1.460,1.456,
          1.443,1.430,1.470], [3.24E-07,3.0E-08,2.86E-08,2.51E-08,2.2E-08,2.0E-08,
          1.0E-08,1.0E-08,1.48E-08,2.0E-08,6.85E-08,1.0E-07,1.25E-06,3.0E-06,3.5E-04,
          6.0E-04,6.86E-04])

    def test_multimodal_dist_errors3(self):
      with self.assertRaises(ParameterError):
        ap = AeroProfile.MultimodalLogNormalDistribution(0.001, 20)
        ap.add_component(0.4, 2.03, 0.005, [1.508,1.500,1.500,1.500,1.500,
          1.500,1.500,1.500,1.495,1.490,1.490,1.490,1.486,1.480,1.470,1.460,1.456,
          1.443,1.430,1.470, 1.999, 1.999, 0], [3.24E-07,3.0E-08,2.86E-08,2.51E-08,2.2E-08,2.0E-08,1.0E-08,
          1.0E-08,1.48E-08,2.0E-08,6.85E-08,1.0E-07,1.25E-06,3.0E-06,3.5E-04,6.0E-04,6.86E-04,
          1.7E-03,4.0E-03,1.4E-03])
