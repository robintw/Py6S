import sixs
from Params import *
from pylab import *
import numpy as np

azimuths = np.linspace(0, 360, 360)
zeniths = np.arange(0, 70, 10)
values = []

# Create the 6S object
s = sixs.SixS()

# Set some parameters
s.aero_profile = AeroProfile.URBAN
s.ground_reflectance = GroundReflectance.HomogeneousRoujean(0.037, 0.0, 0.133)
s.solar_z = 30
s.solar_a = 0

for azimuth in azimuths:
  for zenith in zeniths:
    print "%i %i" % (azimuth, zenith)
    # Run some sort of model and get some output
    # We'll just use rand for this example
    s.view_a = azimuth
    s.view_z = zenith
    s.run()
    values.append(s.outputs.pixel_reflectance)
    
theta = np.radians(azimuths)

values = np.array(values)
values = values.reshape(len(azimuths), len(zeniths))

# This (from http://old.nabble.com/2D-polar-surface-plot-td28896848.html)
# works fine
##############
# Create a polar axes
# ax = subplot(111, projection='polar')
# pcolor plot onto it
# c = ax.pcolor(theta, zeniths, values)
# show()

r, theta = np.meshgrid(zeniths, np.radians(azimuths))
fig, ax = subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta, r, values)
autumn()
show()