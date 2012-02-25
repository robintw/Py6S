import numpy as np

class Wavelengths:
  
  def run_for_wavelengths(s, wavelengths):
    results = []
    
    for wavelength in wavelengths:
      s.wavelength = Wavelength.Wavelength(wavelength)
      s.run()
      results.append(s.outputs)
      
    return results

  def run_for_vnir(s):
    wv = np.arange(0.450, 0.900, 0.010)
    return run_for_wavelengths(s, wv)