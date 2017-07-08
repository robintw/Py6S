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

import dateutil.parser

from Py6S.sixs_exceptions import ParameterError


class AtmosProfile:

    """Stores a enumeration for the pre-specified atmospheric model types"""
    NoGaseousAbsorption = 0
    Tropical = 1
    MidlatitudeSummer = 2
    MidlatitudeWinter = 3
    SubarcticSummer = 4
    SubarcticWinter = 5
    USStandard1962 = 6

    @classmethod
    def FromLatitudeAndDate(cls, latitude, date):
        """Automatically pick the atmospheric profile based on the latitude
        and date.

        Based on the table provided at http://www.exelisvis.com/docs/FLAASH.html
        """
        dt = dateutil.parser.parse(date, dayfirst=True)

        rounded_lat = round(latitude, -1)

        # Data from Table 2-2 in http://www.exelisvis.com/docs/FLAASH.html
        SAW = cls.PredefinedType(cls.SubarcticWinter)
        SAS = cls.PredefinedType(cls.SubarcticSummer)
        MLS = cls.PredefinedType(cls.MidlatitudeSummer)
        MLW = cls.PredefinedType(cls.MidlatitudeWinter)
        T = cls.PredefinedType(cls.Tropical)

        ap_JFMA = {80: SAW,
                   70: SAW,
                   60: MLW,
                   50: MLW,
                   40: SAS,
                   30: MLS,
                   20: T,
                   10: T,
                   0: T,
                   -10: T,
                   -20: T,
                   -30: MLS,
                   -40: SAS,
                   -50: SAS,
                   -60: MLW,
                   -70: MLW,
                   -80: MLW
        }

        ap_MJ = {80:SAW,
                 70: MLW,
                 60: MLW,
                 50: SAS,
                 40: SAS,
                 30: MLS,
                 20: T,
                 10: T,
                 0: T,
                 -10: T,
                 -20: T,
                 -30: MLS,
                 -40: SAS,
                 -50: SAS,
                 -60: MLW,
                 -70: MLW,
                 -80: MLW
        }

        ap_JA = {80:MLW,
                 70: MLW,
                 60: SAS,
                 50: SAS,
                 40: MLS,
                 30: T,
                 20: T,
                 10: T,
                 0: T,
                 -10: T,
                 -20: MLS,
                 -30: MLS,
                 -40: SAS,
                 -50: MLW,
                 -60: MLW,
                 -70: MLW,
                 -80: SAW
        }

        ap_SO = {80:  MLW,
                 70:  MLW,
                 60:  SAS,
                 50:  SAS,
                 40:  MLS,
                 30:  T,
                 20:  T,
                 10:  T,
                 0:   T,
                 -10: T,
                 -20: MLS,
                 -30: MLS,
                 -40: SAS,
                 -50: MLW,
                 -60: MLW,
                 -70: MLW,
                 -80: MLW
        }

        ap_ND = {80: SAW,
                 70: SAW,
                 60: MLW,
                 50: SAS,
                 40: SAS,
                 30: MLS,
                 20: T,
                 10: T,
                 0: T,
                 -10: T,
                 -20: T,
                 -30: MLS,
                 -40: SAS,
                 -50: SAS,
                 -60: MLW,
                 -70: MLW,
                 -80: MLW
        }


        ap_dict = {1: ap_JFMA,
                   2: ap_JFMA,
                   3: ap_JFMA,
                   4: ap_JFMA,
                   5: ap_MJ,
                   6: ap_MJ,
                   7: ap_JA,
                   8: ap_JA,
                   9: ap_SO,
                   10: ap_SO,
                   11: ap_ND,
                   12: ap_ND
        }

        return ap_dict[dt.month][rounded_lat]

    @classmethod
    def PredefinedType(cls, type):
        """Set 6S to use a predefined atmosphere type.

        Arguments:

        * ``type`` -- the predefined atmosphere type, one of the constants defined in this class

        Example usage::

          s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeSummer)

        """
        return "%d" % type

    @classmethod
    def UserWaterAndOzone(cls, water, ozone):
        """Set 6S to use an atmosphere defined by an amount of water vapour and ozone.

        Arguments:

        * ``water`` -- The total amount of water in a vertical path through the atmosphere (in g/cm^2)
        * ``ozone`` -- The total amount of ozone in a vertical path through the atmosphere (in cm-atm)

        Example usage::

          s.atmos_profile = AtmosProfile.UserWaterAndOzone(3.6, 0.9)

        """
        return "8 (Water Vapour and Ozone)\n%f %f" % (water, ozone)

    @classmethod
    def RadiosondeProfile(cls, data):
        """Set 6S to use an atmosphere defined by a profile from a radiosonde measurements.

        Arguments:

        * ``data`` -- A dictionary containing five iterables (eg. lists) with the radiosonde measurements in them. The dictionary must have the following keys:
            * ``altitude`` -- in km
            * ``pressure`` -- in mb
            * ``temperature`` -- in k
            * ``water`` -- in g/m^3
            * ``ozone`` -- in g/m^3

        There must be 34 items in each iterable, or a :class:`ParameterExeception` will be thrown.

        """

        # Check to make sure all iterables have 34 items
        all_lists = [data['altitude'], data['pressure'], data['temperature'], data['water'], data['ozone']]
        if not all(len(x) == 34 for x in all_lists):
            raise ParameterError("radiosonde levels", "There must be 34 values in the lists for each radiosonde attribute (altitude, pressure, temperature, water, ozone)")

        result = ""

        for i in range(34):
            result = result + "%f %f %f %f %f\n" % (data['altitude'][i], data['pressure'][i], data['temperature'][i], data['water'][i], data['ozone'][i])

        return "7 User's data base profile\n" + result
