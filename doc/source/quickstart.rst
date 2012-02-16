Quick Start
================================

Now you've installed Py6S, this section will give you a brief guide on how to use it.

A first run
-----------

The :class:`.SixS` class is at the heart of Py6S. It has methods and attributes that allow you to set 6S parameters, run 6S and then view the outputs.

Py6S sets every 6S parameter to a sensible default, so the simplest possible code just uses the default values and prints an output::

  from Py6S import * # Import all of the Py6S code
  s = SixS() # Create a SixS object called s (used as the standard name by convention)
  s.run() # Run the 6S model
  print s.outputs.pixel_radiance # Print the pixel radiance calculated by 6S
  
Of course, this isn't particularly helpful as the defaults I've chosen probably aren't the parameters that you want to use for your simulation, and you may not be interested in the calculated pixel radiance. The sections below will explain how to alter this simple program to produce more useful results.

Setting parameters
------------------

We'll start with an example, and then explain the details::

  from Py6S import *
  s = SixS()
  s.atmos_profile = AtmosProfile.PredefinedType(AtmosProfile.Tropical)
  s.wavelength = Wavelength.Wavelength(0.357)
  s.run()
  print s.outputs.pixel_radiance

You can see here that we have changed the atmospheric profile to a Tropical profile, and changed the wavelength that we are using for the simulation to 0.357 micrometres. If you run this you'll find that the resulting pixel radiance has changed quite significantly.

Of course, there are lots of other parameters we can change, summarised in the table below:

====================== ============================================================== =========================================================
SixS Parameter           Description                                                    Possible values
====================== ============================================================== =========================================================
``atmos_profile``      Atmospheric profile (pressure, water vapour, ozone etc)        Any outputs from :class:`.AtmosProfile`
``aero_profile``       Aerosol profile (types, distributions etc)                     Any outputs from :class:`.AeroProfile`
``ground_reflectance`` Ground reflectance (Homogeneity, BRDF etc.)                    Any outputs from :class:`.GroundReflectance`
``geometry``           Viewing/Illumination geometry (manual or satellite-specific)   A ``Geometry*`` class, for example :class:`.GeometryUser`
``aot550``             Aerosol Optical Thickness at 550nm                             Floating point number
``visibility``         Visibility in km                                               Floating point number
``atmos_corr``         Atmospheric correction settings (yes/no, reflectances)         Any outputs from :class:`.AtmosCorr`
====================== ============================================================== =========================================================

As you can see, the parameter and class names are designed to be fairly self-explanatory. Using the details from above, a more advanced parameterisation is shown below::

  from Py6S import *
  s = SixS()
  s.atmos_profile = AtmosProfile.UserWaterAndOzone(3.6, 0.9) # Set the atmosphere profile to be based on 3.6cm of water and 0.9cm-atm of ozone
  s.wavelength = Wavelength.Wavelength(Wavelength.LANDSAT_TM_B3) # Set the wavelength to be that of the Landsat TM Band 3 - includes response function 
  s.ground_reflectance = GroundReflectance.HomogeneousWalthall(1.08, 0.48, 4.96, 0.5) # Set the surface to have a BRDF approximated by the Walthall model
  s.geometry = GeometryLandsat_TM()
  s.geometry.month = 7
  s.geometry.day = 14
  s.geometry.gmt_decimal_hour = 7.75
  s.geometry.latitude = 51.148
  s.geometry.longitude = 0.307
  s.run()
  print s.outputs.pixel_radiance
  
This is far more detailed, but should be self-explanatory given the comments and the table above. Far more details about the individual parameterisations are available in their documentation pages.

The real power of Py6S comes when you combine the paramterisation abilities of Py6S with the standard Python programming constructs. For example, you can easily loop over a number of parameter values and produce the outputs for each of them::

  from Py6S import *
  s = SixS()
  
  for param in [AtmosProfile.Tropical, AtmosProfile.MidlatitudeSummer, AtmosProfile.MidlatitudeWinter]:
    s.atmos_profile = AtmosProfile.PredefinedType(param)
    s.run()
    print s.outputs.pixel_radiance
    
You can see that in this instance the change in pixel radiance over different atmospheric profiles is fairly low (< 0.8).

That's it for the quick guide to setting parameters - more details, particularly on running sets of parameters using helper methods, 

Accessing outputs
-----------------
The outputs from the 6S model are available under the ``s.outputs`` attribute. The outputs are actually stored as dictionaries, and the main set of outputs can be printed (and saved) from the ``s.outputs.values`` attribute. For example::

  from Py6S import *
  s = SixS()
  s.run()
  print s.outputs.values
  
However, it's normally more useful to access individual outputs. This can be done using the standard Python dictionary access methods - for example, ``print s.outputs.values['pixel_radiance']``, but it is generally easy to do this by appending the output name to ``s.outputs.``. For example::

  from Py6S import *
  s = SixS()
  s.run()
  print s.outputs.pixel_radiance
  print s.outputs.environmental_irradiance
  print s.outputs.total_gaseous_transmittance

The outputs stored under ``s.outputs.values`` are the main outputs of 6S provided on the first two 'screenfulls' of raw 6S output. The tables showing the integrated values of various transmittances (rayleigh, water, ozone etc) are stored under the ``s.outputs.trans`` dictionary as instances of the :class:`Transmittance` class. This allows the easy storage of the three different transmittances: downward, upward and total. Again, rather than dealing with the dictionary directly, courtesy methods are provided, for example::

  from Py6S import *
  s = SixS()
  s.run()
  print s.outputs.transmittance_rayleigh_scattering
  print s.outputs.transmittance_rayleigh_scattering.downward
  print s.outputs.transmittance_rayleigh_scattering.upward
  print s.outputs.transmittance_rayleigh_scattering.total
  print s.outputs.transmittance_water