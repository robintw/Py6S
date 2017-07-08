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

import pprint
import sys
from .sixs_exceptions import *


class Outputs(object):

    """Stores the output from a 6S run.

    Attributes:

     * ``fulltext`` -- The full output of the 6S executable. This can be written to a file with the write_output_file method.
     * ``values`` -- The main outputs from the 6S run, stored in a dictionary. Accessible either via standard dictionary notation (``s.outputs.values['pixel_radiance']``) or as attributes (``s.outputs.pixel_radiance``)

    Methods:

     * :meth:`.__init__` -- Constructor which takes the stdout and stderr from the model and processes it into the numerical outputs.
     * :meth:`.extract_results` -- Function called by the constructor to parse the output into individual variables
     * :meth:`.to_int` -- Convert a string to an int, so that it works even if passed a float.
     * :meth:`.write_output_file` -- Write the full textual output of the 6S model to a file.

    """
    # Stores the full textual output from 6S
    fulltext = ""

    # Stores the numerical values extracted from the textual output as a dictionary

    def __init__(self, stdout, stderr):
        """Initialise the class with the stdout output from the model, and process
        it into the numerical outputs.

        Arguments:
         * ``stdout`` -- Standard output from the model run
         * ``stderr`` -- Standard error from the model run

        Will raise an :class:`.OutputParsingError` if the output cannot be parsed for any reason.

        """

        self.values = {}
        self.trans = {}
        self.rat = {}

        if len(stderr) > 0:
            # Something on standard error - so there's been an error
            print(stderr)
            raise OutputParsingError("6S returned an error (shown above) - check for invalid parameter inputs")


        self.fulltext = stdout

        # For Python 3 need to decode to string
        if sys.version_info[0] >= 3:
            self.fulltext = self.fulltext.decode()

        self.extract_results()

    def __getattr__(self, name):
        """Executed when an attribute is referenced and not found. This method is overridden
        to allow the user to access the outputs as ``outputs.variable`` rather than using the dictionary
        explicity"""

        # If there is a key with this name in the standard variables field then use it
        if name in self.values:
            return self.values[name]
        else:
            # If not, then split it by .'s
            items = name.split("_")
            if items[0] == "transmittance":
                return self.trans["_".join(items[1:])]
            else:
                if name in self.rat:
                    return self.rat[name]
                else:
                    raise OutputParsingError("The specifed output variable does not exist.")

    def __dir__(self):
        # Returns list of the attributes that I want to tab-complete on that aren't actually attributes, for IPython
        trans_keys = ["transmittance_" + key for key in self.trans.keys()]
        rat_keys = self.rat.keys()

        all_keys = list(self.values.keys()) + list(trans_keys) + list(rat_keys)
        return sorted(all_keys)

    def extract_results(self):
        """Extract the results from the text output of the model and place them in the ``values`` dictionary."""

        # Remove all of the *'s from the text as they just make it look pretty
        # and get in the way of analysing the output
        fulltext = self.fulltext.replace("*", "")

        # Split into lines
        lines = fulltext.splitlines()

        CURRENT = 0
        WHOLE_LINE = (0, 30)

        # The dictionary below specifies how to extract each variable from the text output
        # of 6S.
        # The dictionary key is the text to search for. When this is found, the line corresponding
        # to the first value in the tuple is found. If this is CURRENT (ie. 0) then it is the line on which
        # the text was found, if it is 1 then it is the next line, 2 the one after that etc.
        # The next item in the tuple is the index of the split line to extract the value from, and the
        # third item is the key to store it in in the values dictionary. The final item is the type to convert
        # it to - the type conversion function must be specified. More specific functions such as math.floor can
        # be used here if desired.

        #              Search Term                                Line   Index DictKey   Type
        extractors = {"6SV version": (CURRENT, 2, "version", str),
                      "month": (CURRENT, 1, "month", self.to_int),
                      "day": (CURRENT, 4, "day", self.to_int),
                      "solar zenith angle": (CURRENT, 3, "solar_z", self.to_int),
                      "solar azimuthal angle": (CURRENT, 8, "solar_a", self.to_int),
                      "view zenith angle": (CURRENT, 3, "view_z", self.to_int),
                      "view azimuthal angle": (CURRENT, 8, "view_a", self.to_int),
                      "scattering angle": (CURRENT, 2, "scattering_angle", float),
                      "azimuthal angle difference": (CURRENT, 7, "azimuthal_angle_difference", float),
                      "optical condition identity": (1, WHOLE_LINE, "visibility", self.extract_vis),
                      "optical condition": (1, WHOLE_LINE, "aot550", self.extract_aot),
                      "ground pressure": (CURRENT, 3, "ground_pressure", float),
                      "ground altitude": (CURRENT, 3, "ground_altitude", float),

                      "appar. rad.(w/m2/sr/mic)": (CURRENT, 2, "apparent_reflectance", float),
                      "appar. rad.": (CURRENT, 5, "apparent_radiance", float),
                      "total gaseous transmittance": (CURRENT, 3, "total_gaseous_transmittance", float),

                      "wv above aerosol": (CURRENT, 4, "wv_above_aerosol", float),
                      "wv mixed with aerosol": (CURRENT, 10, "wv_mixed_with_aerosol", float),
                      "wv under aerosol": (CURRENT, 4, "wv_under_aerosol", float),

                      "% of irradiance": (2, 0, "percent_direct_solar_irradiance", float),
                      "% of irradiance at": (2, 1, "percent_diffuse_solar_irradiance", float),
                      "% of irradiance at ground level": (2, 2, "percent_environmental_irradiance", float),
                      "reflectance at satellite level": (2, 0, "atmospheric_intrinsic_reflectance", float),
                      "reflectance at satellite lev": (2, 1, "background_reflectance", float),
                      "reflectance at satellite l": (2, 2, "pixel_reflectance", float),
                      "irr. at ground level": (2, 0, "direct_solar_irradiance", float),
                      "irr. at ground level (w/": (2, 1, "diffuse_solar_irradiance", float),
                      "irr. at ground level (w/m2/mic)": (2, 2, "environmental_irradiance", float),
                      "rad at satel. level": (2, 0, "atmospheric_intrinsic_radiance", float),
                      "rad at satel. level (w/m2/": (2, 1, "background_radiance", float),
                      "rad at satel. level (w/m2/sr/mic)": (2, 2, "pixel_radiance", float),
                      "sol. spect (in w/m2/mic)": (1, 0, "solar_spectrum", float),


                      "measured radiance [w/m2/sr/mic]": (CURRENT, 4, "measured_radiance", float),
                      "atmospherically corrected reflectance": (1, 3, "atmos_corrected_reflectance_lambertian", float),
                      "atmospherically corrected reflect": (2, 3, "atmos_corrected_reflectance_brdf", float),
                      "coefficients xa": (CURRENT, 5, "coef_xa", float),
                      "coefficients xa xb": (CURRENT, 6, "coef_xb", float),
                      "coefficients xa xb xc": (CURRENT, 7, "coef_xc", float),
                      "int. funct filter (in mic)": (1, 0, 'int_funct_filt', float),
                      "int. sol. spect (in w/m2)": (1, 1, 'int_solar_spectrum', float)
                      }
        # Process most variables in the output
        for index in range(len(lines)):
            current_line = lines[index]
            for label, details in extractors.items():
                    # If the label we're searching for is in the current line
                if label.lower() in current_line.lower():
                    # See if the data is in the current line (as specified above)
                    if details[0] == CURRENT:
                        extracting_line = current_line
                    # Otherwise, work out which line to use and get it
                    else:
                        extracting_line = lines[index + details[0]]

                    funct = details[3]
                    items = extracting_line.split()

                    try:
                        a = details[1][0]
                        b = details[1][1]
                    except:
                        a = details[1]
                        b = details[1] + 1

                    data_for_func = items[a:b]

                    if len(data_for_func) == 1:
                        data_for_func = data_for_func[0]

                    try:
                        self.values[details[2]] = funct(data_for_func)
                    except:
                        self.values[details[2]] = float('nan')

        # Process big grid in the middle of the output for transmittances
        grid_extractors = {'global gas. trans. :': "global_gas",
                           'water   "     "    :': "water",
                           'ozone   "     "    :': "ozone",
                           'co2     "     "    :': "co2",
                           'oxyg    "     "    :': "oxygen",
                           'no2     "     "    :': "no2",
                           'ch4     "     "    :': "ch4",
                           'co      "     "    :': "co",
                           'rayl.  sca. trans. :': "rayleigh_scattering",
                           'aeros. sca.   "    :': "aerosol_scattering",
                           'total  sca.   "    :': "total_scattering"}

        for index in range(len(lines)):
            current_line = lines[index]
            for search, name in grid_extractors.items():
                # If the label we're searching for is in the current line
                if search in current_line:
                    items = current_line.split()
                    values = Transmittance()

                    try:
                        values.downward = float(items[4])
                    except:
                        values.downward = float('nan')

                    try:
                        values.upward = float(items[5])
                    except:
                        values.upward = float('nan')

                    try:
                        values.total = float(items[6])
                    except:
                        values.total = float('nan')

                    self.trans[name] = values

        # Process big grid in the middle of the output for transmittances
        bottom_grid_extractors = {'spherical albedo   :': "spherical_albedo",
                                  'optical depth total:': "optical_depth_total",
                                  'optical depth plane:': "optical_depth_plane",
                                  'reflectance I      :': "reflectance_I",
                                  'reflectance Q      :': "reflectance_Q",
                                  'reflectance U      :': "reflectance_U",
                                  'polarized reflect. :': "polarized_reflectance",
                                  #'degree of polar.   :' : "degree_of_polarization",
                                  'dir. plane polar.  :': "direction_of_plane_polarization",
                                  'phase function I   :': "phase_function_I",
                                  'phase function Q   :': "phase_function_Q",
                                  'phase function U   :': "phase_function_U",
                                  'primary deg. of pol:': "primary_degree_of_polarization",
                                  'sing. scat. albedo :': "single_scattering_albedo"
                                  }

        for index in range(len(lines)):
            current_line = lines[index]
            for search, name in bottom_grid_extractors.items():
                # If the label we're searching for is in the current line
                if search in current_line:
                    items = current_line.rsplit(None, 3)

                    values = RayleighAerosolTotal()

                    try:
                        values.total = float(items[3])
                    except:
                        values.total = float('nan')

                    try:
                        values.aerosol = float(items[2])
                    except:
                        values.aerosol = float('nan')

                    try:
                        values.rayleigh = float(items[1])
                    except:
                        values.rayleigh = float('nan')

                    self.rat[name] = values

    def to_int(self, str):
        """Converts a string to an integer.

        Does this by converting to float and then converting that to int, meaning that
        converting "5.00" to an integer will actually work.

        Arguments:
         * ``str`` -- The string containing the number to convert to an integer

        """
        return int(float(str))

    def extract_vis(self, data):
        """Extracts the visibility from the visibility and AOT line in the output"""
        s = " ".join(data)
        spl = s.split(":")
        spl2 = spl[1].split()

        try:
            value = float(spl2[0])
        except:
            value = float("Inf")

        return value

    def extract_aot(self, data):
        """Extracts the AOT from the visibility and AOT line in the output."""
        s = " ".join(data)
        spl = s.split(":")

        return float(spl[2])

    def write_output_file(self, filename):
        """Writes the full textual output of the 6S model run to the specified filename.

        Arguments:
         * ``filename`` -- The filename to write the output to

        """
        with open(filename, 'w') as f:
            f.write(self.fulltext)


class Transmittance(object):

    """Stores transmittance values from the 6S output.

    Basically a simple class storing three attributes:
    * ``downward`` -- Transmittance downwards
    * ``upward`` -- Transmittance upwards
    * ``total`` -- Total transmittance

    """
    downward = float('nan')
    upward = float('nan')
    total = float('nan')

    def __str__(self):
        return "Downward: %f, Upward: %f, Total: %f" % (self.downward, self.upward, self.total)


class RayleighAerosolTotal(object):

    rayleigh = float('nan')
    aerosol = float('nan')
    total = float('nan')

    def __str__(self):
        return "Rayleigh: %f, Aerosol: %f, Total: %f" % (self.rayleigh, self.aerosol, self.total)
