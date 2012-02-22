import numpy as np
from matplotlib.pyplot import *

class Angles:
  def run_all_angles(s, solar_or_view, na=36, nz=10):
    #if not isinstance(s, GeometryUser):
    #  raise ParameterError("geometry", "To use the all_angles helper you must be using a user-specified geometry (ie. a GeometryUser instance)")
    
    results = []
    
    azimuths = np.linspace(0, 360, na)
    zeniths = np.linspace(0, 89, nz)
      
    for azimuth in azimuths:
      for zenith in zeniths:
        if solar_or_view == 'view':
          s.geometry.view_a = azimuth
          s.geometry.view_z = zenith
        elif solar_or_view == 'solar':
          s.geometry.solar_a = azimuth
          s.geometry.solar_z = zenith
        else:
          raise ParameterException("all_angles", "You must choose to vary either the solar or view angle.")
        s.run()
        print "%d %d" % (azimuth, zenith)
        results.append(s.outputs)
        
    return (results, azimuths, zeniths, s.geometry.solar_a, s.geometry.solar_z)  
  
  def extract_output(results, output_name):
    results_output = [getattr(r, output_name) for r in results]
    
    return results_output
    
  def plot_all_angles(data, output_name, show_sun=True):
    results, azimuths, zeniths, sa, sz = data
    
    values = extract_output(results, output_name)  
    
    fig, ax = plot_polar_contour(values, azimuths, zeniths)
    
    if show_sun:
      ax.autoscale(False)
      ax.plot(np.radians(sa), sz, '*', markersize=20, markerfacecolor='yellow', markeredgecolor='red')
      show()
    
    return fig, ax
    
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
    cb = fig.colorbar(cax)
    cb.set_label("Pixel reflectance")
    
    return fig, ax, cax
    
  def run_and_plot_all_angles(s, solar_or_view, output_name, show_sun=True, na=36, nz=10):
    if solar_or_view == 'solar':
      show_sun = False
    
    res = run_all_angles(s, solar_or_view, na, nz)  
    plot_res = plot_all_angles(res, output_name, show_sun)
    
    return plot_res
    
  def run_principal_plane(s):
    sa = s.geometry.solar_a
    sz = s.geometry.solar_z
    
    vz_for_sz = 90 - sz
    
    opp_sa = (sa + 180) % 360
    
    first_side_z = np.arange(vz_for_sz, -5, -5)
    first_side_a = np.repeat(sa, len(first_side_z))
    
    temp = first_side_z[:-1]
    second_side_z = temp[::-1] # Reverse array
    second_side_a = np.repeat(opp_sa, len(second_side_z))
    
    all_zeniths = np.hstack((first_side_z, second_side_z))
    all_azimuths = np.hstack((first_side_a, second_side_a))
    
    print all_zeniths
    print all_azimuths
    
    results = []
    
    for i in range(len(all_zeniths)):
      print all_zeniths[i]
      print all_azimuths[i]
      
      s.geometry.view_z = all_zeniths[i]
      s.geometry.view_a = all_azimuths[i]
      s.run()
      results.append(s.outputs.pixel_reflectance)
    
      
    # Must deal with zeniths and make half of them negative before returning, so plotting works
    return all_zeniths, results
