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

import io
import re
import sys

import numpy as np
from scipy.interpolate import interp1d

from ..Params import AtmosProfile
from ..sixs_exceptions import ParameterError

if sys.version_info[0] >= 3:
    import urllib.request as urllib
else:
    import urllib


class Radiosonde:

    sixs_altitudes = np.array(
        [
            0.0,
            1.0,
            2.0,
            3.0,
            4.0,
            5.0,
            6.0,
            7.0,
            8.0,
            9.0,
            10.0,
            11.0,
            12.0,
            13.0,
            14.0,
            15.0,
            16.0,
            17.0,
            18.0,
            19.0,
            20.0,
            21.0,
            22.0,
            23.0,
            24.0,
            25.0,
            30.0,
            35.0,
            40.0,
            45.0,
            50.0,
            70.0,
            100.0,
            99999.0,
        ]
    )

    # Temperature profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    temp_profiles = np.array(
        [
            [
                3.000e02,
                2.940e02,
                2.880e02,
                2.840e02,
                2.770e02,
                2.700e02,
                2.640e02,
                2.570e02,
                2.500e02,
                2.440e02,
                2.370e02,
                2.300e02,
                2.240e02,
                2.170e02,
                2.100e02,
                2.040e02,
                1.970e02,
                1.950e02,
                1.990e02,
                2.030e02,
                2.070e02,
                2.110e02,
                2.150e02,
                2.170e02,
                2.190e02,
                2.210e02,
                2.320e02,
                2.430e02,
                2.540e02,
                2.650e02,
                2.700e02,
                2.190e02,
                2.100e02,
                2.100e02,
            ],
            [
                2.940e02,
                2.900e02,
                2.850e02,
                2.790e02,
                2.730e02,
                2.670e02,
                2.610e02,
                2.550e02,
                2.480e02,
                2.420e02,
                2.350e02,
                2.290e02,
                2.220e02,
                2.160e02,
                2.160e02,
                2.160e02,
                2.160e02,
                2.160e02,
                2.160e02,
                2.170e02,
                2.180e02,
                2.190e02,
                2.200e02,
                2.220e02,
                2.230e02,
                2.240e02,
                2.340e02,
                2.450e02,
                2.580e02,
                2.700e02,
                2.760e02,
                2.180e02,
                2.100e02,
                2.100e02,
            ],
            [
                2.722e02,
                2.687e02,
                2.652e02,
                2.617e02,
                2.557e02,
                2.497e02,
                2.437e02,
                2.377e02,
                2.317e02,
                2.257e02,
                2.197e02,
                2.192e02,
                2.187e02,
                2.182e02,
                2.177e02,
                2.172e02,
                2.167e02,
                2.162e02,
                2.157e02,
                2.152e02,
                2.152e02,
                2.152e02,
                2.152e02,
                2.152e02,
                2.152e02,
                2.152e02,
                2.174e02,
                2.278e02,
                2.432e02,
                2.585e02,
                2.657e02,
                2.307e02,
                2.102e02,
                2.100e02,
            ],
            [
                2.870e02,
                2.820e02,
                2.760e02,
                2.710e02,
                2.660e02,
                2.600e02,
                2.530e02,
                2.460e02,
                2.390e02,
                2.320e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.250e02,
                2.260e02,
                2.280e02,
                2.350e02,
                2.470e02,
                2.620e02,
                2.740e02,
                2.770e02,
                2.160e02,
                2.100e02,
                2.100e02,
            ],
            [
                2.571e02,
                2.591e02,
                2.559e02,
                2.527e02,
                2.477e02,
                2.409e02,
                2.341e02,
                2.273e02,
                2.206e02,
                2.172e02,
                2.172e02,
                2.172e02,
                2.172e02,
                2.172e02,
                2.172e02,
                2.172e02,
                2.166e02,
                2.160e02,
                2.154e02,
                2.148e02,
                2.141e02,
                2.136e02,
                2.130e02,
                2.124e02,
                2.118e02,
                2.112e02,
                2.160e02,
                2.222e02,
                2.347e02,
                2.470e02,
                2.593e02,
                2.457e02,
                2.100e02,
                2.100e02,
            ],
            [
                2.881e02,
                2.816e02,
                2.751e02,
                2.687e02,
                2.622e02,
                2.557e02,
                2.492e02,
                2.427e02,
                2.362e02,
                2.297e02,
                2.232e02,
                2.168e02,
                2.166e02,
                2.166e02,
                2.166e02,
                2.166e02,
                2.166e02,
                2.166e02,
                2.166e02,
                2.166e02,
                2.166e02,
                2.176e02,
                2.186e02,
                2.196e02,
                2.206e02,
                2.216e02,
                2.265e02,
                2.365e02,
                2.534e02,
                2.642e02,
                2.706e02,
                2.197e02,
                2.100e02,
                2.100e02,
            ],
        ]
    )

    # Pressure profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    pressure_profiles = np.array(
        [
            [
                1.013e03,
                9.040e02,
                8.050e02,
                7.150e02,
                6.330e02,
                5.590e02,
                4.920e02,
                4.320e02,
                3.780e02,
                3.290e02,
                2.860e02,
                2.470e02,
                2.130e02,
                1.820e02,
                1.560e02,
                1.320e02,
                1.110e02,
                9.370e01,
                7.890e01,
                6.660e01,
                5.650e01,
                4.800e01,
                4.090e01,
                3.500e01,
                3.000e01,
                2.570e01,
                1.220e01,
                6.000e00,
                3.050e00,
                1.590e00,
                8.540e-01,
                5.790e-02,
                3.000e-04,
                0.000e00,
            ],
            [
                1.013e03,
                9.020e02,
                8.020e02,
                7.100e02,
                6.280e02,
                5.540e02,
                4.870e02,
                4.260e02,
                3.720e02,
                3.240e02,
                2.810e02,
                2.430e02,
                2.090e02,
                1.790e02,
                1.530e02,
                1.300e02,
                1.110e02,
                9.500e01,
                8.120e01,
                6.950e01,
                5.950e01,
                5.100e01,
                4.370e01,
                3.760e01,
                3.220e01,
                2.770e01,
                1.320e01,
                6.520e00,
                3.330e00,
                1.760e00,
                9.510e-01,
                6.710e-02,
                3.000e-04,
                0.000e00,
            ],
            [
                1.018e03,
                8.973e02,
                7.897e02,
                6.938e02,
                6.081e02,
                5.313e02,
                4.627e02,
                4.016e02,
                3.473e02,
                2.992e02,
                2.568e02,
                2.199e02,
                1.882e02,
                1.610e02,
                1.378e02,
                1.178e02,
                1.007e02,
                8.610e01,
                7.350e01,
                6.280e01,
                5.370e01,
                4.580e01,
                3.910e01,
                3.340e01,
                2.860e01,
                2.430e01,
                1.110e01,
                5.180e00,
                2.530e00,
                1.290e00,
                6.820e-01,
                4.670e-02,
                3.000e-04,
                0.000e00,
            ],
            [
                1.010e03,
                8.960e02,
                7.929e02,
                7.000e02,
                6.160e02,
                5.410e02,
                4.730e02,
                4.130e02,
                3.590e02,
                3.107e02,
                2.677e02,
                2.300e02,
                1.977e02,
                1.700e02,
                1.460e02,
                1.250e02,
                1.080e02,
                9.280e01,
                7.980e01,
                6.860e01,
                5.890e01,
                5.070e01,
                4.360e01,
                3.750e01,
                3.227e01,
                2.780e01,
                1.340e01,
                6.610e00,
                3.400e00,
                1.810e00,
                9.870e-01,
                7.070e-02,
                3.000e-04,
                0.000e00,
            ],
            [
                1.013e03,
                8.878e02,
                7.775e02,
                6.798e02,
                5.932e02,
                5.158e02,
                4.467e02,
                3.853e02,
                3.308e02,
                2.829e02,
                2.418e02,
                2.067e02,
                1.766e02,
                1.510e02,
                1.291e02,
                1.103e02,
                9.431e01,
                8.058e01,
                6.882e01,
                5.875e01,
                5.014e01,
                4.277e01,
                3.647e01,
                3.109e01,
                2.649e01,
                2.256e01,
                1.020e01,
                4.701e00,
                2.243e00,
                1.113e00,
                5.719e-01,
                4.016e-02,
                3.000e-04,
                0.000e00,
            ],
            [
                1.013e03,
                8.986e02,
                7.950e02,
                7.012e02,
                6.166e02,
                5.405e02,
                4.722e02,
                4.111e02,
                3.565e02,
                3.080e02,
                2.650e02,
                2.270e02,
                1.940e02,
                1.658e02,
                1.417e02,
                1.211e02,
                1.035e02,
                8.850e01,
                7.565e01,
                6.467e01,
                5.529e01,
                4.729e01,
                4.047e01,
                3.467e01,
                2.972e01,
                2.549e01,
                1.197e01,
                5.746e00,
                2.871e00,
                1.491e00,
                7.978e-01,
                5.520e-02,
                3.008e-04,
                0.000e00,
            ],
        ]
    )

    # Water density profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    water_density_profiles = np.array(
        [
            [
                1.900e01,
                1.300e01,
                9.300e00,
                4.700e00,
                2.200e00,
                1.500e00,
                8.500e-01,
                4.700e-01,
                2.500e-01,
                1.200e-01,
                5.000e-02,
                1.700e-02,
                6.000e-03,
                1.800e-03,
                1.000e-03,
                7.600e-04,
                6.400e-04,
                5.600e-04,
                5.000e-04,
                4.900e-04,
                4.500e-04,
                5.100e-04,
                5.100e-04,
                5.400e-04,
                6.000e-04,
                6.700e-04,
                3.600e-04,
                1.100e-04,
                4.300e-05,
                1.900e-05,
                6.300e-06,
                1.400e-07,
                1.000e-09,
                0.000e00,
            ],
            [
                1.400e01,
                9.300e00,
                5.900e00,
                3.300e00,
                1.900e00,
                1.000e00,
                6.100e-01,
                3.700e-01,
                2.100e-01,
                1.200e-01,
                6.400e-02,
                2.200e-02,
                6.000e-03,
                1.800e-03,
                1.000e-03,
                7.600e-04,
                6.400e-04,
                5.600e-04,
                5.000e-04,
                4.900e-04,
                4.500e-04,
                5.100e-04,
                5.100e-04,
                5.400e-04,
                6.000e-04,
                6.700e-04,
                3.600e-04,
                1.100e-04,
                4.300e-05,
                1.900e-05,
                1.300e-06,
                1.400e-07,
                1.000e-09,
                0.000e00,
            ],
            [
                3.500e00,
                2.500e00,
                1.800e00,
                1.200e00,
                6.600e-01,
                3.800e-01,
                2.100e-01,
                8.500e-02,
                3.500e-02,
                1.600e-02,
                7.500e-03,
                6.900e-03,
                6.000e-03,
                1.800e-03,
                1.000e-03,
                7.600e-04,
                6.400e-04,
                5.600e-04,
                5.000e-04,
                4.900e-04,
                4.500e-04,
                5.100e-04,
                5.100e-04,
                5.400e-04,
                6.000e-04,
                6.700e-04,
                3.600e-04,
                1.100e-04,
                4.300e-05,
                1.900e-05,
                6.300e-06,
                1.400e-07,
                1.000e-09,
                0.000e00,
            ],
            [
                9.100e00,
                6.000e00,
                4.200e00,
                2.700e00,
                1.700e00,
                1.000e00,
                5.400e-01,
                2.900e-01,
                1.300e-01,
                4.200e-02,
                1.500e-02,
                9.400e-03,
                6.000e-03,
                1.800e-03,
                1.000e-03,
                7.600e-04,
                6.400e-04,
                5.600e-04,
                5.000e-04,
                4.900e-04,
                4.500e-04,
                5.100e-04,
                5.100e-04,
                5.400e-04,
                6.000e-04,
                6.700e-04,
                3.600e-04,
                1.100e-04,
                4.300e-05,
                1.900e-05,
                6.300e-06,
                1.400e-07,
                1.000e-09,
                0.000e00,
            ],
            [
                1.200e00,
                1.200e00,
                9.400e-01,
                6.800e-01,
                4.100e-01,
                2.000e-01,
                9.800e-02,
                5.400e-02,
                1.100e-02,
                8.400e-03,
                5.500e-03,
                3.800e-03,
                2.600e-03,
                1.800e-03,
                1.000e-03,
                7.600e-04,
                6.400e-04,
                5.600e-04,
                5.000e-04,
                4.900e-04,
                4.500e-04,
                5.100e-04,
                5.100e-04,
                5.400e-04,
                6.000e-04,
                6.700e-04,
                3.600e-04,
                1.100e-04,
                4.300e-05,
                1.900e-05,
                6.300e-06,
                1.400e-07,
                1.000e-09,
                0.000e00,
            ],
            [
                5.900e00,
                4.200e00,
                2.900e00,
                1.800e00,
                1.100e00,
                6.400e-01,
                3.800e-01,
                2.100e-01,
                1.200e-01,
                4.600e-02,
                1.800e-02,
                8.200e-03,
                3.700e-03,
                1.800e-03,
                8.400e-04,
                7.200e-04,
                6.100e-04,
                5.200e-04,
                4.400e-04,
                4.400e-04,
                4.400e-04,
                4.800e-04,
                5.200e-04,
                5.700e-04,
                6.100e-04,
                6.600e-04,
                3.800e-04,
                1.600e-04,
                6.700e-05,
                3.200e-05,
                1.200e-05,
                1.500e-07,
                1.000e-09,
                0.000e00,
            ],
        ]
    )

    # Ozone density profiles used in 6S, for different profiles, in order: Tropical, MidLat Sum, MidLat Winter, SubArc Sum, SubArc Winter, USStd62
    ozone_density_profiles = np.array(
        [
            [
                5.600e-05,
                5.600e-05,
                5.400e-05,
                5.100e-05,
                4.700e-05,
                4.500e-05,
                4.300e-05,
                4.100e-05,
                3.900e-05,
                3.900e-05,
                3.900e-05,
                4.100e-05,
                4.300e-05,
                4.500e-05,
                4.500e-05,
                4.700e-05,
                4.700e-05,
                6.900e-05,
                9.000e-05,
                1.400e-04,
                1.900e-04,
                2.400e-04,
                2.800e-04,
                3.200e-04,
                3.400e-04,
                3.400e-04,
                2.400e-04,
                9.200e-05,
                4.100e-05,
                1.300e-05,
                4.300e-06,
                8.600e-08,
                4.300e-11,
                0.000e00,
            ],
            [
                6.000e-05,
                6.000e-05,
                6.000e-05,
                6.200e-05,
                6.400e-05,
                6.600e-05,
                6.900e-05,
                7.500e-05,
                7.900e-05,
                8.600e-05,
                9.000e-05,
                1.100e-04,
                1.200e-04,
                1.500e-04,
                1.800e-04,
                1.900e-04,
                2.100e-04,
                2.400e-04,
                2.800e-04,
                3.200e-04,
                3.400e-04,
                3.600e-04,
                3.600e-04,
                3.400e-04,
                3.200e-04,
                3.000e-04,
                2.000e-04,
                9.200e-05,
                4.100e-05,
                1.300e-05,
                4.300e-06,
                8.600e-08,
                4.300e-11,
                0.000e00,
            ],
            [
                6.000e-05,
                5.400e-05,
                4.900e-05,
                4.900e-05,
                4.900e-05,
                5.800e-05,
                6.400e-05,
                7.700e-05,
                9.000e-05,
                1.200e-04,
                1.600e-04,
                2.100e-04,
                2.600e-04,
                3.000e-04,
                3.200e-04,
                3.400e-04,
                3.600e-04,
                3.900e-04,
                4.100e-04,
                4.300e-04,
                4.500e-04,
                4.300e-04,
                4.300e-04,
                3.900e-04,
                3.600e-04,
                3.400e-04,
                1.900e-04,
                9.200e-05,
                4.100e-05,
                1.300e-05,
                4.300e-06,
                8.600e-08,
                4.300e-11,
                0.000e00,
            ],
            [
                4.900e-05,
                5.400e-05,
                5.600e-05,
                5.800e-05,
                6.000e-05,
                6.400e-05,
                7.100e-05,
                7.500e-05,
                7.900e-05,
                1.100e-04,
                1.300e-04,
                1.800e-04,
                2.100e-04,
                2.600e-04,
                2.800e-04,
                3.200e-04,
                3.400e-04,
                3.900e-04,
                4.100e-04,
                4.100e-04,
                3.900e-04,
                3.600e-04,
                3.200e-04,
                3.000e-04,
                2.800e-04,
                2.600e-04,
                1.400e-04,
                9.200e-05,
                4.100e-05,
                1.300e-05,
                4.300e-06,
                8.600e-08,
                4.300e-11,
                0.000e00,
            ],
            [
                4.100e-05,
                4.100e-05,
                4.100e-05,
                4.300e-05,
                4.500e-05,
                4.700e-05,
                4.900e-05,
                7.100e-05,
                9.000e-05,
                1.600e-04,
                2.400e-04,
                3.200e-04,
                4.300e-04,
                4.700e-04,
                4.900e-04,
                5.600e-04,
                6.200e-04,
                6.200e-04,
                6.200e-04,
                6.000e-04,
                5.600e-04,
                5.100e-04,
                4.700e-04,
                4.300e-04,
                3.600e-04,
                3.200e-04,
                1.500e-04,
                9.200e-05,
                4.100e-05,
                1.300e-05,
                4.300e-06,
                8.600e-08,
                4.300e-11,
                0.000e00,
            ],
            [
                5.400e-05,
                5.400e-05,
                5.400e-05,
                5.000e-05,
                4.600e-05,
                4.600e-05,
                4.500e-05,
                4.900e-05,
                5.200e-05,
                7.100e-05,
                9.000e-05,
                1.300e-04,
                1.600e-04,
                1.700e-04,
                1.900e-04,
                2.100e-04,
                2.400e-04,
                2.800e-04,
                3.200e-04,
                3.500e-04,
                3.800e-04,
                3.800e-04,
                3.900e-04,
                3.800e-04,
                3.600e-04,
                3.400e-04,
                2.000e-04,
                1.100e-04,
                4.900e-05,
                1.700e-05,
                4.000e-06,
                8.600e-08,
                4.300e-11,
                0.000e00,
            ],
        ]
    )

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
        f_interp_temp = interp1d(
            altitude, temperature, bounds_error=False, fill_value=temperature[0]
        )
        f_interp_mixrat = interp1d(
            altitude, mixing_ratio, bounds_error=False, fill_value=mixing_ratio[0]
        )

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

        params = {
            "altitude": cls.sixs_altitudes,
            "pressure": final_pressure,
            "temperature": final_temp,
            "water": final_water,
            "ozone": final_ozone,
        }

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
            raise ParameterError(
                "url",
                "The URL for importing radiosonde data is not giving a valid response",
            )

        html = u.read()
        if sys.version_info[0] >= 3:
            html = html.decode()

        if "Sorry, the server is too busy to process your request" in html:
            raise ParameterError("url", "The server is too busy")

        # Extract the data inside the PRE tag (we can do it like this because it is very simple HTML)
        regex = re.compile("<PRE>(.*?)</PRE>", re.IGNORECASE | re.DOTALL)
        r = regex.search(html)
        table = r.groups()[0].strip()

        # Remove last line as it is normally incomplete
        spl = table.split("\n")
        spl = spl[:-1]
        table = "\n".join(spl)

        # Check for partly empty first line in U of W data which impacts interpolations:
        if len(table.split("\n")[4].split()) != 11:
            num_skip = 5
        else:
            num_skip = 4

        # Import to NumPy arrays
        s = io.BytesIO(table.encode())
        array = np.genfromtxt(
            s, skip_header=num_skip, delimiter=7, usecols=(0, 1, 2, 5), filling_values=0
        )

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
