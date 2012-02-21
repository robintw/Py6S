import numpy as np
from matplotlib.pyplot import *

from matplotlib.projections import PolarAxes, register_projection
from matplotlib.transforms import Affine2D, Bbox, IdentityTransform

class NorthPolarAxes(PolarAxes):
    '''
    A variant of PolarAxes where theta starts pointing north and goes
    clockwise.
    '''
    name = 'northpolar'

    class NorthPolarTransform(PolarAxes.PolarTransform):
        def transform(self, tr):
            xy   = np.zeros(tr.shape, np.float_)
            t    = tr[:, 0:1]
            r    = tr[:, 1:2]
            x    = xy[:, 0:1]
            y    = xy[:, 1:2]
            x[:] = r * np.sin(t)
            y[:] = r * np.cos(t)
            return xy

        transform_non_affine = transform

        def inverted(self):
            return NorthPolarAxes.InvertedNorthPolarTransform()

    class InvertedNorthPolarTransform(PolarAxes.InvertedPolarTransform):
        def transform(self, xy):
            x = xy[:, 0:1]
            y = xy[:, 1:]
            r = np.sqrt(x*x + y*y)
            theta = np.arctan2(y, x)
            return np.concatenate((theta, r), 1)

        def inverted(self):
            return NorthPolarAxes.NorthPolarTransform()

    def _set_lim_and_transforms(self):
        PolarAxes._set_lim_and_transforms(self)
        self.transProjection = self.NorthPolarTransform()
        self.transData = (
            self.transScale + 
            self.transProjection + 
            (self.transProjectionAffine + self.transAxes))
        self._xaxis_transform = (
            self.transProjection +
            self.PolarAffine(IdentityTransform(), Bbox.unit()) +
            self.transAxes)
        self._xaxis_text1_transform = (
            self._theta_label1_position +
            self._xaxis_transform)
        self._yaxis_transform = (
            Affine2D().scale(np.pi * 2.0, 1.0) +
            self.transData)
        self._yaxis_text1_transform = (
            self._r_label1_position +
            Affine2D().scale(1.0 / 360.0, 1.0) +
            self._yaxis_transform)

register_projection(NorthPolarAxes)

def all_angles(s):
  #if not isinstance(s, GeometryUser):
  #  raise ParameterError("geometry", "To use the all_angles helper you must be using a user-specified geometry (ie. a GeometryUser instance)")
  
  results = []
  
  azimuths = np.arange(0, 375, 15)
  zeniths = np.arange(0, 100, 10)
    
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
  fig, ax = subplots(subplot_kw=dict(projection='northpolar'))
  ax.contourf(theta, r, values)
  show()