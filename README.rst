.. image:: https://travis-ci.org/robintw/Py6S.svg?branch=master
    :target: https://travis-ci.org/robintw/Py6S
.. image:: https://coveralls.io/repos/github/robintw/Py6S/badge.svg
    :target: https://coveralls.io/github/robintw/Py6S

Introduction 
-------------
Py6S is a Python interface to the 6S Radiative Transfer Model. It allows you to run many 6S simulations using a
simple Python syntax, rather than dealing with the rather cryptic 6S input and output files. As well as generally
making it easier to use 6S, Py6S adds some new features:

* The ability to run many simulations easily and quickly, with no manual editing of input files
* The ability to run for many wavelengths and/or angles and easily plot the results
* The ability to import real-world data to parameterise 6S, from radiosonde measurements and AERONET sun photometer measurements

Py6S has been designed to be easy to use, and to work on the 'principle of least surprise'. Far more details are available in the rest of
this documentation, but a quick code example should give you an idea of what Py6S can do::

  # Import the Py6S module
  from Py6S import *
  # Create a SixS object
  s = SixS()
  # Set the wavelength to 0.675um
  s.wavelength = Wavelength(0.675)
  # Set the aerosol profile to Maritime
  s.aero_profile = AeroProfile.PredefinedType(AeroProfile.Maritime)
  # Run the model
  s.run()
  # Print some outputs
  print(s.outputs.pixel_reflectance, s.outputs.pixel_radiance, s.outputs.direct_solar_irradiance)
  # Run the model across the VNIR wavelengths, and plot the result
  wavelengths, results = SixSHelpers.Wavelengths.run_vnir(s, output_name='pixel_radiance')
  SixSHelpers.Wavelengths.plot_wavelengths(wavelengths, results, "Pixel radiance ($W/m^2$)")
  
This will produce the results shown below::

  0.283 112.095 667.589
  
Followed by an image containing a graph showing the result for each wavelength.

To use Py6S you will also need to compile and install the 6S executable. Please follow the installation instructions in the `documentation <http://py6s.readthedocs.org>`_ to find out how to do this on Windows, OS X or Linux.

Py6S was described in a `journal article <https://py6s.readthedocs.org/en/latest/publications.html>`_ which should be referenced if Py6S is used for producing outputs for a scientific report/publication.

This project was written as part of my PhD at the University of Southampton. The code is open-source,
released under the LGPL license, and is available at `Github <http://github.com/robintw/py6s>`_.

I'm very interested in receiving feedback, bug reports and feature suggestions, so please email me at robin@rtwilson.com.
