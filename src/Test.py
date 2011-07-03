from Py6S import *
from Py6S.Params.wavelength import Wavelength
import numpy as np
import matplotlib.pyplot as plt
import matplotlib



test = SixS()

test.wavelength = Wavelength.Wavelength(Wavelength.ETM_B1)

zenith = np.arange(10, 90, 5)
azimuth = np.arange(0, 359, 30)

value = []
radius = []
theta = []

for z in zenith:
    for a in azimuth:
        test.view_z = z
        test.view_a = a
        test.run()
        value.append(test.outputs.direct_solar_irradiance)
        radius.append(z)
        theta.append(a)
        
        
value = np.array(value)
radius = np.array(radius)
theta = np.array(theta)

print value
print max(value)
print min(value)

print np.shape(radius)
print np.shape(theta)

x = radius * np.cos(theta)
y = radius * np.sin(theta)
#Z = np.reshape(value, (len(zenith), len(azimuth)))

xi = np.linspace(min(x), max(x), 200)
yi = np.linspace(min(y), max(y), 200)
zi = matplotlib.mlab.griddata(x, y, value, xi, yi)

ax = plt.subplot(111)

ax.contourf(xi, yi, zi, 100)

# make sure aspect ratio preserved
ax.set_aspect('equal')
plt.show()

print "Done"
        