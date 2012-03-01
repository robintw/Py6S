from Py6S import *
import numpy as np
from matplotlib.pyplot import *

class Wavelengths:
  """Helper functions for running the 6S model for a range of wavelengths, and plotting the result"""
  
  @classmethod
  def run_wavelengths(cls, s, wavelengths, output_name=None):
    """Runs the given SixS parameterisation for each of the wavelengths given, optionally extracting a specific output.
    
    Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``wavelengths`` -- An iterable containing the wavelengths to iterate over
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the wavelengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    
    Example usage::
    
      # Run for all wavelengths from 0.4 to 0.5 micrometers, with a spacing of 1nm, returns SixS.Outputs instances
      wavelengths, results = SixSHelpers.Wavelengths.run_for_wavelengths(s, np.arange(0.400, 0.500, 0.001))
      # Run for all wavelengths from 0.4 to 0.5 micrometers, with a spacing of 1nm, returns a list of pixel radiance values
      wavelengths, results = SixSHelpers.Wavelengths.run_for_wavelengths(s, np.arange(0.400, 0.500, 0.001), output_name='pixel_radiance')
      # Run for the first three Landsat TM bands
      wavelengths, results = SixSHelpers.Wavelengths.run_for_wavelengths(s, [Wavelength.LANDSAT_TM_B1, Wavelength.LANDSAT_TM_B2, Wavelength.LANDSAT_TM_B3)
    
    """
    results = []
    
    for wavelength in wavelengths:
      s.wavelength = Wavelength.Wavelength(wavelength)
      s.run()
      if output_name == None:
        results.append(s.outputs)
      else:
        results.append(getattr(s.outputs, output_name))
      
    return wavelengths, results

  @classmethod
  def run_vnir(cls, s, spacing=0.005, output_name=None):
    """Runs the given SixS parameterisation for wavelengths over the Visible-Near Infrared range, optionally extracting a specific output.
    
    By default, the given model is run for wavelengths from 0.4-1.4um, with a spacing of 5nm.
    
    Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``spacing`` -- (Optional) The spacing to use between each wavelength, in um. Eg. a spacing of 0.001 is a spacing of 1nm.
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the wavelengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    
    Example usage::
    
      # Run for the VNIR wavelengths, with the default spacing (5nm), returning SixS.Outputs instances
      wavelengths, results = SixSHelpers.Wavelengths.run_vnir(s)
      # Run for the VNIR wavelengths, with a spacing of 10nm, returning pixel reflectance values
      wavelengths, results = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.010, output_name='pixel_reflectance')
      
    """
    
    wv = np.arange(0.400, 1.400, spacing)
    return cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    
  @classmethod
  def run_whole_range(cls, s, spacing=0.010, output_name=None):
    """Runs the given SixS parameterisation for the entire wavelength range of the 6S model, optionally extracting a specific output.
    
    By default, the given model is run for wavelengths from 0.2-4.0um, with a spacing of 10nm.
    
    Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``spacing`` -- (Optional) The spacing to use between each wavelength, in um. Eg. a spacing of 0.001 is a spacing of 1nm.
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the wavelengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    
    Example usage::
    
      # Run for the VNIR wavelengths, with the default spacing (5nm), returning SixS.Outputs instances
      wavelengths, results = SixSHelpers.Wavelengths.run_vnir(s)
      # Run for the VNIR wavelengths, with a spacing of 10nm, returning pixel reflectance values
      wavelengths, results = SixSHelpers.Wavelengths.run_vnir(s, spacing=0.010, output_name='pixel_reflectance')
      
    """
    wv = np.arange(0.2, 4.0, spacing)
    return cls.run_for_wavelengths(s, wv, output_name=output_name)
  
  @classmethod
  def run_landsat_tm(cls, s, output_name=None):
    """Runs the given SixS parameterisation for all of the Landsat TM bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    
    wv = [Wavelengths.LANDSAT_TM_B1, Wavelengths.LANDSAT_TM_B2, Wavelengths.LANDSAT_TM_B3, Wavelengths.LANDSAT_TM_B4, Wavelengths.LANDSAT_TM_B5, Wavelengths.LANDSAT_TM_B7]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.485, 0.56, 0.66, 0.83, 1.65, 2.215]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_landsat_etm(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the Landsat ETM bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.ETM_B1, Wavelengths.ETM_B2, Wavelengths.ETM_B3, Wavelengths.ETM_B4, Wavelengths.ETM_B5, Wavelengths.ETM_B7]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.4825, 0.565, 0.66, 0.825, 1.65, 2.215]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_landsat_mss(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the Landsat MSS bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.LANDSAT_MSS_B1, Wavelengths.LANDSAT_MSS_B2, Wavelengths.LANDSAT_MSS_B3, Wavelengths.LANDSAT_MSS_B4]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.55, 0.65, 0.75, 0.95]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_meris(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the MERIS bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.MERIS_B1, Wavelengths.MERIS_B2, Wavelengths.MERIS_B3, Wavelengths.MERIS_B4, Wavelengths.MERIS_B5, Wavelengths.MERIS_B6, Wavelengths.MERIS_B7, Wavelengths.MERIS_B8, Wavelengths.MERIS_B9, Wavelengths.MERIS_B10, Wavelengths.MERIS_B11, Wavelengths.MERIS_B12, Wavelengths.MERIS_B14, Wavelengths.MERIS_B15]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.4125, 0.4425, 0.490, 0.510, 0.560, 0.620, 0.665, 0.8125, 0.70875, 0.75375, 0.760625, 0.77875, 0.865, 0.885, 0.900]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_modis(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the MODIS bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.MODIS_B1, Wavelengths.MODIS_B2, Wavelengths.MODIS_B3, Wavelengths.MODIS_B4, Wavelengths.MODIS_B5, Wavelengths.MODIS_B6, Wavelengths.MODIS_B7, Wavelengths.MERIS_B8]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.645, 0.8585, 0.469, 0.555, 1.24, 1.64, 2.13]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_spot_hrv(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the SPOT HRV (both 1 and 2, as the only bands specified are the same for both) bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.SPOT_HRV1_B1, Wavelengths.SPOT_HRV1_B2, Wavelengths.SPOT_HRV1_B3]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.545, 0.645, 0.84]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_spot_vgt(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the SPOT Vegetation bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.SPOT_VGT_B1, Wavelengths.SPOT_VGT_B2, Wavelengths.SPOT_VGT_B3, Wavelengths.SPOT_VGT_B4]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.45, 0.645, 0.835, 1.665]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_polder(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the POLDER bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.POLDER_B1, Wavelengths.POLDER_B2, Wavelengths.POLDER_B3, Wavelengths.POLDER_B4, Wavelengths.POLDER_B5, Wavelengths.POLDER_B6, Wavelengths.POLDER_B7, Wavelengths.POLDER_B8]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.4445, 0.4449, 0.4922, 0.5645, 0.6702, 0.7633, 0.7631, 0.9077]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_seawifs(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the SeaWiFS bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.SEAWIFS_B1, Wavelengths.SEAWIFS_B2, Wavelengths.SEAWIFS_B3, Wavelengths.SEAWIFS_B4, Wavelengths.SEAWIFS_B5, Wavelengths.SEAWIFS_B6, Wavelengths.SEAWIFS_B7, Wavelengths.SEAWIFS_B8]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.412, 0.443, 0.49, 0.51, 0.555, 0.67, 0.765, 0.865]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_aatsr(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the AATSR bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.AATSR_B1, Wavelengths.AATSR_B2, Wavelengths.AATSR_B3, Wavelengths.AATSR_B4]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.560, 0.660, 0.862, 1.594]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_aster(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the ASTER bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.ASTER_B1, Wavelengths.ASTER_B2, Wavelengths.ASTER_B3N, Wavelengths.ASTER_B3B, Wavelengths.ASTER_B4, Wavelengths.ASTER_B5, Wavelengths.ASTER_B6, Wavelengths.ASTER_B7, Wavelengths.ASTER_B8, Wavelengths.ASTER_B9]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.56, 0.66, 0.81, 0.81, 1.65, 2.185, 2.205, 2.26, 2.33, 2.395]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_viirs(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the VIIRS bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.VIIRS_BM1, Wavelengths.VIIRS_BM2, Wavelengths.VIIRS_BM3, Wavelengths.VIIRS_BM4, Wavelengths.VIIRS_BM5, Wavelengths.VIIRS_BM6, Wavelengths.VIIRS_BM7, Wavelengths.VIIRS_BM8, Wavelengths.VIIRS_BM9, Wavelengths.VIIRS_BM10, Wavelengths.VIIRS_BM11, Wavelengths.VIIRS_BM12, Wavelengths.VIIRS_BI1, Wavelengths.VIIRS_BI2, Wavelengths.VIIRS_B3, Wavelengths.VIIRS_B4]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.412, 0.445, 0.488, 0.555, 0.672, 0.746, 0.865, 1.24, 1.378, 1.61, 2.25, 3.70, 0.640, 0.865, 1.61, 3.74]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_er2_mas(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the ER2 MODIS Airborne Simulator (MAS) bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.ER2_MAS_B1, Wavelengths.ER2_MAS_B2, Wavelengths.ER2_MAS_B3, Wavelengths.ER2_MAS_B4, Wavelengths.ER2_MAS_B5, Wavelengths.ER2_MAS_B6, Wavelengths.ER2_MAS_B7]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.4649, 0.5494, 0.6550, 0.7024, 0.7431, 0.8248, 0.8667]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_ali(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the ALI bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.ALI_B1P, Wavelengths.ALI_B1, Wavelengths.ALI_B2, Wavelengths.ALI_B3, Wavelengths.ALI_B4, Wavelengths.ALI_B4P, Wavelengths.ALI_B5P, Wavelengths.ALI_B5, Wavelengths.ALI_B7]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.443, 0.4825, 0.565, 0.66, 0.79, 0.8675, 1.25, 1.65, 2.215]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_gli(cls, s, output_name=None):
      """Runs the given SixS parameterisation for all of the GLI bands within the 6S band range, optionally extracting a specific output.
    
     Arguments:
    
    * ``s`` -- A SixS instance with the parameters set as required
    * ``output_name`` -- (Optional) The output to extract from ``s.outputs``, as a string that could be placed after ``s.outputs.``, for example ``pixel_reflectance``
    
    Return value:
    
    A tuple containing the centre wavlengths used for the run and the results of the simulations. The results will be a list of :class:`SixS.Outputs` instances if ``output_name`` is not set,
    or a list of values of the selected output if ``output_name`` is set.
    """
    wv = [Wavelengths.GLI_B1, Wavelengths.GLI_B2, Wavelengths.GLI_B3, Wavelengths.GLI_B4, Wavelengths.GLI_B5, Wavelengths.GLI_B6, Wavelengths.GLI_B7, Wavelengths.GLI_B8, Wavelengths.GLI_B9, Wavelengths.GLI_B10, Wavelengths.GLI_B11, Wavelengths.GLI_B12, Wavelengths.GLI_B13, Wavelengths.GLI_B14, Wavelengths.GLI_B15, Wavelengths.GLI_B16, Wavelengths.GLI_B17, Wavelengths.GLI_B18, Wavelengths.GLI_B19, Wavelengths.GLI_B20, Wavelengths.GLI_B21, Wavelengths.GLI_B22, Wavelengths.GLI_B23, Wavelengths.GLI_B24, Wavelengths.GLI_B25, Wavelengths.GLI_B26, Wavelengths.GLI_B27, Wavelengths.GLI_B28, Wavelengths.GLI_B29, Wavelengths.GLI_B30]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.380, 0.400, 0.412, 0.443, 0.460, 0.490, 0.520, 0.545, 0.565, 0.625, 0.666, 0.680, 0.678, 0.710, 0.710, 0.749, 0.763, 0.865, 0.865, 0.460, 0.545, 0.660, 0.825, 1.050, 1.135, 1.240, 1.380, 1.640, 2.210, 3.715]
    
    return (centre_wvs, res)  
  
  @classmethod
  def plot_wavelengths(cls, wavelengths, values, y_axis_label):
    """Plot the given wavelengths and values, such as those produced by the other functions in this class.
    
    Arguments:
    
    * ``wavelengths`` -- A list of wavelengths (in um)
    * ``values`` -- A corresponding list of values at the wavelengths above
    * ``y_axis_label`` -- A string containing tha axis label to use for the Y axis
    
    Example usage::
    
      SixSHelpers.Wavelengths.plot_wavelengths(wavelengths, values, 'Pixel Radiance (W/m^2)')
    
    """
    
    plot(wavelengths, values, 'k')
    xlabel("Micrometres")
    ylabel(y_axis_label)
    show()