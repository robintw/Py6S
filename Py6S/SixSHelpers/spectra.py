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

import sys
import numpy as np

# Python 2/3 imports
try:
    import urllib2
except ImportError:
    if sys.version_info[0] >= 3:
        import urllib.request as urllib2
    else:
        raise

try:
    from StringIO import StringIO
except ImportError:
    if sys.version_info[0] >= 3:
        from io import StringIO
    else:
        raise



class Spectra:

    """Class allowing the import of spectral libraries from various sources"""

    @classmethod
    def import_from_usgs(cls, loc):
        """Imports a spectral library from the USGS Spectral Library (available at http://speclab.cr.usgs.gov/spectral.lib06/).

        Arguments:

          * ``loc`` -- Location of the data to import. Can either be a URL (eg. http://speclab.cr.usgs.gov/spectral.lib06/ds231/ASCII/V/russianolive.dw92-4.30728.asc) or a file path.

        Returns:

        An ``ndarray`` with two columns: wavelength (um) and reflectance (fraction)

        Example usage::

           from Py6S import *
           s = SixS()
           s.wavelength = Wavelength(0.500)
           s.ground_reflectance = GroundReflectance.HomogeneousLambertian(Spectra.import_from_usgs("http://speclab.cr.usgs.gov/spectral.lib06/ds231/ASCII/V/russianolive.dw92-4.30728.asc"))
           s.run()
           # Bear in mind this will produce a result for a single Wavelength
           # To see what the whole spectrum will look like after atmospheric
           # radiative transfer has taken place you must run for multiple wavelengths
           # For example
           wavelengths, reflectances = SixSHelpers.Wavelengths.run_vnir(s, output_name="apparent_radiance")


        """
        if loc.startswith("""http://"""):
            data = urllib2.urlopen(loc).read()
            if sys.version_info[0] >= 3:
                f = StringIO(data.decode())
            else:
                f = StringIO(data)
        else:
            f = open(loc, "r")

        npdata = np.loadtxt(f, skiprows=16)
        f.close()
        npdata[npdata == -1.23e+34] = np.nan
        npdata = npdata[:, 0:2]

        return npdata

    @classmethod
    def import_from_aster(cls, loc):
        """Imports a spectral library from the ASTER Spectral Library (http://speclib.jpl.nasa.gov/)

        Arguments:

          * ``loc`` -- Location of the data to import. Can either be a URL (eg. http://speclib.jpl.nasa.gov/speclibdata/jhu.becknic.vegetation.trees.conifers.solid.conifer.spectrum.txt) or a file path.

        Returns:

        An ``ndarray`` with two columns: wavelength (um) and reflectance (fraction)

        Example usage::

           from Py6S import *
           s = SixS()
           s.ground_reflectance = GroundReflectance.HomogeneousLambertian(Spectra.import_from_aster("http://speclib.jpl.nasa.gov/speclibdata/jhu.becknic.vegetation.trees.conifers.solid.conifer.spectrum.txt"))
           s.run()
           # Bear in mind this will produce a result for a single Wavelength
           # To see what the whole spectrum will look like after atmospheric
           # radiative transfer has taken place you must run for multiple wavelengths
           # For example
           wavelengths, reflectances = SixSHelpers.Wavelengths.run_vnir(s, output_name="apparent_radiance")

        """
        if loc.startswith("""http://"""):
            data = urllib2.urlopen(loc).read()
            if sys.version_info[0] >= 3:
                f = StringIO(data.decode())
            else:
                f = StringIO(data)
        else:
            f = open(loc, "r")

        npdata = np.loadtxt(f, skiprows=26)
        f.close()
        npdata[:, 1] = npdata[:, 1] / 100
        return npdata
