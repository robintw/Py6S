# Import Py6S
# Import the functions for copying objects
import copy

# Import the Matplotlib plotting environment
from matplotlib.pyplot import *

from Py6S import *


# Define a function to easily calculate NDVI
def ndvi(red, nir):
    return (nir - red) / (nir + red)


# Create a SixS object for the 'early' time (~08:00)
early = SixS()
# Set the altitudes
early.altitudes.set_target_sea_level()
early.altitudes.set_sensor_satellite_level()
# Set the ground reflectance to be a typical green veg spectrum
early.ground_reflectance = GroundReflectance.HomogeneousLambertian(
    GroundReflectance.GreenVegetation
)
early.geometry = Geometry.User()

# Make a copy of the SixS object to use for the 'late' time (~11:30)
late = copy.deepcopy(early)

# Import the AERONET data into each SixS object
SixSHelpers.Aeronet.import_aeronet_data(early, "CHL", "17/06/2006 08:00:00")
SixSHelpers.Aeronet.import_aeronet_data(late, "CHL", "17/06/2006 11:30:00")

# Set the geometry for each SixS object
# With solar angles from location and time and
# with view from nadir
early.geometry.from_time_and_location(51.14510, -1.43861, "2006-06-17 08:00:00", 0, 0)
late.geometry.from_time_and_location(51.14510, -1.43861, "2006-06-1711:30:00", 0, 0)

# Run each simulation for the VNIR wavelengths - using a wider spacing than default
# to make the simulation faster
wv, early_res = SixSHelpers.Wavelengths.run_vnir(early, spacing=0.01, output_name="pixel_radiance")
wv, late_res = SixSHelpers.Wavelengths.run_vnir(late, spacing=0.01, output_name="pixel_radiance")

# Plot the two radiance curves
clf()
plot(wv, early_res, "b-", label="08:00")
plot(wv, late_res, "r-", label="11:30")
xlabel("Wavelength ($\mu m$)")
ylabel("Radiance ($W/m^2$)")
legend()
savefig("ncaveo_radiances.png")

# Calculate the percentage difference and plot it
clf()
perc_diff = ((early_res - late_res) / early_res) * 100
plot(wv, perc_diff)
xlabel("Wavelength ($\mu m$)")
ylabel("Percentage difference from 08:10 measurement (%)")
savefig("ncaveo_perc_diff.png")

# Run simulations again for the SPOT HRV sensor
# to then calculate the NDVI difference
wv, early_spot = SixSHelpers.Wavelengths.run_spot_hrv(early, output_name="pixel_radiance")
wv, late_spot = SixSHelpers.Wavelengths.run_spot_hrv(late, output_name="pixel_radiance")

print(early_spot)
print(late_spot)

# Calculate NDVIs
early_ndvi = ndvi(early_spot[1], early_spot[2])
late_ndvi = ndvi(late_spot[1], late_spot[2])

print("Early NDVI:\t%f" % early_ndvi)
print("Late NDVI:\t%f" % late_ndvi)
print("Percentage Difference:\t%f" % (((early_ndvi - late_ndvi) / early_ndvi) * 100))
