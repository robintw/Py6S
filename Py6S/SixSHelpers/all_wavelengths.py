from Py6S import *
import numpy as np
from matplotlib.pyplot import *

class Wavelengths:
  """Helper functions for running the 6S model for a range of wavelengths, and plotting the result"""
  
  @classmethod
  def run_for_wavelengths(cls, s, wavelengths, output_name=None):
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
  def run_landsat_tm(cls, s, output_name=None):
    wv = [Wavelengths.LANDSAT_TM_B1, Wavelengths.LANDSAT_TM_B2, Wavelengths.LANDSAT_TM_B3, Wavelengths.LANDSAT_TM_B4, Wavelengths.LANDSAT_TM_B5, Wavelengths.LANDSAT_TM_B7]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.485, 0.56, 0.66, 0.83, 1.65, 2.215]
    
    return (centre_wvs, res)
    
  @classmethod
  def run_landsat_etm(cls, s, output_name=None):
    wv = [Wavelengths.ETM_B1, Wavelengths.ETM_B2, Wavelengths.ETM_B3, Wavelengths.ETM_B4, Wavelengths.ETM_B5, Wavelengths.ETM_B7]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.4825, 0.565, 0.66, 0.825, 1.65, 2.215]
    
    return (centre_wvs, res)
  
  @classmethod
  def run_landsat_mss(cls, s, output_name=None):
    wv = [Wavelengths.LANDSAT_MSS_B1, Wavelengths.LANDSAT_MSS_B2, Wavelengths.LANDSAT_MSS_B3, Wavelengths.LANDSAT_MSS_B4]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.55, 0.65, 0.75, 0.95]
    
    return (centre_wvs, res)
    
  def run_meris(cls, s, output_name=None):
    wv = [Wavelengths.MERIS_B1, Wavelengths.MERIS_B2, Wavelengths.MERIS_B3, Wavelengths.MERIS_B4, Wavelengths.MERIS_B5, Wavelengths.MERIS_B6, Wavelengths.MERIS_B7, Wavelengths.MERIS_B8, Wavelengths.MERIS_B9, Wavelengths.MERIS_B10, Wavelengths.MERIS_B11, Wavelengths.MERIS_B12, Wavelengths.MERIS_B14, Wavelengths.MERIS_B15]
    wv, res = cls.run_for_wavelengths(s, wv, output_name=output_name)
    
    centre_wvs = [0.4125, 0.4425, 0.490, 0.510, 0.560, 0.620, 0.665, 0.8125, 0.70875, 0.75375, 0.760625, 0.77875, 0.865, 0.885, 0.900]
    
    return (centre_wvs, res)
  
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