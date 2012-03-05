from Py6S import *
from matplotlib.pyplot import *
import copy

early = SixS()
early.altitudes.set_target_sea_level()
early.altitudes.set_sensor_satellite_level()
early.ground_reflectance = GroundReflectance.HomogeneousLambertian(GroundReflectance.GreenVegetation)

late = copy.deepcopy(early)

SixSHelpers.Aeronet.import_aeronet_data(early, "C:\Dropbox\Dropbox\Py6S_WriteUp\NCAVEO\CHL", "17/06/2006 08:00:00")
SixSHelpers.Aeronet.import_aeronet_data(late, "C:\Dropbox\Dropbox\Py6S_WriteUp\NCAVEO\CHL", "17/06/2006 11:30:00")




print "run 1"
wv, early_res = SixSHelpers.Wavelengths.run_vnir(early, spacing=0.01, output_name='pixel_radiance')
print "run 2"
wv, late_res = SixSHelpers.Wavelengths.run_vnir(late, spacing=0.01, output_name='pixel_radiance')

plot(wv, early_res, 'b-', wv, late_res, 'r-')
show()