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


class AtmosCorr:

    """Class representing options for selecting atmospheric correction settings for 6S."""

    @classmethod
    def NoAtmosCorr(cls):
        """Set 6S not to perform any atmospheric correction"""
        return """-1 No atm. corrections selected\n"""

    @classmethod
    def AtmosCorrLambertianFromRadiance(cls, radiance):
        """Set 6S to perform atmospheric correction assuming a Lambertian surface, using a given radiance value.

        Arguments:
        * ``radiance`` -- Radiance of the surface.

        """
        return """0 Atm. correction Lambertian
%f radiance
""" % radiance

    @classmethod
    def AtmosCorrLambertianFromReflectance(cls, reflectance):
        """Set 6S to perform atmospheric correction assuming a Lambertian surface, using a given reflectance value.

        Arguments:
        * ``reflectance`` -- Reflectance of the surface.

        """
        return """0 Atm. correction Lambertian
%f reflectance
""" % (reflectance * -1)

    @classmethod
    def AtmosCorrBRDFFromRadiance(cls, radiance):
        """Set 6S to perform atmospheric correction using a fully BRDF-represented surface, using a given radiance value.

        Arguments:
        * ``radiance`` -- Radiance of the surface

        """
        return """1 BRDF
%f radiance
""" % radiance

    @classmethod
    def AtmosCorrBRDFFromReflectance(cls, reflectance):
        """Set 6S to perform atmospheric correction using a fully BRDF-represented surface, using a given reflectance value.

        Arguments:
        * ``reflectance`` -- Reflectance of the surface.

        """
        return """1 BRDF
%f reflectance
""" % (reflectance * -1)
