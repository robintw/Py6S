import numpy as np
from matplotlib.pyplot import *


def all_angles(s):
  #if not isinstance(s, GeometryUser):
  #  raise ParameterError("geometry", "To use the all_angles helper you must be using a user-specified geometry (ie. a GeometryUser instance)")
  
  results = []
  
  azimuths = np.arange(0, 375, 15)
  zeniths = np.arange(0, 90, 10)
    
  for azimuth in azimuths:
    for zenith in zeniths:
      s.geometry.view_a = azimuth
      s.geometry.view_z = zenith
      s.run()
      print "%d %d" % (azimuth, zenith)
      results.append(s.outputs)
      
  return (results, azimuths, zeniths)

def extract_output(data, output_name):
  results = data[0]
  results_output = [getattr(r, output_name) for r in results]
  
  return (results_output, data[1], data[2])
  
def plot_all_angles(data):
  values = data[0]
  azimuths = data[1]
  zeniths = data[2]
  
  plot_polar_contour(values, azimuths, zeniths)
  
def plot_polar_contour(values, azimuths, zeniths):
  theta = np.radians(azimuths)
  zeniths = np.array(zeniths)

  values = np.array(values)
  values = values.reshape(len(azimuths), len(zeniths))

  r, theta = np.meshgrid(zeniths, np.radians(azimuths))
  fig, ax = subplots(subplot_kw=dict(projection='polar'))
  ax.set_theta_zero_location("N")
  ax.set_theta_direction(-1)
  cax = ax.contourf(theta, r, values, 30)
  autumn()
  cb = fig.colorbar(cax)
  cb.set_label("Pixel reflectance")
  #ax.plot(0, 30, 'p', scalex=False, scaley=False)
  ax.autoscale(False)
  ax.plot(0, 30, 'p')
  
  show()
  #import ipdb; ipdb.set_trace()
