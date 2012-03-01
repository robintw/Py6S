Helper methods
================================

The SixSHelpers module contains a number of helper functions that improve the ease-of-use of Py6S. These include functions to set 6S parameters from various external data sources, as well as functions to make it easy to produce wavelength and BRDF plots from 6S runs.

Running for many wavelengths
----------------------------
The Wavelengths class contains functions to run 6S over a number of wavelength ranges.

For example, the following code runs 6S simulations across the Visible-Near Infrared wavelength range and plots the results::

  from Py6S import *
  s = SixS()
  s.aero_profile = AeroProfile.PredefinedType(AeroProfile.Maritime)
  wavelengths, values = SixSHelpers.Wavelengths.run_vnir(s, output_name='pixel_radiance')
  SixSHelpers.Wavelengths.plot_wavelengths(wavelengths, values, 'Pixel Radiance (W/m^2)')

Similar functions exist to run across the whole 6S wavelength range (:meth:`.run_whole_range`), and to run for all bands for the various sensors supported in 6S (for example, :meth:`.run_landsat_tm`, :meth:`.run_modis` and :meth:`.run_aatsr`). It should be noted that bands which are outside of the 6S wavelength range (0.2-4.0um) will not be simulated.
  
.. autoclass:: Py6S.SixSHelpers.Wavelengths
  :members:

Running for many angles
-----------------------
The Angles class contains functions to run 6S over a number of different angles, which are particularly useful when dealing with surfaces with a modelled-BRDF.

For example, the following code runs 6S simulations for many view zenith and azimuth angles and plots a polar contour plot of the resulting reflectance distribution::
  
    s = SixS()
    s.ground_reflectance = GroundReflectance.HomogeneousWalthall(0.48, 0.50, 2.95, 0.6)
    s.geometry.solar_z = 30
    s.geometry.solar_a = 0
    SixSHelpers.Angles.run_and_plot_360(s, 'view', 'pixel_reflectance')
      
.. autoclass:: Py6S.SixSHelpers.Angles
  :members:

Importing atmospheric profiles from radiosonde data
---------------------------------------------------
6S is provided with a number of pre-defined atmospheric profiles, such as Midlatitude Summer, Tropical and Subarctic Winter. However, it also possible to parameterise 6S using data acquired from radiosonde (weather balloon) measurements.

The main function in this class :meth:`.import_uow_radiosonde_data` imports radiosonde data from the University of Wyoming's radiosonde data website to 6S, allowing accurate parameterisation based on real-world measurements.

.. autoclass:: Py6S.SixSHelpers.Radiosonde
  :members: