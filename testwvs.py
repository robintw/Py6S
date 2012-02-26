from Py6S import *
import numpy as np
from matplotlib.pyplot import *

s = SixS()

wv = np.arange(0.400, 0.900, 0.002)

s.ground_reflectance = GroundReflectance.HomogeneousLambertian(GroundReflectance.GreenVegetation)

s.aot550 = 0.2

wavelengths, values = SixSHelpers.Wavelengths.run_vnir(s, output_name="pixel_radiance")
SixSHelpers.Wavelengths.plot_wavelengths(wavelengths, values)