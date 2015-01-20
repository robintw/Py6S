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

from collections import defaultdict
#from sixs_exceptions import *
from Py6S.sixs_exceptions import ParameterError
import sys

class AeroProfile:

    """Class representing options for Aerosol Profiles"""

    NoAerosols = 0
    Continental = 1
    Maritime = 2
    Urban = 3
    Desert = 5
    BiomassBurning = 6
    Stratospheric = 7

    @classmethod
    def PredefinedType(cls, type):
        """Set 6S to use a predefined aerosol type, one of the constants defined in this class.

        Arguments:

        * ``type`` -- the predefined aerosol type, one of the constants defined in this class

        Example usage::

          s.aeroprofile = AeroProfile.PredefinedType(AeroProfile.Urban)

        """
        return "%d" % type

    @classmethod
    def User(cls, **kwargs):
        """Set 6S to use a user-defined aerosol profile based on proportions of standard aerosol components.

        The profile is set as a mixture of pre-defined components, each given as an optional keyword.
        Not all keywords need to be given, but the values for the keywords given must sum to 1, or a
        ParameterError will be raised.

        Optional keywords:

        * ``dust`` -- The proportion of dust-like aerosols
        * ``water`` -- The proportion of water-like aerosols
        * ``oceanic`` -- The proportion of oceanic aerosols
        * ``soot`` -- The proportion of soot-like aerosols

        Example usage::

          s.aeroprofile = AeroProfile.User(dust=0.3, oceanic=0.7)
          s.aeroprofile = AeroProfile.User(soot = 0.1, water = 0.3, oceanic = 0.05, dust = 0.55)

        """
        d = defaultdict(lambda: 0, kwargs)

        dust = d['dust']
        water = d['water']
        oceanic = d['oceanic']
        soot = d['soot']

        if (((dust + water + oceanic + soot) - 1) > 0.01):
            raise ParameterError("Aerosol Profile", "User aerosol components don't sum to 1.0")

        return "4 (User's Components)\n%f, %f, %f, %f" % (dust, water, oceanic, soot)

    @classmethod
    def MultimodalLogNormalDistribution(cls, rmin, rmax):
        """Set 6S to use a Multimodal Log-Normal distribution.

        Arguments:

        * ``rmin`` -- The minimum aerosol radius
        * ``rmax`` -- The maximum aerosol radius

        This returns an :class:`.AerosolDistribution` object. Components can then be added to this distribution using the :meth:`.add_component`
        method of the returned class.

        Example usage::

          s.aeroprofile = AeroProfile.MultimodalLogNormalDistribution(0.3, 0.1)
          s.aeroprofile.add_component(...)

        """
        return cls.AerosolDistribution(rmin, rmax, 8)

    @classmethod
    def ModifiedGammaDistribution(cls, rmin, rmax):
        """Set 6S to use a Modified Gamma distribution.

        Arguments:

        * ``rmin`` -- The minimum aerosol radius
        * ``rmax`` -- The maximum aerosol radius

        This returns an :class:`.AerosolDistribution` object. Components can then be added to this distribution using the :meth:`.add_component`
        method of the returned class.

        Example usage::

          s.aeroprofile = AeroProfile.ModifiedGammaDistribution(0.3, 0.1)
          s.aeroprofile.add_component(...)

        """
        return cls.AerosolDistribution(rmin, rmax, 9)

    @classmethod
    def JungePowerLawDistribution(cls, rmin, rmax):
        """Set 6S to use a Junge Power Law distribution.

        Arguments:

        * ``rmin`` -- The minimum aerosol radius
        * ``rmax`` -- The maximum aerosol radius

        This returns an :class:`.AerosolDistribution` object. Components can then be added to this distribution using the :meth:`.add_component`
        method of the returned class.

        Example usage::

          s.aeroprofile = AeroProfile.JungePowerLawDistribution(0.1, 0.3)
          s.aeroprofile.add_component(...)

        """
        return cls.AerosolDistribution(rmin, rmax, 10)

    @classmethod
    def SunPhotometerDistribution(cls, r, dvdlogr, refr_real, refr_imag):
        """Set 6S to use an aerosol parameterisation from Sun Photometer measurements.

        The real and imaginary parts of the refractive indices must be input at the following wavelengths
        (given in micrometers):
        0.350, 0.400, 0.412, 0.443, 0.470, 0.488, 0.515, 0.550, 0.590, 0.633, 0.670, 0.694, 0.760,
        0.860, 1.240, 1.536, 1.650, 1.950, 2.250, 3.750

        Arguments:

        * ``r`` -- A list of radius measurements from a sun photometer (microns)
        * ``dvdlogr`` -- A list of dV/d(logr) measurements from a sun photometer, for the radiuses as above (cm^3/cm^2/micron)
        * ``refr_real`` -- A list containing the real part of the refractive indices for each of the 20 wavelengths (above). If a single
          float value is given then the value is treated as constant for all wavelengths.
        * ``refr_imag`` -- A list containing the imaginary part of the refractive indices for each of the 20 wavelengths (above). If a single
          float value is given then the value is treated as constant for all wavelengths.

        """
        header = "11 (Sun Photometric Distribution)\n"

        # Check lengths of r and dvdlorg are the same
        if len(r) != len(dvdlogr):
            raise ParameterError("R and dV/d(log r)", "These must be the same length")

        num = "%d\n" % len(r)

        ds = ""
        comp = ""

        for i in range(len(r)):
            ds += "%f %f\n" % (r[i], dvdlogr[i])

        try:
            if type(refr_real) is float:
                refr_real = [refr_real] * 20
            elif len(refr_real) != 20:
                raise ParameterError("Aerosol Distribution Real Refractive Index", "You must specify the real part of the Refractive Index at 20 wavelengths.")
        except TypeError:
            raise ParameterError("Aerosol Distribution Imaginary Refractive Index", "You must specify the imaginary part of the Refractive Index at 20 wavelengths.")

        try:
            if type(refr_imag) is float:
                refr_imag = [refr_imag] * 20
            elif len(refr_imag) != 20:
                raise ParameterError("Aerosol Distribution Imaginary Refractive Index", "You must specify the imaginary part of the Refractive Index at 20 wavelengths.")
        except TypeError:
            raise ParameterError("Aerosol Distribution Imaginary Refractive Index", "You must specify the imaginary part of the Refractive Index at 20 wavelengths.")

        real = map(str, refr_real)
        imag = map(str, refr_imag)

        if sys.version_info[0] >= 3:
            real = list(real)
            imag = list(imag)

        comp += ' '.join(real) + '\n'
        comp += ' '.join(imag) + '\n'

        return header + num + ds + comp + "0 no results saved"

    class AerosolDistribution:

        """Stores data regarding a specific Aerosol Distribution.

        Used by the following methods:

        * :meth:`.MultimodalLogNormalDistribution`
        * :meth:`.ModifiedGammaDistribution`
        * :meth:`.JungePowerLawDistribution`

        """
        numtype = 0
        rmin = 0
        rmax = 0
        values = []

        def __init__(self, rmin, rmax, numtype):
            """Initialise an Aerosol Distribution with various parameters.

            Should not be called directly - use one of the methods like AeroProfile.MultimodalLogNormalDistribution() instead.

            Arguments:

            * ``rmin`` -- The minimum aerosol radius
            * ``rmax`` -- The maximum aerosol radius
            * ``numtype`` -- The type of aerosol distribution (eg. 8 for Multimodal Log Normal)

            """
            self.rmin = rmin
            self.rmax = rmax
            self.numtype = numtype

        def add_component(self, rmean, sigma, percentage_density, refr_real, refr_imag):
            """Adds a component to the aerosol distribution.

            Wavelength dependent values must be input at the following wavelengths (given in micrometers):
            0.350, 0.400, 0.412, 0.443, 0.470, 0.488, 0.515, 0.550, 0.590, 0.633, 0.670, 0.694, 0.760,
            0.860, 1.240, 1.536, 1.650, 1.950, 2.250, 3.750


            Arguments:

            * ``rmean`` -- The mean radius of the aerosols
            * ``sigma`` -- Sigma, as defined by the distribution (Log Normal etc)
            * ``percentage_density`` -- The percentage density of the aerosol
            * ``refr_real`` -- A 20-element iterable giving the real part of the refractive indices at the specified wavelengths (see above)
            * ``refr_imag`` -- A 20-element iterable giving the imaginary part of the refractive indices at the specified wavelengths (see above)

            """
            if len(self.values) >= 4:
                raise ParameterError("Aerosol Distribution components", "You can only add a maximum of 4 components")

            if len(refr_real) != 20:
                raise ParameterError("Aerosol Distribution Real Refractive Index", "You must specify the real part of the Refractive Index at 20 wavelengths.")

            if len(refr_imag) != 20:
                raise ParameterError("Aerosol Distribution Imaginary Refractive Index", "You must specify the imaginary part of the Refractive Index at 20 wavelengths.")

            comp = "%f %f %f\n" % (rmean, sigma, percentage_density)
            real = map(str, refr_real)
            imag = map(str, refr_imag)

            if sys.version_info[0] >= 3:
                real = list(real)
                imag = list(imag)

            comp += ' '.join(real) + '\n'
            comp += ' '.join(imag) + '\n'

            self.values.append(comp)

        def __str__(self):
            result = "%d\n%f %f %d\n" % (self.numtype, self.rmin, self.rmax, len(self.values))
            components = ''.join(self.values)
            return result + components + "0 no results saved"

    class UserProfile:

        """Set 6S to use a user-defined aerosol profile, with differing AOTs over the height of the profile.

        Arguments:

        * ``atype`` --  Aerosol type to be used for all layers. Must be one of the pre-defined types defined in this class.

        Methods:

        * :meth:`.add_layer` -- Adds a layer to the user-defined aerosol profile, with the specified height and aerosol optical thickness.

        Example usage::

          s.aeroprofile = AeroProfile.UserProfile(AeroProfile.Maritime)
          s.aeroprofile.add_layer(5, 0.34) # Add a 5km-thick layer with an AOT of 0.34
          s.aeroprofile.add_layer(10, 0.7) # Add a 10km-thick layer with an AOT of 0.7
          s.aeroprofile.add_layer(100, 0.01) # Add a 100km-thick layer with an AOT of 0.01

        """
        values = []
        aerotype = 0

        def __init__(self, atype):
            """Initialises the user-defined aerosol profile to a specific aerosol type.

            Arguments:

            * ``atype`` --  Aerosol type to be used for all layers. Must be one of the pre-defined types defined in this class.

            """
            self.aerotype = atype

        def add_layer(self, height, optical_thickness):
            """Adds a layer to the user-defined profile.

            Arguments:

            * ``height`` -- Height of the layer (in km)
            * ``optical_thickness`` -- Optical thickness of the layer

            Example usage::

              s.aeroprofile.add_layer(5, 0.34) # Add a 5km-thick layer with an AOT of 0.34
            """
            self.values.append((height, optical_thickness))

        def __str__(self):
            res = "-1 Aerosol model (type) and profile\n%d\n" % len(self.values)
            for val in self.values:
                res += "%f %f %d\n" % (val[0], val[1], self.aerotype)

            return res
