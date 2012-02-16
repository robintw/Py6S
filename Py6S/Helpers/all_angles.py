import numpy as np
from matplotlib.pyplot import *

def all_angles(s):
  #if not isinstance(s, GeometryUser):
  #  raise ParameterError("geometry", "To use the all_angles helper you must be using a user-specified geometry (ie. a GeometryUser instance)")
  
  results = []
  
  azimuths = np.linspace(0, 360, 60)
  zeniths = np.arange(0, 70, 10)
    
  for azimuth in azimuths:
    for zenith in zeniths:
      s.geometry.view_a = azimuth
      s.geometry.view_z = zenith
      s.run()
      results.append(s.outputs)
      
  return results

def extract_output(results, output_name):
  results_output = [getattr(r, output_name) for r in results]
  return results_output
  
def plot_all_angles(data):
  azimuths = np.linspace(0, 360, 60)
  zeniths = np.arange(0, 70, 10)
  
  theta = np.radians(azimuths)
  zeniths = np.array(zeniths)

  values = np.array(data)
  values = values.reshape(len(azimuths), len(zeniths))

  r, theta = np.meshgrid(zeniths, np.radians(azimuths))
  fig, ax = subplots(subplot_kw=dict(projection='polar'))
  ax.contourf(theta, r, values)
  autumn()
  show()
  
if __name__ == '__main__':
  s = SixS()
  s.ground_reflectance = GroundReflectance.HomogeneousRoujean(0.037, 0.0, 0.133)
  s.solar_z = 30
  s.solar_a = 0
  
  res = all_angles(s)
  o = extract_output(res, 'pixel_reflectance')
  plot_all_angles(o)