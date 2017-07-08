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

#from sixs_exceptions import *
import sys
import collections
import numpy as np
try:
    import StringIO
except ImportError:
    # If Python 3 import io as StringIO (so we can still use StringIO.StringIO)
    if sys.version_info[0] >= 3:
        import io as StringIO
    else:
        raise


class GroundReflectance:

    """Produces strings for the input file for a number of different ground reflectance scenarios.

    Options are:

    - Homogeneous

      - Lambertian
      - BRDF

          - Walthall et al. model
          - Rahman et al. model
          - etc

    - Heterogeneous

      - Lambertian

    These are combined to give function names like:

    :meth:`.HomogeneousLambertian` or :meth:`.HomogeneousWalthall`

    The standard functions (:meth:`.HomogeneousLambertian` and :meth:`.HeterogeneousLambertian`) will decide what to do based on the types of inputs they are given::

      model.ground_reflectance = GroundReflectance.HomogeneousLambertian(0.7) # A spectrally-constant reflectance of 0.7
      model.ground_reflectance = GroundReflectance.HomogeneousLambertian(GroundReflectance.GreenVegetation) # A built-in green vegetation spectrum
      model.ground_reflectance = GroundReflectance.HomogeneousLambertian([0.6, 0.8, 0.34, 0.453]) # A user-defined spectrum given in micrometers with steps of 2.5nm
      # A 2D ndarray, such as that returned by any of the Spectra.import_* functions
      model.ground_reflectance = GroundReflectance.HomogeneousLambertian(Spectra.import_from_usgs("http://speclab.cr.usgs.gov/spectral.lib06/ds231/ASCII/V/russianolive.dw92-4.30728.asc"))
    """

    GreenVegetation = -1
    ClearWater = -2
    Sand = -3
    LakeWater = -4

    @classmethod
    def HomogeneousLambertian(cls, ro):
        """Provides parameterisation for homogeneous Lambertian (ie. uniform BRDF) surfaces.

        The single argument can be either:

        - A single float value (for example, 0.634), in which case it is interpreted as a spectrally-constant reflectance value.
        - A constant defined by this class (one of ``GroundReflectance.GreenVegetation``, ``GroundReflectance.ClearWater``, ``GroundReflectance.Sand`` or ``GroundReflectance.LakeWater``) in which case a built-in spectrum of the specified material is used.
        - An array of values (for example, [0.67, 0.85, 0.34, 0.65]) in which case the values are taken to be reflectances across the whole wavelength range at a spacing of 2.5nm. In this case, if the start wavelength is s and the end wavelength is e, the values must be given for the wavelengths: ``s, s+2.5, s+5.0, s+7.5, ..., e-2.5, e``
        - A multidimensional ndarray giving wavelength (column 0) and reflectance (column 1) values

        """
        ro_type, ro_value = cls._GetTargetTypeAndValues(ro)

        if ro_value == "":
            res = """0 Homogeneous surface
0 No directional effects
%s\n""" % (ro_type)
        elif ro_type == "-1":
            res = """0 Homogeneous surface
0 No directional effects
%s
WV_REPLACE
%s\n""" % (ro_type, ro_value)
        else:
            res = """0 Homogeneous surface
0 No directional effects
%s
%s\n""" % (ro_type, ro_value)

        return [res, ro]

    @classmethod
    def HeterogeneousLambertian(cls, radius, ro_target, ro_env):
        """Provides parameterisation for heterogeneous Lambertian (ie. uniform BRDF) surfaces.

        These surfaces are modelled in 6S as a circular target surrounded by an environment of a different reflectance.

        Arguments:

        * ``radius`` -- The radius of the target (in km)
        * ``ro_target`` -- The reflectance of the target
        * ``ro_env`` -- The reflectance of the environment

        Both of the reflectances can be set to any of the following:

        - A single float value (for example, 0.634), in which case it is interpreted as a spectrally-constant reflectance value.
        - A constant defined by this class (one of ``GroundReflectance.GreenVegetation``, ``GroundReflectance.ClearWater``, ``GroundReflectance.Sand`` or ``GroundReflectance.LakeWater``) in which case a built-in spectrum of the specified material is used.
        - An array of values (for example, [0.67, 0.85, 0.34, 0.65]) in which case the values are taken to be reflectances across the whole wavelength range at a spacing of 2.5nm. In this case, if the start wavelength is s and the end wavelength is e, the values must be given for the wavelengths: ``s, s+2.5, s+5.0, s+7.5, ..., e-2.5, e``
        - A multidimensional ndarray giving wavelength (column 0) and reflectance (column 1) values
        """
        ro_target_type, ro_target_values = cls._GetTargetTypeAndValues(ro_target)
        ro_env_type, ro_env_values = cls._GetTargetTypeAndValues(ro_env, "REFL_REPLACE_2")

        if ro_target_values == "" and ro_env_values == "":
            s =  """1 (Non homogeneous surface)
%s %s %f (ro1 ro2 radius)\n""" % (ro_target_type, ro_env_type, radius)
        else:
            s =  """1 (Non homogeneous surface)
%s %s %f (ro1 ro2 radius)
%s
%s\n""" % (ro_target_type, ro_env_type, radius, ro_target_values, ro_env_values)

        return [s, ro_target, ro_env]

    @classmethod
    def HomogeneousWalthall(cls, param1, param2, param3, albedo):
        """Parameterisation for a surface BRDF based on the Walthall et al. model.

        The parameters are:

        - term in square ts*tv
        - term in square ts*ts+tv*tv
        - term in ts*tv*cos(phi) (limacon de pascal)
        - albedo

        """
        return """0 Homogeneous surface
1 (directional effects)
4 (Walthall et al. model)
%f %f %f %f\n""" % (param1, param2, param3, albedo)

    @classmethod
    def HomogeneousHapke(cls, albedo, assymetry, amplitude, width):
        """Parameterisation for a surface BRDF based on the Hapke model.

        The parameters are:

        - albedo
        - assymetry parameter for the phase function
        - amplitude of hot spot
        - width of the hot spot

         """
        return """0 Homogeneous surface
1 (directional effects)
1 (Hapke model)
%f %f %f %f\n""" % (albedo, assymetry, amplitude, width)

    @classmethod
    def HomogeneousRoujean(cls, albedo, k1, k2):
        """Parameterisation for a surface BRDF based on the Roujean et al. model.

        The parameters are:

        - albedo
        - geometric parameter for hot spot effect
        - geometric parameter for hot spot effect

         """
        return """0 Homogeneous surface
1 (directional effects)
3 (Roujean model)
%f %f %f\n""" % (albedo, k1, k2)

    @classmethod
    def HomogeneousMinnaert(cls, k, alb):
        """Parameterisation for a surface BRDF based on the Minnaert BRDF model.

        The parameters are:
        - K surface parameter
        - Surface albedo

        """
        return """0 Homogeneous surface
1 (directional effects)
5 (Minnaert model)
%f %f\n""" % (k, alb)

    @classmethod
    def HomogeneousMODISBRDF(cls, par1, par2, par3):
        """Parameterisation for a surface BRDF based on the MODIS Operational BRDF model.

        The parameters are:

        - Weight for lambertian kernel
        - Weight for Ross Thick kernel
        - Weight for Li Spare kernel

        """
        return """0 Homogeneous surface
1 (directional effects)
10 (MODIS BRDF model)
%f %f %f\n""" % (par1, par2, par3)

    @classmethod
    def HomogeneousOcean(cls, wind_speed, wind_azimuth, salinity, pigment_concentration):
        """Parameterisation for a surface BRDF based on the Ocean BRDF model.

        The parameters are:

        - wind speed (in m/s)
        - azimuth of the wind (in degrees)
        - salinity (in ppt) (set to 34.3ppt if < 0)
        - pigment concentration (in mg/m3)

        """
        return """0 Homogeneous surface
1 (directional effects)
6 (Ocean BRDF)
%f %f %f %f\n""" % (wind_speed, wind_azimuth, salinity, pigment_concentration)

    @classmethod
    def HomogeneousRahman(cls, intensity, asymmetry_factor, structural_parameter):
        """Parameterisation for a surface BRDF based on the Rahman BRDF model.

        The parameters are:

        - Intensity of the reflectance of the surface (N/D value >= 0)
        - Asymmetry factor, N/D value between -1.0 and 1.0
        - Structural parameter of the medium

        """
        return """0 Homogeneous surface
1 (directional effects)
8 (Rahman model)
%f %f %f\n""" % (intensity, asymmetry_factor, structural_parameter)

    @classmethod
    def HomogeneousIaquintaPinty(cls, leaf_dist, hot_spot, lai, hot_spot_param, leaf_reflec, leaf_trans, soil_albedo):
        """Parameterisation for a surface BRDF based on the Iaquinta and Pinty model.

        The parameters are:

        - Leaf distribution (one of the ``GroundReflectance.LeafDistXXX`` constants)
        - Hot spot setting (``GroundReflectance.HotSpot`` or ``GroundReflectance.NoHotSpot``)
        - Leaf Area Index (1-15)
        - Hot spot parameter 2*r*lambda (0-2)
        - Leaf reflectance (0-0.99)
        - Leaf transmittance (0-0.99)
        - Soil albedo (0-0.99)

        Leaf reflectance + Leaf transmittance must be less than 0.99. If this is not the case, a :class:`.ParameterException` is raised.

        """
        if leaf_reflec + leaf_trans > 0.99:
            raise ParameterException("leaf_reflec", "Leaf reflectance + Leaf transmittance must be < 0.99")

        return """0 Homogeneous surface
1 (directional effects)
7 (Iaquinta and Pinty model)
%d %d
%d %d
%d %d %d\n""" % (leaf_dist, hot_spot, lai, hot_spot_param, leaf_reflec, leaf_trans, soil_albedo)

    LeafDistPlanophile = 1
    LeafDistErectophile = 2
    LeafDistPlagiophile = 3
    LeafDistExtremophile = 4
    LeafDistUniform = 5

    NoHotSpot = 1
    HotSpot = 2

    @classmethod
    def HomogeneousVerstaeteEtAl(cls, kappa_param, phase_funct, scattering_type, leaf_area_density, sun_flecks_radius, ssa, legendre_first, legendre_second, k1, k2, asym_factor, chil):
        """Parameterisation for a surface BRDF based on the Verstraete, Pinty and Dickinson model.

        The parameters are:

        - The type of Kappa parameterisation (one of the ``GroundReflectance.KappaXXX`` constants)
        - The phase function to use (one of the ``GroundReflectance.PhaseXXX`` constants)
        - The scattering type to use (either ``GroundReflectance.SingleScatteringOnly`` or ``GroundReflectance.DickinsonMultipleScattering``)
        - Leaf area density (m^2/m^-3)
        - Radius of the sun flecks on the scatterer (m)
        - Single Scattering Albedo (0-1)
        - First coefficient of Legendre polynomial (Only used if phase function is not ``GroundReflectance.PhaseIsotropic``, set to ``None`` otherwise)
        - Second coefficient of Legendre polynomial (Only used if phase function is not ``GroundReflectance.PhaseIsotropic``, set to ``None`` otherwise)
        - Kappa value k1 (Only used if Kappa parameterisation was ``GroundReflectance.KappaGivenValues``, set to ``None`` otherwise)
        - Kappa value k2 (Only used if Kappa parameterisation was ``GroundReflectance.KappaGivenValues``, set to ``None`` otherwise)
        - Asymmetry factor for Heyney-Greenstein parameterisation (Only used if Phase function is set to ``GroundReflectance.PhaseHeyneyGreenstein``, set to ``None`` otherwise)
        - Goudriaan's chil parameter (Only used if Kappa parameterisation was NOT ``GroundReflectance.KappaGivenValues``, set to ``None`` otherwise)
        """
        header = """0 Homogeneous surface
1 (directional effects)
2 (Verstraete Pinty Dickinson model\n"""

        params_line = "%d %d %d\n" % (kappa_param, phase_funct, scattering_type)

        if kappa_param == KappaGivenValues:
            middle_line = "%f %f %f %f\n" % (leaf_area_density, sun_flecks_radius, k1, k2)
        else:
            middle_line = "%f %f %f\n" % (leaf_area_density, sun_flecks_radius, chil)

        if phase_funct == PhaseIsotropic:
            last_line = ""
        elif phase_funct == PhaseHeyneyGreenstein:
            last_line = "%f" % (asym_factor)
        else:
            last_line == "%f %f\n" % (legendre_first, legendre_second)

        return header + params_line + middle_line + last_line

    KappaGivenValues = 0
    KappaGoudriaan = 1
    KappaDickinson = 2

    PhaseIsotropic = 0
    PhaseHeyneyGreenstein = 1
    PhaseLegendre = 2

    SingleScatteringOnly = 0
    DickinsonMultipleScattering = 1

    @classmethod
    def HomogeneousKuuskMultispectralCR(cls, lai, lad_eps, lad_thm, relative_leaf_size, chlorophyll_content, leaf_water_equiv_thickness, effective_num_layers, ratio_refractive_indices, weight_first_price_function):
        """Parameterisation for a surface BRDF based on Kuusk's multispectral CR model.

        The Parameters are:

        - Leaf Area Index (0.1-10)
        - LAD eps (0.0-0.9)
        - LAD thm (0.0-90.0)
        - Relative leaf size (0.01-1.0)
        - Chlorophyll content (ug/cm^2, 0-30)
        - Leaf water equivalent thickness (0.01-0.03)
        - Effective number of elementary layers inside a leaf (1-225)
        - Ratio of refractive indices of the leaf surface wax and internal material (0-1.0)
        - Weight of the 1st Price function for the soil reflectance (0.1-0.8)

        """
        header = """0 Homogeneous surface
1 (directional effects)
9 (Kuusk's multispectral CR model)\n"""

        middle = "%f %f %f %f\n" % (lai, lad_eps, lad_thm, relative_leaf_size)

        bottom = "%f %f %f %f %f\n" % (chlorophyll_content, leaf_water_equiv_thickness, effective_num_layers, ratio_refractive_indices, weight_first_price_function)

        return header + middle + bottom
    @classmethod
    def HomogeneousUserDefined(cls, observed_reflectance, albedo, ro_sun_at_thetas, ro_sun_at_thetav):
        """Parameterisation for a user-defined surface BRDF.

        The parameters are:

        - `observed_reflectance` -- Observed reflectance in the geometry specified in the Geometry parameterisation
        - `albedo` -- Surface spherical albedo
        - `ro_sun_at_thetas` -- A reflectance table (described below) for the scenario when the sun is at theta_s
          (the solar zenith angle specified in the Geometry parameterisation)
        - `ro_sun_at_thetav` -- A reflectance table (described below) for the scenario when the sun is at theta_v
          (the view zenith angle specified in the Geometry parameterisation)

        The reflectance tables mentioned above must be NumPy arrays (that is, instances of :class:`ndarray`) with a shape of (10, 13) where the table headers are as below,
        and each cell contains the reflectance of the surface in the specified geometry::

                zenith
                0   10    20    30    40    50    60    70    80    85
          a 0
          z 30
          i 60
          m 90
          u 120
          t 150
          h .
            .
            .

        """
        header = "0 Homogeneous surface\n1 (directional effects)\n0 Input user's defined model\n"

        top_table = cls._ArrayToString(ro_sun_at_thetas)
        bottom_table = cls._ArrayToString(ro_sun_at_thetav)

        bottom = "%f\n %f\n" % (albedo, observed_reflectance)

        return header + top_table + "\n"+ bottom_table + bottom

    @classmethod
    def _ArrayToString(cls, array):
        text = StringIO.StringIO()
        np.savetxt(text, array, fmt="%.5f", delimiter=' ')
        s = text.getvalue()
        text.close()
        return s

    @classmethod
    def _GetTargetTypeAndValues(cls, target, name=None):
        if name is None:
            str_name = "REFL_REPLACE"
        else:
            str_name = name
        if isinstance(target, np.ndarray):
            target_type = "-1"
            target_value = str_name
        elif isinstance(target, collections.Iterable):
            # If it has
            target_type = "-1"
            target_value = " ".join(map(str, target))
        else:
            # If it's less than zero then it must be one of the predefined types
            if target < 0:
                target_type = str(-1 * target)
                target_value = ""
            # Otherwise it must be a constant ro
            else:
                target_type = "0"
                target_value = target

        return (target_type, target_value)
