Helper methods
================================

The SixSHelpers module contains a number of helper functions that improve the ease-of-use of Py6S. These include functions to set 6S parameters from various external data sources, as well as functions to make it easy to produce wavelength and BRDF plots from 6S runs.

For example, the following code runs 6S simulations across the Visible-Near Infrared wavelength range and plots the results::

  from Py6S import *
  s = SixS()
  s.aero_profile = AeroProfile.PredefinedType(AeroProfile.Maritime)
  wavelengths, values = SixSHelpers.Wavelengths.run_vnir(s, output_name='pixel_radiance')
  SixSHelpers.Wavelengths.plot_wavelengths(wavelengths, values, 'Pixel Radiance (W/m^2)')

Wavelengths
-----------
The Wavelengths class contains functions to run 6S over a number of wavelength ranges.

.. autoclass:: Py6S.SixSHelpers.Wavelengths
  :members: