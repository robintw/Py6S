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

from Py6S import *
import sys
import numpy as np
import urllib
import re
from scipy.interpolate import interp1d
import io

if sys.version_info[0] >= 3:
    import urllib.request as urllib
else:
    import urllib

class Radiosonde:

    sixs_altitudes = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8.,
                               9., 10., 11., 12., 13., 14., 15., 16., 17.,
                               18., 19., 20., 21., 22., 23., 24., 25., 30.,
                               35., 40., 45., 50., 70., 100., 99999.])

    # Temperature profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    temp_profiles = np.array([[3.000e+02, 2.940e+02, 2.880e+02, 2.840e+02, 2.770e+02, 2.700e+02,
                               2.640e+02, 2.570e+02, 2.500e+02, 2.440e+02, 2.370e+02, 2.300e+02,
                               2.240e+02, 2.170e+02, 2.100e+02, 2.040e+02, 1.970e+02, 1.950e+02,
                               1.990e+02, 2.030e+02, 2.070e+02, 2.110e+02, 2.150e+02, 2.170e+02,
                               2.190e+02, 2.210e+02, 2.320e+02, 2.430e+02, 2.540e+02, 2.650e+02,
                               2.700e+02, 2.190e+02, 2.100e+02, 2.100e+02],

                              [2.940e+02, 2.900e+02, 2.850e+02, 2.790e+02, 2.730e+02, 2.670e+02,
                               2.610e+02, 2.550e+02, 2.480e+02, 2.420e+02, 2.350e+02, 2.290e+02,
                               2.220e+02, 2.160e+02, 2.160e+02, 2.160e+02, 2.160e+02, 2.160e+02,
                               2.160e+02, 2.170e+02, 2.180e+02, 2.190e+02, 2.200e+02, 2.220e+02,
                               2.230e+02, 2.240e+02, 2.340e+02, 2.450e+02, 2.580e+02, 2.700e+02,
                               2.760e+02, 2.180e+02, 2.100e+02, 2.100e+02],

                              [2.722e+02, 2.687e+02, 2.652e+02, 2.617e+02, 2.557e+02, 2.497e+02,
                               2.437e+02, 2.377e+02, 2.317e+02, 2.257e+02, 2.197e+02, 2.192e+02,
                               2.187e+02, 2.182e+02, 2.177e+02, 2.172e+02, 2.167e+02, 2.162e+02,
                               2.157e+02, 2.152e+02, 2.152e+02, 2.152e+02, 2.152e+02, 2.152e+02,
                               2.152e+02, 2.152e+02, 2.174e+02, 2.278e+02, 2.432e+02, 2.585e+02,
                               2.657e+02, 2.307e+02, 2.102e+02, 2.100e+02],

                              [2.870e+02, 2.820e+02, 2.760e+02, 2.710e+02, 2.660e+02, 2.600e+02,
                               2.530e+02, 2.460e+02, 2.390e+02, 2.320e+02, 2.250e+02, 2.250e+02,
                               2.250e+02, 2.250e+02, 2.250e+02, 2.250e+02, 2.250e+02, 2.250e+02,
                               2.250e+02, 2.250e+02, 2.250e+02, 2.250e+02, 2.250e+02, 2.250e+02,
                               2.260e+02, 2.280e+02, 2.350e+02, 2.470e+02, 2.620e+02, 2.740e+02,
                               2.770e+02, 2.160e+02, 2.100e+02, 2.100e+02],

                              [2.571e+02, 2.591e+02, 2.559e+02, 2.527e+02, 2.477e+02, 2.409e+02,
                               2.341e+02, 2.273e+02, 2.206e+02, 2.172e+02, 2.172e+02, 2.172e+02,
                               2.172e+02, 2.172e+02, 2.172e+02, 2.172e+02, 2.166e+02, 2.160e+02,
                               2.154e+02, 2.148e+02, 2.141e+02, 2.136e+02, 2.130e+02, 2.124e+02,
                               2.118e+02, 2.112e+02, 2.160e+02, 2.222e+02, 2.347e+02, 2.470e+02,
                               2.593e+02, 2.457e+02, 2.100e+02, 2.100e+02],

                              [2.881e+02, 2.816e+02, 2.751e+02, 2.687e+02, 2.622e+02, 2.557e+02,
                               2.492e+02, 2.427e+02, 2.362e+02, 2.297e+02, 2.232e+02, 2.168e+02,
                               2.166e+02, 2.166e+02, 2.166e+02, 2.166e+02, 2.166e+02, 2.166e+02,
                               2.166e+02, 2.166e+02, 2.166e+02, 2.176e+02, 2.186e+02, 2.196e+02,
                               2.206e+02, 2.216e+02, 2.265e+02, 2.365e+02, 2.534e+02, 2.642e+02,
                               2.706e+02, 2.197e+02, 2.100e+02, 2.100e+02]
                              ])

    # Pressure profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    pressure_profiles = np.array([[1.013e+03, 9.040e+02, 8.050e+02, 7.150e+02, 6.330e+02, 5.590e+02,
                                   4.920e+02, 4.320e+02, 3.780e+02, 3.290e+02, 2.860e+02, 2.470e+02,
                                   2.130e+02, 1.820e+02, 1.560e+02, 1.320e+02, 1.110e+02, 9.370e+01,
                                   7.890e+01, 6.660e+01, 5.650e+01, 4.800e+01, 4.090e+01, 3.500e+01,
                                   3.000e+01, 2.570e+01, 1.220e+01, 6.000e+00, 3.050e+00, 1.590e+00,
                                   8.540e-01, 5.790e-02, 3.000e-04, 0.000e+00],

                                  [1.013e+03, 9.020e+02, 8.020e+02, 7.100e+02, 6.280e+02, 5.540e+02,
                                   4.870e+02, 4.260e+02, 3.720e+02, 3.240e+02, 2.810e+02, 2.430e+02,
                                   2.090e+02, 1.790e+02, 1.530e+02, 1.300e+02, 1.110e+02, 9.500e+01,
                                   8.120e+01, 6.950e+01, 5.950e+01, 5.100e+01, 4.370e+01, 3.760e+01,
                                   3.220e+01, 2.770e+01, 1.320e+01, 6.520e+00, 3.330e+00, 1.760e+00,
                                   9.510e-01, 6.710e-02, 3.000e-04, 0.000e+00],

                                  [1.018e+03, 8.973e+02, 7.897e+02, 6.938e+02, 6.081e+02, 5.313e+02,
                                   4.627e+02, 4.016e+02, 3.473e+02, 2.992e+02, 2.568e+02, 2.199e+02,
                                   1.882e+02, 1.610e+02, 1.378e+02, 1.178e+02, 1.007e+02, 8.610e+01,
                                   7.350e+01, 6.280e+01, 5.370e+01, 4.580e+01, 3.910e+01, 3.340e+01,
                                   2.860e+01, 2.430e+01, 1.110e+01, 5.180e+00, 2.530e+00, 1.290e+00,
                                   6.820e-01, 4.670e-02, 3.000e-04, 0.000e+00],

                                  [1.010e+03, 8.960e+02, 7.929e+02, 7.000e+02, 6.160e+02, 5.410e+02,
                                   4.730e+02, 4.130e+02, 3.590e+02, 3.107e+02, 2.677e+02, 2.300e+02,
                                   1.977e+02, 1.700e+02, 1.460e+02, 1.250e+02, 1.080e+02, 9.280e+01,
                                   7.980e+01, 6.860e+01, 5.890e+01, 5.070e+01, 4.360e+01, 3.750e+01,
                                   3.227e+01, 2.780e+01, 1.340e+01, 6.610e+00, 3.400e+00, 1.810e+00,
                                   9.870e-01, 7.070e-02, 3.000e-04, 0.000e+00],

                                  [1.013e+03, 8.878e+02, 7.775e+02, 6.798e+02, 5.932e+02, 5.158e+02,
                                   4.467e+02, 3.853e+02, 3.308e+02, 2.829e+02, 2.418e+02, 2.067e+02,
                                   1.766e+02, 1.510e+02, 1.291e+02, 1.103e+02, 9.431e+01, 8.058e+01,
                                   6.882e+01, 5.875e+01, 5.014e+01, 4.277e+01, 3.647e+01, 3.109e+01,
                                   2.649e+01, 2.256e+01, 1.020e+01, 4.701e+00, 2.243e+00, 1.113e+00,
                                   5.719e-01, 4.016e-02, 3.000e-04, 0.000e+00],

                                  [1.013e+03, 8.986e+02, 7.950e+02, 7.012e+02, 6.166e+02, 5.405e+02,
                                   4.722e+02, 4.111e+02, 3.565e+02, 3.080e+02, 2.650e+02, 2.270e+02,
                                   1.940e+02, 1.658e+02, 1.417e+02, 1.211e+02, 1.035e+02, 8.850e+01,
                                   7.565e+01, 6.467e+01, 5.529e+01, 4.729e+01, 4.047e+01, 3.467e+01,
                                   2.972e+01, 2.549e+01, 1.197e+01, 5.746e+00, 2.871e+00, 1.491e+00,
                                   7.978e-01, 5.520e-02, 3.008e-04, 0.000e+00]
                                  ])

    # Water density profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    water_density_profiles = np.array([[1.900e+01, 1.300e+01, 9.300e+00, 4.700e+00, 2.200e+00, 1.500e+00,
                                        8.500e-01, 4.700e-01, 2.500e-01, 1.200e-01, 5.000e-02, 1.700e-02,
                                        6.000e-03, 1.800e-03, 1.000e-03, 7.600e-04, 6.400e-04, 5.600e-04,
                                        5.000e-04, 4.900e-04, 4.500e-04, 5.100e-04, 5.100e-04, 5.400e-04,
                                        6.000e-04, 6.700e-04, 3.600e-04, 1.100e-04, 4.300e-05, 1.900e-05,
                                        6.300e-06, 1.400e-07, 1.000e-09, 0.000e+00],

                                       [1.400e+01, 9.300e+00, 5.900e+00, 3.300e+00, 1.900e+00, 1.000e+00,
                                        6.100e-01, 3.700e-01, 2.100e-01, 1.200e-01, 6.400e-02, 2.200e-02,
                                        6.000e-03, 1.800e-03, 1.000e-03, 7.600e-04, 6.400e-04, 5.600e-04,
                                        5.000e-04, 4.900e-04, 4.500e-04, 5.100e-04, 5.100e-04, 5.400e-04,
                                        6.000e-04, 6.700e-04, 3.600e-04, 1.100e-04, 4.300e-05, 1.900e-05,
                                        1.300e-06, 1.400e-07, 1.000e-09, 0.000e+00],

                                       [3.500e+00, 2.500e+00, 1.800e+00, 1.200e+00, 6.600e-01, 3.800e-01,
                                        2.100e-01, 8.500e-02, 3.500e-02, 1.600e-02, 7.500e-03, 6.900e-03,
                                        6.000e-03, 1.800e-03, 1.000e-03, 7.600e-04, 6.400e-04, 5.600e-04,
                                        5.000e-04, 4.900e-04, 4.500e-04, 5.100e-04, 5.100e-04, 5.400e-04,
                                        6.000e-04, 6.700e-04, 3.600e-04, 1.100e-04, 4.300e-05, 1.900e-05,
                                        6.300e-06, 1.400e-07, 1.000e-09, 0.000e+00],

                                       [9.100e+00, 6.000e+00, 4.200e+00, 2.700e+00, 1.700e+00, 1.000e+00,
                                        5.400e-01, 2.900e-01, 1.300e-01, 4.200e-02, 1.500e-02, 9.400e-03,
                                        6.000e-03, 1.800e-03, 1.000e-03, 7.600e-04, 6.400e-04, 5.600e-04,
                                        5.000e-04, 4.900e-04, 4.500e-04, 5.100e-04, 5.100e-04, 5.400e-04,
                                        6.000e-04, 6.700e-04, 3.600e-04, 1.100e-04, 4.300e-05, 1.900e-05,
                                        6.300e-06, 1.400e-07, 1.000e-09, 0.000e+00],

                                       [1.200e+00, 1.200e+00, 9.400e-01, 6.800e-01, 4.100e-01, 2.000e-01,
                                        9.800e-02, 5.400e-02, 1.100e-02, 8.400e-03, 5.500e-03, 3.800e-03,
                                        2.600e-03, 1.800e-03, 1.000e-03, 7.600e-04, 6.400e-04, 5.600e-04,
                                        5.000e-04, 4.900e-04, 4.500e-04, 5.100e-04, 5.100e-04, 5.400e-04,
                                        6.000e-04, 6.700e-04, 3.600e-04, 1.100e-04, 4.300e-05, 1.900e-05,
                                        6.300e-06, 1.400e-07, 1.000e-09, 0.000e+00],

                                       [5.900e+00, 4.200e+00, 2.900e+00, 1.800e+00, 1.100e+00, 6.400e-01,
                                        3.800e-01, 2.100e-01, 1.200e-01, 4.600e-02, 1.800e-02, 8.200e-03,
                                        3.700e-03, 1.800e-03, 8.400e-04, 7.200e-04, 6.100e-04, 5.200e-04,
                                        4.400e-04, 4.400e-04, 4.400e-04, 4.800e-04, 5.200e-04, 5.700e-04,
                                        6.100e-04, 6.600e-04, 3.800e-04, 1.600e-04, 6.700e-05, 3.200e-05,
                                        1.200e-05, 1.500e-07, 1.000e-09, 0.000e+00]
                                       ])

    # Ozone density profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    ozone_density_profiles = np.array([[5.600e-05, 5.600e-05, 5.400e-05, 5.100e-05, 4.700e-05, 4.500e-05,
                                        4.300e-05, 4.100e-05, 3.900e-05, 3.900e-05, 3.900e-05, 4.100e-05,
                                        4.300e-05, 4.500e-05, 4.500e-05, 4.700e-05, 4.700e-05, 6.900e-05,
                                        9.000e-05, 1.400e-04, 1.900e-04, 2.400e-04, 2.800e-04, 3.200e-04,
                                        3.400e-04, 3.400e-04, 2.400e-04, 9.200e-05, 4.100e-05, 1.300e-05,
                                        4.300e-06, 8.600e-08, 4.300e-11, 0.000e+00],

                                       [6.000e-05, 6.000e-05, 6.000e-05, 6.200e-05, 6.400e-05, 6.600e-05,
                                        6.900e-05, 7.500e-05, 7.900e-05, 8.600e-05, 9.000e-05, 1.100e-04,
                                        1.200e-04, 1.500e-04, 1.800e-04, 1.900e-04, 2.100e-04, 2.400e-04,
                                        2.800e-04, 3.200e-04, 3.400e-04, 3.600e-04, 3.600e-04, 3.400e-04,
                                        3.200e-04, 3.000e-04, 2.000e-04, 9.200e-05, 4.100e-05, 1.300e-05,
                                        4.300e-06, 8.600e-08, 4.300e-11, 0.000e+00],

                                       [6.000e-05, 5.400e-05, 4.900e-05, 4.900e-05, 4.900e-05, 5.800e-05,
                                        6.400e-05, 7.700e-05, 9.000e-05, 1.200e-04, 1.600e-04, 2.100e-04,
                                        2.600e-04, 3.000e-04, 3.200e-04, 3.400e-04, 3.600e-04, 3.900e-04,
                                        4.100e-04, 4.300e-04, 4.500e-04, 4.300e-04, 4.300e-04, 3.900e-04,
                                        3.600e-04, 3.400e-04, 1.900e-04, 9.200e-05, 4.100e-05, 1.300e-05,
                                        4.300e-06, 8.600e-08, 4.300e-11, 0.000e+00],

                                       [4.900e-05, 5.400e-05, 5.600e-05, 5.800e-05, 6.000e-05, 6.400e-05,
                                        7.100e-05, 7.500e-05, 7.900e-05, 1.100e-04, 1.300e-04, 1.800e-04,
                                        2.100e-04, 2.600e-04, 2.800e-04, 3.200e-04, 3.400e-04, 3.900e-04,
                                        4.100e-04, 4.100e-04, 3.900e-04, 3.600e-04, 3.200e-04, 3.000e-04,
                                        2.800e-04, 2.600e-04, 1.400e-04, 9.200e-05, 4.100e-05, 1.300e-05,
                                        4.300e-06, 8.600e-08, 4.300e-11, 0.000e+00],

                                       [4.100e-05, 4.100e-05, 4.100e-05, 4.300e-05, 4.500e-05, 4.700e-05,
                                        4.900e-05, 7.100e-05, 9.000e-05, 1.600e-04, 2.400e-04, 3.200e-04,
                                        4.300e-04, 4.700e-04, 4.900e-04, 5.600e-04, 6.200e-04, 6.200e-04,
                                        6.200e-04, 6.000e-04, 5.600e-04, 5.100e-04, 4.700e-04, 4.300e-04,
                                        3.600e-04, 3.200e-04, 1.500e-04, 9.200e-05, 4.100e-05, 1.300e-05,
                                        4.300e-06, 8.600e-08, 4.300e-11, 0.000e+00],

                                       [5.400e-05, 5.400e-05, 5.400e-05, 5.000e-05, 4.600e-05, 4.600e-05,
                                        4.500e-05, 4.900e-05, 5.200e-05, 7.100e-05, 9.000e-05, 1.300e-04,
                                        1.600e-04, 1.700e-04, 1.900e-04, 2.100e-04, 2.400e-04, 2.800e-04,
                                        3.200e-04, 3.500e-04, 3.800e-04, 3.800e-04, 3.900e-04, 3.800e-04,
                                        3.600e-04, 3.400e-04, 2.000e-04, 1.100e-04, 4.900e-05, 1.700e-05,
                                        4.000e-06, 8.600e-08, 4.300e-11, 0.000e+00]
                                       ])

    @classmethod
    def _import_from_arrays(cls, pressure, altitude, temperature, mixing_ratio, base_profile):
        """Import radiosonde data from a set of arrays containing various radiosonde parameters.

        This routine deals with all of the interpolation and combining required for use in 6S.

        The arguments must be:

        * `pressure` in hPa or millibars
        * `altitude` in km
        * `temperature` in celsius
        * `mixing_ratio` in g/kg

        This returns an atmospheric profile suitable for storing in s.atmos_profile.
        """
        # Interpolate to 6S levels
        max_alt = np.max(altitude)

        interp_altitudes = cls.sixs_altitudes[cls.sixs_altitudes < max_alt]

        f_interp_pressure = interp1d(altitude, pressure, bounds_error=False, fill_value=pressure[0])
        f_interp_temp = interp1d(altitude, temperature, bounds_error=False, fill_value=temperature[0])
        f_interp_mixrat = interp1d(altitude, mixing_ratio, bounds_error=False, fill_value=mixing_ratio[0])

        int_pres = f_interp_pressure(interp_altitudes)
        int_temp = f_interp_temp(interp_altitudes)
        int_mixrat = f_interp_mixrat(interp_altitudes)

        base_profile_index = base_profile - 1

        # Convert units (temperature from C -> K and mixing ratio to density)
        int_temp = cls._celsius_to_kelvin(int_temp)
        int_water = cls._mixing_ratio_to_density(int_pres, int_temp, int_mixrat)

        # Get the rest of the profile from the base profiles
        rest_of_pres = cls.pressure_profiles[base_profile_index]
        rest_of_pres = rest_of_pres[cls.sixs_altitudes >= max_alt]

        rest_of_temp = cls.temp_profiles[base_profile_index]
        rest_of_temp = rest_of_temp[cls.sixs_altitudes >= max_alt]

        rest_of_water = cls.water_density_profiles[base_profile_index]
        rest_of_water = rest_of_water[cls.sixs_altitudes >= max_alt]

        final_pressure = np.hstack((int_pres, rest_of_pres))
        final_temp = np.hstack((int_temp, rest_of_temp))
        final_water = np.hstack((int_water, rest_of_water))
        final_ozone = cls.ozone_density_profiles[base_profile_index]

        params = {'altitude': cls.sixs_altitudes,
                  'pressure': final_pressure,
                  'temperature': final_temp,
                  'water': final_water,
                  'ozone': final_ozone}

        return AtmosProfile.RadiosondeProfile(params)

    @classmethod
    def import_uow_radiosonde_data(cls, url, base_profile):
        """Imports radiosonde data from the University of Wyoming website (http://weather.uwyo.edu/upperair/sounding.html) for use in Py6S.

        Arguments:

        * ``url`` -- The URL of the sounding results page on the UoW website
        * ``base_profile`` -- One of the predefined Atmospheric Profiles to use for any parts of the profile which the radiosonde data does not cover (>40km normally)

        Return value:

        A value suitable for assigning to ``s.atmos_profile``, where ``s`` is a :class:`.SixS` instance.

        How to use:

        1. Go to http://weather.uwyo.edu/upperair/sounding.html and use the interface to select the sounding that you want. Ensure that the From and To date/times are the same, so that only one sounding is retrieved.

        #. Copy the URL of the page displaying the sounding. It will look something like http://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR=2012&MONTH=02&FROM=2712&TO=2712&STNM=03808

        #. Call this function with the URL as the first argument, and one of the predefined atmospheric profiles (eg. ``AtmosProfile.MidlatitudeSummer`` or ``AtmosProfile.Tropical``) as the second argument, and store the result in the atmos_profile attribute of a SixS instance. For example::

              s.atmos_profile = SixSHelpers.Radiosonde.import_uow_radiosonde_data("http://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR=2012&MONTH=02&FROM=2712&TO=2712&STNM=03808", AtmosProfile.MidlatitudeWinter)

        The water density, pressure and temperature values from the radiosonde sounding will be interpolated to the 6S atmospheric grid and used for the 6S parameterisation. As radiosonde data tends to end at an altitude of around 30-40km, the data from the selected base profile is used above that height. Ozone data is not imported from the radiosonde data, as most radiosondes do not collect ozone density measurements, so the entire profile is taken from the base profile selected.

        """
        # Get data from given URL
        u = urllib.urlopen(url)

        if u.getcode() != 200:
            # We have't got the HTTP OK status code, so something is wrong (like the URL is invalid)
            raise ParameterException("url", "The URL for importing radiosonde data is not giving a valid response")

        html = u.read()
        if sys.version_info[0] >= 3:
            html = html.decode()

        if "Sorry, the server is too busy to process your request" in html:
            raise ParameterException("url", "The server is too busy")

        # Extract the data inside the PRE tag (we can do it like this because it is very simple HTML)
        regex = re.compile("<PRE>(.*?)</PRE>", re.IGNORECASE | re.DOTALL)
        r = regex.search(html)
        table = r.groups()[0].strip()

        # Remove last line as it is normally incomplete
        spl = table.split("\n")
        spl = spl[:-1]
        table = "\n".join(spl)

        # Import to NumPy arrays
        s = io.BytesIO(table.encode())
        array = np.genfromtxt(s,skip_header=4, delimiter=7,usecols=(0, 1, 2, 5),filling_values=0)

        pressure = array[:, 0]
        altitude = array[:, 1] / 1000
        temperature = array[:, 2]
        mixing_ratio = array[:, 3]

        return cls._import_from_arrays(pressure, altitude, temperature, mixing_ratio, base_profile)

    @classmethod
    def import_bas_radiosonde_data(cls, filename, base_profile):
        """Imports a radiosonde profile from the British Antarctic Survey radiosonde format.

        TODO: More details here after checking with Martin
        """
        # Import to NumPy arrays
        array = np.loadtxt(filename, skiprows=1, usecols=(2, 3, 4, 6))

        pressure = array[:, 0]
        altitude = array[:, 1] / 1000
        temperature = array[:, 2]
        dewpoint = array[:, 3]

        mixing_ratio = cls._calculate_mixing_ratio(dewpoint, pressure)

        return cls._import_from_arrays(pressure, altitude, temperature, mixing_ratio, base_profile)

    @classmethod
    def _calculate_mixing_ratio(cls, dewpoint_temp, pressure):
        """Calculates the mixing ratio from dewpoint temperature and pressure measurements.

        Requires the dewpoint temperature to be in celsius andthe pressure to be in hPa, which
        is the same as millibars.
        """
        e = 6.11 * 10 ** ((7.5 * dewpoint_temp) / (237.7 + dewpoint_temp))
        mixing_ratio = 621.97 * (e / (pressure - e))

        return mixing_ratio

    @classmethod
    def _celsius_to_kelvin(cls, temp):
        """Converts the argument (which may be a scalar or a ndarray) from a temperature in degrees Celsius to a temperature in Kelvin."""
        return temp + 273.15

    @classmethod
    def _mixing_ratio_to_density(cls, pres, temp, mixrat):
        """Converts mixing ratio (measured in g/kg) to density (measured in g/m3).

        This is designed for use with mixing ratios derived from radiosonde measurements,
        where the mixing ratio defines the grams of water per kg of dry air.

        Arguments:

        * ``pres`` -- Pressure in mb
        * ``temp`` -- Temperature in K
        * ``mixrat`` -- Mixing ratio in g/kg

        All arguments can be scalars or ndarrays - if the latter then they must all be the same length.

        """

        mass = 0.3484 * (pres / temp) * (1 - (0.000379 * mixrat))

        density = mixrat * mass

        return density
