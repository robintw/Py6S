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
import sys

# Fix for Python 3 where long is not available
if sys.version_info[0] >= 3:
    long = int

class Geometry:

    class User:

        """Stores parameters for a user-defined geometry for 6S.

        Attributes:

         * ``solar_z`` -- Solar zenith angle
         * ``solar_a`` -- Solar azimuth angle
         * ``view_z`` -- View zenith angle
         * ``view_a`` -- View azimuth angle
         * ``day`` -- The day the image was acquired in (1-31)
         * ``month`` -- The month the image was acquired in (0-12)

        """

        solar_z = 0
        solar_a = 0
        view_z = 0
        view_a = 0
        day = 1
        month = 1

        def __str__(self):
            return '0 (User defined)\n%f %f %f %f %d %d\n' % (self.solar_z, self.solar_a, self.view_z, self.view_a, self.month, self.day)

        def from_time_and_location(self, lat, lon, datetimestring, view_z, view_a):
            """Sets the user-defined geometry to a given view zenith and azimuth, and a solar zenith and azimuth calculated from the lat, lon and date given.

            Uses the PySolar module for the calculations.

            Arguments:

            * ``lat`` -- The latitude of the location (0-90 degrees)
            * ``lon`` -- The longitude of the location
            * ``datetimestring`` -- Any string that can be parsed to produce a date/time object. All that is really needed is a time - eg. "14:53"
            * ``view_z`` -- The view zenith angle
            * ``view_a`` -- The view azimuth angle

            """
            # Try and import the PySolar module, if it fails give an error message
            try:
                import Pysolar
            except:
                raise ImportError("To set the geometry from a time and location you must have the PySolar module installed.\nPy6S requires Pysolar v0.6.\nTo install this, run 'pip install pysolar==0.6' at the command line.")

            dt = dateutil.parser.parse(datetimestring, dayfirst=True)
            self.solar_z = 90.0 - Pysolar.GetAltitude(lat, lon, dt)

            az = Pysolar.GetAzimuth(lat, lon, dt)

            if az < 0:
                self.solar_a = abs(az) + 180
            else:
                self.solar_a = abs(az - 180)

            self.solar_a = self.solar_a % 360

            self.day = dt.day
            self.month = dt.month

            self.view_z = view_z
            self.view_a = view_a

    class Meteosat:

        """Stores parameters for a Meteosat geometry for 6S.

        Attributes:

          * ``month`` -- The month the image was acquired in (0-12)
          * ``day`` -- The day the image was acquired in (1-31)
          * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
          * ``column`` -- The Meteosat column of the image
          * ``line`` -- The Meteosat line of the image

        """

        month = 1
        day = 1
        gmt_decimal_hour = 0
        column = 0
        line = 0

        def __str__(self):
            return '1 (Meteosat)\n%d %d %f %d %d (Geometrical Conditions)\n' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)

    class GoesEast:

        """Stores parameters for a GOES East geometry for 6S.

        Attributes:

         * ``month`` -- The month the image was acquired in (0-12)
         * ``day`` -- The day the image was acquired in (1-31)
         * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
         * ``column`` -- The GOES East column of the image
         * ``line`` -- The GOES East line of the image

        """
        month = 1
        day = 1
        gmt_decimal_hour = 0
        column = 0
        line = 0

        def __str__(self):
            return '2 (Goes East)\n%d %d %f %d %d (Geometrical Conditions)\n' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)

    class GoesWest:

        """Stores parameters for a GOES West geometry for 6S.

        Attributes:

         * ``month`` -- The month the image was acquired in (0-12)
         * ``day`` -- The day the image was acquired in (1-31)
         * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
         * ``column`` -- The GOES West column of the image
         * ``line`` -- The GOES West line of the image

        """
        month = 1
        day = 1
        gmt_decimal_hour = 0
        column = 0
        line = 0

        def __str__(self):
            return '3 (Goes West)\n%d %d %f %d %d (Geometrical Conditions)\n' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)

    class AVHRR_PM:

        """Stores parameters for a AVHRR afternoon pass geometry for 6S.

        Attributes:

         * ``month`` -- The month the image was acquired in (0-12)
         * ``day`` -- The day the image was acquired in (1-31)
         * ``column`` -- The AVHRR column of the image
         * ``ascendant_node_longitude`` -- The longitude of the ascendant node of the image
         * ``ascendant_node_hour`` -- The hour of the ascendant node of the image

        """
        month = 1
        day = 1
        gmt_decimal_hour = 0
        column = 0
        ascendant_node_longitude = 0
        ascendant_node_hour = 0

        def __str__(self):
            return '4 (AVHRR PM NOAA)\n%d %d %d %f %f (Geometrical Conditions)\n' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.ascendant_node_longitude, self.ascendant_node_hour)

    class AVHRR_AM:

        """Stores parameters for a AVHRR morning pass geometry for 6S.

        Attributes:

         * ``month`` -- The month the image was acquired in (0-12)
         * ``day`` -- The day the image was acquired in (1-31)
         * ``column`` -- The AVHRR column of the image
         * ``ascendant_node_longitude`` -- The longitude of the ascendant node of the image
         * ``ascendant_node_hour`` -- The hour of the ascendant node of the image

        """
        month = 1
        day = 1
        gmt_decimal_hour = 0
        column = 0
        ascendant_node_longitude = 0
        ascendant_node_hour = 0

        def __str__(self):
            return '5 (AVHRR AM NOAA)\n%d %d %d %f %f (Geometrical Conditions)\n' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.ascendant_node_longitude, self.ascendant_node_hour)

    class SPOT_HRV:

        """Stores parameters for a SPOT HRV geometry for 6S.

        Attributes:

         * ``month`` -- The month the image was acquired in (0-12)
         * ``day`` -- The day the image was acquired in (1-31)
         * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
         * ``latitude`` -- The latitude of the centre of the image
         * ``longitude`` -- The longitude of the centre of the image

        """
        month = 1
        day = 1
        gmt_decimal_hour = 0
        longitude = 0
        latitude = 0

        def __str__(self):
            return '6 (SPOT)\n%d %d %f %f %f (Geometrical Conditions)\n' % (self.month, self.day, self.gmt_decimal_hour, self.longitude, self.latitude)

    class Landsat_TM:

        """Stores parameters for a Landsat TM geometry for 6S.

        Attributes:

         * ``month`` -- The month the image was acquired in (0-12)
         * ``day`` -- The day the image was acquired in (1-31)
         * ``gmt_decimal_hour`` -- The time in GMT, as a decimal, in hours (eg. 7.5 for 7:30am)
         * ``latitude`` -- The latitude of the centre of the image
         * ``longitude`` -- The longitude of the centre of the image

        """
        month = 1
        day = 1
        gmt_decimal_hour = 0
        longitude = 0
        latitude = 0

        def __str__(self):
            return '7 (TM)\n%d %d %f %f %f (Geometrical Conditions)\n' % (self.month, self.day, self.gmt_decimal_hour, self.longitude, self.latitude)
