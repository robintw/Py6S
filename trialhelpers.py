from Py6S import *

s = SixS()
s.ground_reflectance = GroundReflectance.HomogeneousWalthall(0.48, 0.50, 2.95, 0.6)
s.geometry.solar_z = 30
s.geometry.solar_a = 0

SixSHelpers.Angles.run_and_plot_360(s, 'view', "pixel_reflectance")