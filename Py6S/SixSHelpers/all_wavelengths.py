from Py6S import *
import numpy as np
from matplotlib.pyplot import *

class Wavelengths:
  
  @classmethod
  def run_for_wavelengths(cls, s, wavelengths, output_name=None):
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
    wv = np.arange(0.400, 1.400, spacing)
    return cls.run_for_wavelengths(s, wv, output_name=output_name)
  
  @classmethod
  def run_whole_range(cls, s, spacing=0.010, output_name=None):
    wv = np.arange(0.2, 4.0, spacing)
    return cls.run_for_wavelengths(s, wv, output_name=output_name)
  
  @classmethod
  def plot_wavelengths(cls, wavelengths, values):
    plot(wavelengths, values)
    xlabel("Micrometres")
    