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

import subprocess
import os
import sys
import numpy as np
from scipy.interpolate import interp1d
from .Params import *
from .sixs_exceptions import *
from .outputs import *
import tempfile
import math


SIXSVERSION = '1.1'

# Fix for Python 3 where basestring is not available
if sys.version_info[0] >= 3:
    basestring = str

class SixS(object):

    """Wrapper for the 6S Radiative Transfer Model.

    This is the main class which can be used to instantiate an object which has the key methods for running 6S.

    The most import method in this class is the :meth:`.run` method which writes the 6S input file,
    runs the model and processes the output.

    The parameters of the model are set as the attributes of this class, and the outputs are available as attributes under
    the output attribute.

    For a simple test to ensure that Py6S has found the correct executable for 6S simply
    run the :meth:`.test` method of this class::

      SixS.Test()

    Attributes:

    * ``atmos_profile`` -- The atmospheric profile to use. Should be set to the output of an AtmosProfile method. For example::

                            s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeSummer)

    * ``aero_profile`` -- The aerosol profile to use. Should be set to the output of an AeroProfile method. For example::

                            s.aero_profile = AeroProfile.PredefinedType(AeroProfile.Urban)

    * ``ground_reflectance`` -- The ground reflectance to use. Should be set to the output of a GroundReflectance method. For example::

                            s.ground_reflectance = GroundReflectance.HomogeneousLambertian(0.3)

    * ``geometry`` -- The geometrical settings, including solar and viewing angles. Should be set to an instance of a Geometry class, which can then have various attributes set. For example::

                            s.geometry = GeometryUser()
                            s.geometry.solar_z = 35
                            s.geometry.solar_a = 190

    * ``altitudes`` -- The settings for the sensor and target altitudes. This should be set to an instance of the :meth:`.Altitudes` class, which can then have various attributes set. For example::

                            s.altitudes = Altitudes()
                            s.altitudes.set_target_custom_altitude(2.3)
                            s.altitudes.set_sensor_sea_level()

    * ``wavelength`` -- The wavelength settings. Should be set to the output of the :meth:`.Wavelength()` method. For example::

                            s.wavelength = Wavelength(0.550)

    * ``atmos_corr`` -- The settings for whether to perform atmospheric correction or not, and the parameters for this correction. Should be set to the output of a AtmosCorr method. For example::

                            s.atmos_corr = AtmosCorr.AtmosCorrLambertianFromReflectance(0.23)

    """

    # Stores the outputs from 6S as an instance of the Outputs class
    outputs = None

    min_wv = None
    max_wv = None

    __version__ = "1.7.1"

    def __init__(self, path=None):
        """Initialises the class and finds the right 6S executable to use.

        Sets default parameter values (a set of fairly sensible values that will allow a simple test run to be performed),
        and finds the 6S executable by searching the path.

        Arguments:

        * ``path`` -- (Optional) The path to the 6S executable - if not specified then the system PATH and current directory are searched for the executable.

        """
        self.sixs_path = self._find_path(path)

        self.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.MidlatitudeSummer)
        self.aero_profile = AeroProfile.PredefinedType(AeroProfile.Maritime)

        self.ground_reflectance = GroundReflectance.HomogeneousLambertian(0.3)

        self.geometry = Geometry.User()
        self.geometry.solar_z = 32
        self.geometry.solar_a = 264
        self.geometry.view_z = 23
        self.geometry.view_a = 190
        self.geometry.day = 14
        self.geometry.month = 7

        self.altitudes = Altitudes()
        self.altitudes.set_target_sea_level()
        self.altitudes.set_sensor_sea_level()

        self.wavelength = Wavelength(0.500)

        self.aot550 = 0.5
        self.visibility = None

        self.atmos_corr = AtmosCorr.NoAtmosCorr()

    def _find_path(self, path=None):
        """Finds the path of the 6S executable.

        Arguments:

        * ``path`` -- (Optional) The path to the 6S executable

        Finds the 6S executable on the system, either using the given path or by searching the system PATH variable and the current directory

        """
        if path is not None:
            return path
        else:
            return self._which('sixs.exe') or self._which('sixs') or self._which('sixsV1.1') or self._which('sixsV1.1.exe')

    def _which(self, program):
        def is_exe(fpath):
            return os.path.exists(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None

    def _create_geom_lines(self):
        """Creates the geometry lines for the input file"""
        return str(self.geometry)

    def _create_atmos_aero_lines(self):
        """Creates the atmosphere and aerosol lines for the input file"""
        return str(self.atmos_profile) + '\n' + str(self.aero_profile) + '\n'

    def _create_aot_vis_lines(self):
        """Create the AOT or Visibility lines for the input file"""
        if not isinstance(self.aero_profile, AeroProfile.UserProfile):
            # We don't need to set AOT or visibility for a UserProfile, but we do for all others
            if self.aot550 is not None:
                return "0\n%f value\n" % self.aot550
            elif self.visibility is not None:
                return "%f\n" % self.visibility
            else:
                raise ParameterError("aot550", "You must set either the AOT at 550nm or the Visibility in km.")
        else:
            return ""

    def _create_elevation_lines(self):
        """Create the elevation lines for the input file"""
        return str(self.altitudes)

    def _create_wavelength_lines(self):
        """Create the wavelength lines for the input file"""
        return self.wavelength

    def _create_ground_reflectance_lines(self):
        """Create the ground reflectance lines for the input file"""
        return self.ground_reflectance

    def _create_atmos_corr_lines(self):
        """Create the atmospheric correction lines for the input file"""
        return self.atmos_corr

    def _refls_to_string(self, arr):
        wavelengths = arr[:, 0]
        reflectances = arr[:, 1]

        # Remove the NaN's from the reflectances and wavelengths
        # so that they are interpolated if necessary
        wavelengths = wavelengths[~np.isnan(reflectances)]
        reflectances = reflectances[~np.isnan(reflectances)]

        # Create an array of the wavelengths that we want to get the reflectances at
        new_wavelengths = np.arange(self.min_wv, self.max_wv + 0.0025, 0.0025)

        # We then interpolate to get the right places
        calc_refl = interp1d(wavelengths, reflectances, bounds_error=False, fill_value=0.0)
        new_reflectances = calc_refl(new_wavelengths)

        s = " ".join(map(str, new_reflectances))

        return s

    def write_input_file(self, filename=None):
        """Generates a 6S input file from the parameters stored in the object
        and writes it to the given filename.

        The input file is guaranteed to be a valid 6S input file which can be run manually if required

        """

        input_file = self._create_geom_lines()

        input_file += self._create_atmos_aero_lines()

        input_file += self._create_aot_vis_lines()

        input_file += self._create_elevation_lines()

        # Unlike all of the other functions here, _create_wavelength_lines
        # returns 3 values:
        # * The string to go into the input file
        # * The minimum wavelength
        # * The maximum wavelength
        #
        # If only a single wavelength is given then that wavelength is
        # given in both min_wv and max_wv - that is, they are equal.
        input_file += self._create_wavelength_lines()[0]
        self.min_wv = self._create_wavelength_lines()[1]
        self.max_wv = self._create_wavelength_lines()[2]

        # Do replacements of the values within the surface specification
        #
        # Some surface specifications require the wavelength to be specified there
        # as well as in the wavelength part of the file (a clear violation of DRY, but
        # oh well). We deal with this by putting in the text WV_REPLACE, and then
        # replacing it with the min and max wavelengths.
        #
        ground_reflectance_lines = self._create_ground_reflectance_lines()

        if (isinstance(ground_reflectance_lines, basestring)):
            str_ground_refl = str(ground_reflectance_lines.replace("WV_REPLACE", "%f %f" % (self.min_wv, self.max_wv)))
        else:
            str_ground_refl = str(ground_reflectance_lines[0].replace("WV_REPLACE", "%f %f" % (self.min_wv, self.max_wv)))

        # Furthermore, to deal with spectra from spectral libraries
        # where the spectra are given as a 2D array of wavelength, reflectance
        # we need to interpolate to the right spacing
        # and replace the REFL_REPLACE bit of the string

        if "REFL_REPLACE_2" in str_ground_refl:
            new_str = self._refls_to_string(ground_reflectance_lines[2])
            str_ground_refl = str_ground_refl.replace("REFL_REPLACE_2", new_str)

        if "REFL_REPLACE" in str_ground_refl:
            new_str = self._refls_to_string(ground_reflectance_lines[1])
            str_ground_refl = str_ground_refl.replace("REFL_REPLACE", new_str)

        input_file += str_ground_refl

        input_file += self._create_atmos_corr_lines()


        if filename is None:
            # No filename given, so write to temporary file
            tmp_file = tempfile.NamedTemporaryFile(prefix="tmp_Py6S_input_", delete=False)

            # For Python 3, convert to Byte
            if sys.version_info[0] >= 3:
                tmp_file.file.write(bytes(input_file,'utf-8'))
            else:
                tmp_file.file.write(input_file)
            name = tmp_file.name
            tmp_file.close()
        else:
            f = open(filename, 'w')
            f.write(input_file)
            name = filename
            f.close()

        return name

    def run(self):
        """Runs the 6S model and stores the outputs in the output variable.

        May raise an :class:`.ExecutionError` if the 6S executable cannot be found."""

        if self.sixs_path is None:
            raise ExecutionError("6S executable not found.")

        # Create the input file as a temporary file
        tmp_file_name = self.write_input_file()

        # Run the process and get the stdout from it
        process = subprocess.Popen("%s < %s" % (self.sixs_path, tmp_file_name), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outputs = process.communicate()
        self.outputs = Outputs(outputs[0], outputs[1])

        # Remove the temporary file
        os.remove(tmp_file_name)

    def produce_debug_report(self):
        """Prints out information about the configuration of Py6S generally, and the current
        SixS object specifically, which will be useful when debugging problems."""
        import datetime
        import platform
        import sys

        print("Py6S Debugging Report")
        print("---------------------")
        print("Run on %s" % (str(datetime.datetime.now())))
        print("Platform: %s" % (platform.platform()))
        print("Python version: %s" % (sys.version.split('\n')[0]))
        print("Py6S version: %s" % (self.__version__))
        print("---------------------")
        self.test()
        print("---------------------")

        fname = self.write_input_file()
        with open(fname) as f:
            contents = f.readlines()

        print("".join(contents))

    @classmethod
    def test(cls, path=None):
        """Runs a simple test to ensure that 6S and Py6S are installed correctly."""
        test = cls(path)
        print("6S wrapper script by Robin Wilson")
        sixs_path = test._find_path()
        if sixs_path is None:
            print("Error: cannot find the sixs executable in $PATH or current directory.")
        else:
            print("Using 6S located at %s" % sixs_path)
            print("Running 6S using a set of test parameters")
            test.run()
            print("6sV version: %s" % (test.outputs.version))
            assert test.outputs.version == SIXSVERSION, "Unsupported 6sV version: {0}. Need version {1}".format(test.outputs.version, SIXSVERSION)
            print("The results are:")
            print("Expected result: %f" % 619.158)
            print("Actual result: %f" % test.outputs.diffuse_solar_irradiance)
            if np.abs((test.outputs.diffuse_solar_irradiance - 619.158) < 0.01):
                print("#### Results agree, Py6S is working correctly")
                return 0
            else:
                return 1
