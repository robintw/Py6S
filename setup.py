#!/usr/bin/env python
# This file is part of Py6S.
#
# Copyright 2012 Robin Wilson and contributors listed in the CONTRIBUTORS file.
#
# Py6S is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Py6S is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Py6S.  If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

reqs = ['pysolar', 'matplotlib', 'scipy']

setup(
        name                  = "Py6S",
        packages              = ['Py6S', 'Py6S.Params', 'Py6S.SixSHelpers'],
        requires              = reqs,
        install_requires      = reqs,
        version               = "1.6.0",
        author                = "Robin Wilson",
        author_email          = "robin@rtwilson.com",
        description           = ("""A wrapper for the 6S Radiative Transfer Model to make it easy to run simulations
        with a variety of input parameters, and to produce outputs in an easily processable form."""),
        license               = "BSD",
        url                   = "http://packages.python.org/Py6S",
        long_description      = """Introduction 
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
  print s.outputs.pixel_reflectance, s.outputs.pixel_radiance, s.outputs.direct_solar_irradiance
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

I'm very interested in receiving feedback, bug reports and feature suggestions, so please email me at robin@rtwilson.com.""",
        classifiers           =[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python"
        
        ],
)
