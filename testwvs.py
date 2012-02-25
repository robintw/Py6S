from Py6S import *
import numpy as np
from matplotlib.pyplot import *

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

def extract_output(results, output_name):
  """Extracts data for one particular SixS output from a list of SixS.Outputs instances.
  
  Basically just a wrapper around a list comprehension.
  
  Arguments:
  
   * `results` -- A list of :class:`SixS.Outputs` instances
   * `output_name` -- The name of the output to extract. This should be a string containing whatever is put after the `s.outputs` when printing the output, for example `'pixel_reflectance'`.
  
  """
  results_output = [getattr(r, output_name) for r in results]
  
  return results_output  

s = SixS()

wv = np.arange(0.400, 0.900, 0.002)

s.ground_reflectance = GroundReflectance.HomogeneousLambertian(GroundReflectance.GreenVegetation)

s.aot550 = 0.2

res = extract_output(run_for_wavelengths(s, wv), 'pixel_radiance')

plot(wv, res)

s.aot550 = 0.6
res = extract_output(run_for_wavelengths(s, wv), 'pixel_radiance')

plot(wv, res)