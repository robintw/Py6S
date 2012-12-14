# This file is part of Py6S.
#
# Copyright 2012 Robin Wilson and contributors listed in the CONTRIBUTORS file.
#
# Py6S is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Py6S is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Py6S.  If not, see <http://www.gnu.org/licenses/>.

import sixs
from Params import *
from pylab import *
import numpy as np

# Create the 6S object
s = sixs.SixS()

# Set some parameters
s.aero_profile = AeroProfile.URBAN
s.ground_reflectance = GroundReflectance.HomogeneousRoujean(0.037, 0.0, 0.133)
s.solar_z = 30
s.solar_a = 0

azimuths = np.arange(0, 360, 1)
zeniths = np.arange(0, 90, 10)
values = []

for azimuth in azimuths:
  for zenith in zeniths:
    s.view_a = azimuth
    s.view_z = zenith
    s.run()
    print "%i %i" % (azimuth, zenith)
    values.append(s.outputs.pixel_reflectance)
    
theta = np.radians(azimuths)

values = np.array(values)
values = values.reshape(len(azimuths), len(zeniths))

r, t = np.meshgrid(zeniths, azimuths)

x = r*np.cos(t)
y = r*np.sin(t)

contourf(x, y, values)
