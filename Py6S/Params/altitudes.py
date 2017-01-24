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


class Altitudes:

    """Allows the specification of target and sensor altitudes."""

    def __init__(self):
        self.target_alt_pres = None
        self.sensor_alt_pres = None
        self.sensor_altitude = None
        self.aot = None
        self.water = None
        self.ozone = None

    def set_target_sea_level(self):
        """Set the altitude of the target to be at sea level (0km)"""

        self.target_alt_pres = 0

    def set_target_custom_altitude(self, altitude):
        """Set the altitude of the target.

        Arguments:
         * `altitude` -- The altitude of the target, in km

        """

        self.target_alt_pres = -1 * altitude

    def set_target_pressure(self, pressure):
        """Set the pressure of the target (a proxy for the height of the target).

        Arguments:
         * `pressure` -- The pressure at the target, in mb

        """

        self.target_alt_pres = pressure

    def set_sensor_sea_level(self):
        """Set the sensor altitude to be sea level."""
        # Reset the sensor_altitude (as used by set_sensor_custom_altitude()) to None
        # before setting the sensor_alt_pres
        self.sensor_altitude = None
        self.sensor_alt_pres = 0

    def set_sensor_satellite_level(self):
        """Set the sensor altitude to be satellite level."""
        # Reset the sensor_altitude (as used by set_sensor_custom_altitude()) to None
        # before setting the sensor_alt_pres
        self.sensor_altitude = None
        self.sensor_alt_pres = -1000

    def set_sensor_custom_altitude(self, altitude, aot=-1, water=-1, ozone=-1):
        """Set the altitude of the sensor, along with other variables required for the parameterisation
        of the sensor.

        Takes optional arguments of `aot`, `water` and `ozone` to specify atmospheric contents underneath
        the sensor. If these aren't specified then the water and ozone contents will be interpolated from
        the US-1962 standard atmosphere, and the AOT will be interpolated from a 2km exponential aerosol
        profile.

        Arguments:
         * `altitude` -- The altitude of the sensor, in km.
         * `aot` -- (Optional, keyword argument) The AOT at 550nm at the sensor
         * `water` -- (Optional, keyword argument) The water vapour content (in g/cm^2) at the sensor
         * `ozone` -- (Optional, keyword argument) The ozone content (in cm-atm) at the sensor

        Example usage::

          s.altitudes.set_sensor_custom_altitude(8, 0.35, 1.6, 0.4) # Altitude of 8km, AOT of 0.35, Water content of 1.6g/cm^2 and Ozone of 0.4cm-atm

        """
        if altitude < 0 or altitude >= 100:
            raise ValueError('Sensor altitude must be > 0km and < 100km')
        self.sensor_altitude = -1 * altitude
        self.aot = aot
        self.water = water
        self.ozone = ozone

    def __str__(self):
        if self.sensor_altitude is None:
            return "%f\n%f\n" % (self.target_alt_pres, self.sensor_alt_pres)
        else:
            return "%f\n%f\n%f %f\n%f\n" % (self.target_alt_pres, self.sensor_altitude, self.water, self.ozone, self.aot)
