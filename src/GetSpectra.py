import numpy as np
from SixS import SixS

test = SixS()

wavelengths = []
direct_res = []
diffuse_res = []

for wv in np.arange(0.4, 0.8, 0.001):
    test.wavelength = wv
    test.write_input_file()
    test.run()
    
    
    wavelengths.append(wv)
    direct_res.append(test.outputs.irradiance_direct)
    diffuse_res.append(test.outputs.irradiance_diffuse)
    
print direct_res
#plt.plot(wavelengths, direct_res, "r", label="Direct")
#plt.plot(wavelengths, diffuse_res, "b", label="Diffuse")
#plt.xlabel("Wavelength (micrometres)")
#plt.ylabel("Irradiance (W/m2/mic)")
#plt.title("View Zenith: 23, View Azimuth: 190")
#plt.legend()
#plt.savefig("FirstOutput_a.png")