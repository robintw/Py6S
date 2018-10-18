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

from Py6S import *
import numpy as np
from matplotlib.pyplot import *
import copy
import sys

class Wavelengths:

    """Helper functions for running the 6S model for a range of wavelengths, and plotting the result"""

    @classmethod
    def run_wavelengths(cls, s, wavelengths, output_name=None, n=None, verbose=True):
        """Runs the given SixS parameterisation for each of the wavelengths given, optionally extracting a specific output.

        This function is used by all of the other wavelengths running functions, such as :method:`run_vnir`, and thus
        any arguments that are passed to this function can also be passed to these other functions.

        The calls to 6S for each wavelength will be run in parallel, making this function far faster than simply
        running a for loop over each wavelength.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``wavelengths`` -- An iterable containing the wavelengths to iterate over
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
        * ``n`` -- (Optional) The number of threads to run in parallel. This defaults to the number of CPU cores in your system, and is unlikely to need changing.
        * ``verbose`` -- (Optional) Print wavelengths as Py6S is running (default=True)

        Return value:

        A tuple containing the wavelengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.

        Example usage::

          # Run for all wavelengths from 0.4 to 0.5 micrometers, with a spacing of 1nm, returns SixS.Outputs instances
          wavelengths, results = SixSHelpers.PredefinedWavelengths.run_wavelengths(s, np.arange(0.400, 0.500, 0.001))
          # Run for all wavelengths from 0.4 to 0.5 micrometers, with a spacing of 1nm, returns a list of pixel radiance values
          wavelengths, results = SixSHelpers.PredefinedWavelengths.run_wavelengths(s, np.arange(0.400, 0.500, 0.001), output_name='pixel_radiance')
          # Run for the first three Landsat TM bands
          wavelengths, results = SixSHelpers.PredefinedWavelengths.run_wavelengths(s, [PredefinedWavelengths.LANDSAT_TM_B1, PredefinedWavelengths.LANDSAT_TM_B2, PredefinedWavelengths.LANDSAT_TM_B3)

        """
        # Create a function to be called by the map
        def f(wv):
            s.outputs = None
            a = copy.deepcopy(s)
            a.wavelength = Wavelength(wv)
            if verbose:
               print(wv)
            a.run()
            if output_name is None:
                return a.outputs
            else:
                return cls.recursive_getattr(a.outputs, output_name)

        # Run the map
        from multiprocessing.dummy import Pool

        if n is None:
            pool = Pool()
        else:
            pool = Pool(n)

        if verbose:
            print("wavelengths pass:")
            print(wavelengths)
            print(type(wavelengths))

        print("Running for many wavelengths - this may take a long time")
        results = pool.map(f, wavelengths)

        pool.close()
        pool.join()

        try:
            if len(wavelengths[0]) == 4:
                cleaned_wavelengths = list(map(lambda x: x[:3], wavelengths))
                return np.array(cleaned_wavelengths), np.array(results)
            else:
                return np.array(wavelengths), np.array(results)
        except:
            return np.array(wavelengths), np.array(results)

    @classmethod
    def run_vnir(cls, s, spacing=0.005, **kwargs):
        """Runs the given SixS parameterisation for wavelengths over the Visible-Near Infrared range, optionally extracting a specific output.

        By default, the given model is run for wavelengths from 0.4-1.4um, with a spacing of 5nm.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``spacing`` -- (Optional) The spacing to use between each wavelength, in um. Eg. a spacing of 0.001 is a spacing of 1nm.
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the wavelengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.

        Example usage::

          # Run for the VNIR wavelengths, with the default spacing (5nm), returning SixS.Outputs instances
          wavelengths, results = SixSHelpers.PredefinedWavelengths.run_vnir(s)
          # Run for the VNIR wavelengths, with a spacing of 10nm, returning pixel reflectance values
          wavelengths, results = SixSHelpers.PredefinedWavelengths.run_vnir(s, spacing=0.010, output_name='pixel_reflectance')

        """

        wv = np.arange(0.400, 1.400, spacing)
        return cls.run_wavelengths(s, wv, **kwargs)

    @classmethod
    def run_whole_range(cls, s, spacing=0.010, **kwargs):
        """Runs the given SixS parameterisation for the entire wavelength range of the 6S model, optionally extracting a specific output.

        By default, the given model is run for wavelengths from 0.2-4.0um, with a spacing of 10nm.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``spacing`` -- (Optional) The spacing to use between each wavelength, in um. Eg. a spacing of 0.001 is a spacing of 1nm.
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the wavelengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.

        Example usage::

          # Run for the VNIR wavelengths, with the default spacing (5nm), returning SixS.Outputs instances
          wavelengths, results = SixSHelpers.PredefinedWavelengths.run_vnir(s)
          # Run for the VNIR wavelengths, with a spacing of 10nm, returning pixel reflectance values
          wavelengths, results = SixSHelpers.PredefinedWavelengths.run_vnir(s, spacing=0.010, output_name='pixel_reflectance')

        """
        wv = np.arange(0.2, 4.0, spacing)
        return cls.run_wavelengths(s, wv, **kwargs)

    @classmethod
    def to_centre_wavelengths(cls, item):
        """Get centre wavelengths for a sensor from a list of the wavelength tuples.

        This is calculated simple as minwv+((maxwv-minwv)/2) and is the CENTER wavelength
        (that is the wavelength in the middle of the range) not necessarily the peak wavelength.

        """
        calc_range = item[2] - item[1]
        return (item[1] + calc_range / 2)

    @classmethod
    def run_landsat_tm(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the Landsat TM bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """

        wv = [PredefinedWavelengths.LANDSAT_TM_B1, PredefinedWavelengths.LANDSAT_TM_B2, PredefinedWavelengths.LANDSAT_TM_B3, PredefinedWavelengths.LANDSAT_TM_B4, PredefinedWavelengths.LANDSAT_TM_B5, PredefinedWavelengths.LANDSAT_TM_B7]

        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_landsat_oli(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the Landsat TM bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """

        wv = [PredefinedWavelengths.LANDSAT_OLI_B1,
              PredefinedWavelengths.LANDSAT_OLI_B2,
              PredefinedWavelengths.LANDSAT_OLI_B3,
              PredefinedWavelengths.LANDSAT_OLI_B4,
              PredefinedWavelengths.LANDSAT_OLI_B5,
              PredefinedWavelengths.LANDSAT_OLI_B6,
              PredefinedWavelengths.LANDSAT_OLI_B7,
              PredefinedWavelengths.LANDSAT_OLI_B8,
              PredefinedWavelengths.LANDSAT_OLI_B9]

        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_landsat_etm(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the Landsat ETM bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.LANDSAT_ETM_B1, PredefinedWavelengths.LANDSAT_ETM_B2, PredefinedWavelengths.LANDSAT_ETM_B3, PredefinedWavelengths.LANDSAT_ETM_B4, PredefinedWavelengths.LANDSAT_ETM_B5, PredefinedWavelengths.LANDSAT_ETM_B7]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_landsat_mss(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the Landsat MSS bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.LANDSAT_MSS_B1, PredefinedWavelengths.LANDSAT_MSS_B2, PredefinedWavelengths.LANDSAT_MSS_B3, PredefinedWavelengths.LANDSAT_MSS_B4]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_s2a_msi(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the Sentinel2/MSI bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.S2A_MSI_01,
              PredefinedWavelengths.S2A_MSI_02,
              PredefinedWavelengths.S2A_MSI_03,
              PredefinedWavelengths.S2A_MSI_04,
              PredefinedWavelengths.S2A_MSI_05,
              PredefinedWavelengths.S2A_MSI_06,
              PredefinedWavelengths.S2A_MSI_07,
              PredefinedWavelengths.S2A_MSI_08,
              PredefinedWavelengths.S2A_MSI_09,
              PredefinedWavelengths.S2A_MSI_10,
              PredefinedWavelengths.S2A_MSI_11,
              PredefinedWavelengths.S2A_MSI_12,
              PredefinedWavelengths.S2A_MSI_13]

        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_s3a_olci(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the Sentinel3/OLCI bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.S3A_OLCI_01,
              PredefinedWavelengths.S3A_OLCI_02,
              PredefinedWavelengths.S3A_OLCI_03,
              PredefinedWavelengths.S3A_OLCI_04,
              PredefinedWavelengths.S3A_OLCI_05,
              PredefinedWavelengths.S3A_OLCI_06,
              PredefinedWavelengths.S3A_OLCI_07,
              PredefinedWavelengths.S3A_OLCI_08,
              PredefinedWavelengths.S3A_OLCI_09,
              PredefinedWavelengths.S3A_OLCI_10,
              PredefinedWavelengths.S3A_OLCI_11,
              PredefinedWavelengths.S3A_OLCI_12,
              PredefinedWavelengths.S3A_OLCI_13,
              PredefinedWavelengths.S3A_OLCI_14,
              PredefinedWavelengths.S3A_OLCI_15,
              PredefinedWavelengths.S3A_OLCI_16,
              PredefinedWavelengths.S3A_OLCI_17,
              PredefinedWavelengths.S3A_OLCI_18,
              PredefinedWavelengths.S3A_OLCI_19,
              PredefinedWavelengths.S3A_OLCI_20,
              PredefinedWavelengths.S3A_OLCI_21]

        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)


    @classmethod
    def run_s3a_slstr(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the Sentinel3/SLSTR bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.S3A_SLSTR_01,
              PredefinedWavelengths.S3A_SLSTR_02,
              PredefinedWavelengths.S3A_SLSTR_03,
              PredefinedWavelengths.S3A_SLSTR_04,
              PredefinedWavelengths.S3A_SLSTR_05,
              PredefinedWavelengths.S3A_SLSTR_06]

        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)



    @classmethod
    def run_meris(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the MERIS bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.MERIS_B1, PredefinedWavelengths.MERIS_B2, PredefinedWavelengths.MERIS_B3, PredefinedWavelengths.MERIS_B4, PredefinedWavelengths.MERIS_B5, PredefinedWavelengths.MERIS_B6, PredefinedWavelengths.MERIS_B7, PredefinedWavelengths.MERIS_B9, PredefinedWavelengths.MERIS_B10, PredefinedWavelengths.MERIS_B11, PredefinedWavelengths.MERIS_B12, PredefinedWavelengths.MERIS_B8, PredefinedWavelengths.MERIS_B13, PredefinedWavelengths.MERIS_B14, PredefinedWavelengths.MERIS_B15]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_modis(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the MODIS bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.MODIS_B8, PredefinedWavelengths.MODIS_B3, PredefinedWavelengths.MODIS_B4, PredefinedWavelengths.MODIS_B1, PredefinedWavelengths.MODIS_B2, PredefinedWavelengths.MODIS_B5, PredefinedWavelengths.MODIS_B6, PredefinedWavelengths.MODIS_B7]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_aqua(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the MODIS bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.ACCURATE_MODIS_AQUA_1,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_2,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_3,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_4,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_5,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_6,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_7,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_11,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_12,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_13,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_14,
              PredefinedWavelengths.ACCURATE_MODIS_AQUA_15]

        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)


    @classmethod
    def run_terra(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the MODIS bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.ACCURATE_MODIS_TERRA_1,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_2,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_3,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_4,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_5,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_6,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_7,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_11,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_12,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_13,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_14,
              PredefinedWavelengths.ACCURATE_MODIS_TERRA_15]

        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)


    @classmethod
    def run_spot_hrv(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the SPOT HRV (both 1 and 2, as the only bands specified are the same for both) bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.SPOT_HRV1_B1, PredefinedWavelengths.SPOT_HRV1_B2, PredefinedWavelengths.SPOT_HRV1_B3]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_spot_vgt(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the SPOT Vegetation bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.SPOT_VGT_B1, PredefinedWavelengths.SPOT_VGT_B2, PredefinedWavelengths.SPOT_VGT_B3, PredefinedWavelengths.SPOT_VGT_B4]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_polder(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the POLDER bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.POLDER_B1, PredefinedWavelengths.POLDER_B2, PredefinedWavelengths.POLDER_B3, PredefinedWavelengths.POLDER_B4, PredefinedWavelengths.POLDER_B5, PredefinedWavelengths.POLDER_B6, PredefinedWavelengths.POLDER_B7, PredefinedWavelengths.POLDER_B8]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_seawifs(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the SeaWiFS bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.SEAWIFS_B1, PredefinedWavelengths.SEAWIFS_B2, PredefinedWavelengths.SEAWIFS_B3, PredefinedWavelengths.SEAWIFS_B4, PredefinedWavelengths.SEAWIFS_B5, PredefinedWavelengths.SEAWIFS_B6, PredefinedWavelengths.SEAWIFS_B7, PredefinedWavelengths.SEAWIFS_B8]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_aatsr(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the AATSR bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.AATSR_B1, PredefinedWavelengths.AATSR_B2, PredefinedWavelengths.AATSR_B3, PredefinedWavelengths.AATSR_B4]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_aster(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the ASTER bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.ASTER_B1, PredefinedWavelengths.ASTER_B2, PredefinedWavelengths.ASTER_B3N, PredefinedWavelengths.ASTER_B3B, PredefinedWavelengths.ASTER_B4, PredefinedWavelengths.ASTER_B5, PredefinedWavelengths.ASTER_B6, PredefinedWavelengths.ASTER_B7, PredefinedWavelengths.ASTER_B8, PredefinedWavelengths.ASTER_B9]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_viirs(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the VIIRS bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.VIIRS_BM1, PredefinedWavelengths.VIIRS_BM2, PredefinedWavelengths.VIIRS_BM3, PredefinedWavelengths.VIIRS_BM4, PredefinedWavelengths.VIIRS_BI1, PredefinedWavelengths.VIIRS_BM5, PredefinedWavelengths.VIIRS_BM6, PredefinedWavelengths.VIIRS_BM7, PredefinedWavelengths.VIIRS_BM8, PredefinedWavelengths.VIIRS_BM9, PredefinedWavelengths.VIIRS_BM10, PredefinedWavelengths.VIIRS_BM11, PredefinedWavelengths.VIIRS_BM12, PredefinedWavelengths.VIIRS_BI4]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_er2_mas(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the ER2 MODIS Airborne Simulator (MAS) bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.ER2_MAS_B1, PredefinedWavelengths.ER2_MAS_B2, PredefinedWavelengths.ER2_MAS_B3, PredefinedWavelengths.ER2_MAS_B4, PredefinedWavelengths.ER2_MAS_B5, PredefinedWavelengths.ER2_MAS_B6, PredefinedWavelengths.ER2_MAS_B7]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_ali(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the ALI bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.ALI_B1P, PredefinedWavelengths.ALI_B1, PredefinedWavelengths.ALI_B2, PredefinedWavelengths.ALI_B3, PredefinedWavelengths.ALI_B4, PredefinedWavelengths.ALI_B4P, PredefinedWavelengths.ALI_B5P, PredefinedWavelengths.ALI_B5, PredefinedWavelengths.ALI_B7]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def run_gli(cls, s, **kwargs):
        """Runs the given SixS parameterisation for all of the GLI bands within the 6S band range, optionally extracting a specific output.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance with the parameters set as required
        * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``

        Return value:

        A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
        or a list of values of the selected output if ``output_name`` is set.
        """
        wv = [PredefinedWavelengths.GLI_B1, PredefinedWavelengths.GLI_B2, PredefinedWavelengths.GLI_B3, PredefinedWavelengths.GLI_B4, PredefinedWavelengths.GLI_B5, PredefinedWavelengths.GLI_B6, PredefinedWavelengths.GLI_B7, PredefinedWavelengths.GLI_B8, PredefinedWavelengths.GLI_B9, PredefinedWavelengths.GLI_B10, PredefinedWavelengths.GLI_B22, PredefinedWavelengths.GLI_B11, PredefinedWavelengths.GLI_B12, PredefinedWavelengths.GLI_B13, PredefinedWavelengths.GLI_B14, PredefinedWavelengths.GLI_B15, PredefinedWavelengths.GLI_B16, PredefinedWavelengths.GLI_B17, PredefinedWavelengths.GLI_B18, PredefinedWavelengths.GLI_B23, PredefinedWavelengths.GLI_B19, PredefinedWavelengths.GLI_B24, PredefinedWavelengths.GLI_B25, PredefinedWavelengths.GLI_B26, PredefinedWavelengths.GLI_B27, PredefinedWavelengths.GLI_B28, PredefinedWavelengths.GLI_B29, PredefinedWavelengths.GLI_B30]
        wv, res = cls.run_wavelengths(s, wv, **kwargs)

        centre_wvs = map(cls.to_centre_wavelengths, wv)

        if sys.version_info[0] >= 3:
            centre_wvs = list(centre_wvs)

        return (centre_wvs, res)

    @classmethod
    def recursive_getattr(cls, obj, attr):
        prev_part = obj

        for part in attr.split("."):
            prev_part = getattr(prev_part, part)

        return prev_part

    @classmethod
    def extract_output(cls, results, output_name):
        """Extracts data for one particular SixS output from a list of SixS.Outputs instances.

        Basically just a wrapper around a list comprehension.

        Arguments:

        * ``results`` -- A list of :class:`.SixS.Outputs` instances
        * ``output_name`` -- The name of the output to extract. This should be a string containing whatever is put after the `s.outputs` when printing the output, for example `'pixel_reflectance'`.

        """
        results_output = [cls.recursive_getattr(r, output_name) for r in results]

        return results_output

    @classmethod
    def plot_wavelengths(cls, wavelengths, values, y_axis_label):
        """Plot the given wavelengths and values, such as those produced by the other functions in this class.

        Arguments:

        * ``wavelengths`` -- A list of wavelengths (in um)
        * ``values`` -- A corresponding list of values at the wavelengths above
        * ``y_axis_label`` -- A string containing tha axis label to use for the Y axis

        Example usage::

          SixSHelpers.PredefinedWavelengths.plot_wavelengths(wavelengths, values, 'Pixel Radiance ($W/m^2$)')

        """

        plot(wavelengths, values, 'k')
        xlabel("Wavelength ($\mu m$)")
        ylabel(y_axis_label)
        show()
