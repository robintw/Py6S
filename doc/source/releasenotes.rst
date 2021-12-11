Release Notes
-------------

Details on the changes in recent versions of Py6S can be found below. More detailed information is available by examining the `commit history <https://github.com/robintw/Py6S/commits/master/>`_ via Github.

1.9.1 (11th December 2021)
^^^^^^^^^^^^^^^^^^^^^^^^^^
* Add extraction of polarization outputs - such as apparent polarized radiance/reflectance

1.9.0 (8th June 2021)
^^^^^^^^^^^^^^^^^^^^^
* **Breaking change:** Py6S's optional dependencies have changed. The Geometry.from_time_and_location function requires the pysolar library.
  Previously, Py6S required version 0.6 of the library. We now require version 0.9 of pysolar.
* **Breaking change:** The Geometry.from_time_and_location function now requires that date-time values are given in ISO 8601 format - ie.
  YYYY-MM-DD HH:MM:SS - and must be in the UTC time zone.
* The matplotlib dependency is now optional, and will not be installed by default when running ``pip install Py6S``
* Py6S now gives an error if you attempt to use it with version 2.1 of 6S. Currently Py6S only supports 6SV 1.1, but work on supporting
  version 2.1 will hopefully commence soon.
* There have been significant improvements to the code style and quality across Py6S, to make future alterations easier

1.8.2 (7th June 2021)
^^^^^^^^^^^^^^^^^^^^^
* Add extraction of water reflectance components (foam, water, glint) when configured with the ocean ground reflectance model

1.8.1 (9th February 2021)
^^^^^^^^^^^^^^^^^^^^^^^^^
* Fixed bug when running Py6S with numpy 1.20.0

1.8.0 (23rd April 2020)
^^^^^^^^^^^^^^^^^^^^^^^
* Removed support for Python 2, and updated all docs and code examples to be Python 3 compatible
* Fixed issues when running with conda-forge `sixs` package on Mac OS X, where floating point issues caused the run method to give an error
* Updated Sentinel 2A and 2B MSI spectral response functions with new data from European Space Agency
* Add Sentinel 3 A and B OLCI and SLSTR spectral response functions
* Updated all usages of pandas to work with pandas 1.0
* Fix issue with AerosolDistribution and UserProfile classes, where values could accidentally be shared between instances
* Add error checking to custom filter function specification
* Add check for whether 6S provided a reasonable amount of output, raising an error otherwise
* Updated plot functions to take `figsize` as an argument
* Fixed importing of malformed UoW Radiosonde data
* Updated various parts of the documentation to be clearer

1.7.2 (18th Oct 2018)
^^^^^^^^^^^^^^^^^^^^^
* Fixed similar thread pool bug with `SixSHelpers.Angles.run_360` and
  `SixHelpers.Angles.run_principal_plane`. Both now close the thread pool, allowing them to be run
  many times with no problems.

1.7.1 (18th Oct 2018)
^^^^^^^^^^^^^^^^^^^^^
* Fixed bug with all `SixSHelpers.Wavelengths.run_XXX` functions which weren't closing a thread pool and
  thus could fail if run multiple times in succession.
* Fixed bug with `GroundReflectance.HeterogeneousLambertian` where the reflectances are given as arrays of
  wavelengths and reflectances. This previously resulted in an error, it now works correctly.

1.7 (31st Jan 2017)
^^^^^^^^^^^^^^^^^^^
* Added new spectral response functions
    - Sentinel 2 Multispectral Instrument (MSI) as `PredefinedWavelengths.S2A_MSI_xx`, and with a `run_s2a_msi` function
    - Sentinel 3 Ocean and Land Colour Instrument (OLCI) as `PredefinedWavelengths.S3A_OLCI_xx`, and with a `run_s3a_olci` function
    - Accurate MODIS bands, based on actual measurements of the MODIS sensor on the Aqua and Terra satellites and taking into
      account differences between the sensors. Includes the ocean bands. Provided as `PredefinedWavelengths.ACCURATE_MODIS_TERRA_x`
      and the same for Aqua, with run functions `run_aqua` and `run_terra`.
* Changed radiosonde import to manage missing values properly
* Fixed tab-completion on Python 3
* Added range checking for the altitude parameter to give a sensible error if ground altitudes > 100km or < 0km are given.
* Improved various parts of the documentation

1.6.2 (13th Jan 2016)
^^^^^^^^^^^^^^^^^^^^^
* Fixed bug with all SixSHelpers.Wavelengths.run_xxx functions. They now work with extracting outputs like transmittance_total_scattering.total

1.6.1 (9th July 2015)
^^^^^^^^^^^^^^^^^^^^^
* Added Pleiades spectral response functions, so simulations can now be run using Pleiades wavelengths

1.6 (14th June 2015)
^^^^^^^^^^^^^^^^^^^^
* Py6S now works properly with Python 3. This was meant to be the case as of v1.5, but various things seemed to go wrong. Thanks to Pete Bunting and Dan Clewley for help fixing this.
* Made setup.py script executable (thanks Matthew Hanson)
* Fixed unusable Homogeneous User Defined BRDF specification (thanks J Gomez-Dans)
* Fixed requirement for pysolar, to deal with upstream changes
* Added many more tests

1.5.4 (16th July 2014)
^^^^^^^^^^^^^^^^^^^^^^
Fixed minor error on install (didn't affect any functionality)

1.5.3 (16th July 2014)
^^^^^^^^^^^^^^^^^^^^^^
* Added RapidEye bands to PredefinedWavelengths

1.5.2 (8th July 2014)
^^^^^^^^^^^^^^^^^^^^^
* Added extraction of two outputs that had been missed out before: the integrated filter function, and the integrated solar spectrum.

1.5.1 (3rd July 2014)
^^^^^^^^^^^^^^^^^^^^^
* Added an option to write_input_file to allow a filename to be given - allowing users to easily export standard 6S input files from Py6S.

1.5.0 (22nd April 2014)
^^^^^^^^^^^^^^^^^^^^^^^
* First release compatible with Python 3. All Py6S functionality should work fine on Python 3 - please contact me if there are any problems.
* Added Landsat 8 spectral response functions, and a run_landsat_oli function.

1.4.2 (20th Feb 2014)
^^^^^^^^^^^^^^^^^^^^^
* Fixed bug in the AERONET import routine which meant that ambiguous dates would be imported as MM/DD/YYYY rather than DD/MM/YYYY as specified in the documentation (thanks Marcin)

1.4.1 (22nd Jan 2014)
^^^^^^^^^^^^^^^^^^^^^
* Fixed a minor bug which means that running for multiple wavelengths/angles after having already run the SixS object manually would crash

1.4.0 (21st Jan 2014)
^^^^^^^^^^^^^^^^^^^^^
* Added parallel processing support for the methods in SixSHelpers that run for multiple wavelengths and multiple angles. This will significantly speed up these runs: on a dual-core machine they should take approximately half the time, and the speedup will be even better on quad-core or eight-core computers. The parallelisation abilities (including the speedup) may be improved in the future, but this should be a significant improvement for now.
* Added produce_debug_report() function to the SixS object. This gives all of the debugging information that I would need when helping to fix a problem - so please run this and send me the output whenever problems occur.

1.3.1 (15th Jan 2014)
^^^^^^^^^^^^^^^^^^^^
* Added proper error handling for dealing with erroneous 6S output, now things shouldn't crash if 6S produces strange results
* Bugfix for error when setting custom altitudes in certain situations
* Added more detailed error messages for failure to import AERONET data
* Bugfix for the specification of geometry parameters within the 6S input file - now more accurate
* Improvements to documentation (typos, clearer explanations etc)
* Added CITATION file to explain how to cite Py6S

1.3 (6th April 2013)
^^^^^^^^^^^^^^^^^^^^
* Fixed a number of bugs relating to geometry specification (thanks Matthew Hanson).
* Significantly improved the code for importing AERONET data - this is now far less likely to go wrong, and more intelligent about what measurements it takes.

1.2.4 (28th Feb 2013)
^^^^^^^^^^^^^^^^^^^^^
Bugfix release to fix issue with importing AERONET data from instruments which don't take measurements at 500nm. Importing should now work for any AERONET data, with a warning raised if the instrument doesn't have a band within 70nm of 550nm.

1.2.3 (10th Feb 2013)
^^^^^^^^^^^^^^^^^^^^^
Bugfix release to fix issue with importing geometry details from time and location, due to issues with importing PySolar.

1.2.2 (4th Jan 2013)
^^^^^^^^^^^^^^^^^^^^
Bugfix release to fix issue with installation not finding README.rst on some systems.

1.2.1 (3rd Jan 2013)
^^^^^^^^^^^^^^^^^^^^
Bugfix release to fix an issue with the BRDF options in :py:class:`Py6S.GroundReflectance`, as none of them worked any more due to an issue with the features that were added in v1.2.

1.2 (2nd Jan 2013)
^^^^^^^^^^^^^^^^^^
Added ability to import a spectrum from a spectral library (USGS or ASTER spectral libraries are currently supported) and then specify it as the ground reflectance. See :py:class:`Py6S.SixSHelpers.Spectra` and :py:class:`Py6S.GroundReflectance`.

This also means that anything that can produce a 2D array with wavelengths (column 0, in micrometres) and reflectances (column 1) can be used to set the ground reflectance. For example, the Python interface to the ProSAIL model (`PyProSAIL <https://pyprosail.readthedocs.org/en/latest/>`_) can do this, and thus outputs from PyProSAIL can easily be used with 6S (see `here <https://pyprosail.readthedocs.org/en/latest/#using-with-py6s>`_ for more detailed instructions).

1.1.1 (18th Oct 2012)
^^^^^^^^^^^^^^^^^^^^^
Fixed bug which caused Py6S to crash when performing atmospheric correction on Linux (Thanks Vincent!)

1.1 (11th August 2012)
^^^^^^^^^^^^^^^^^^^^^^
* Updated code for running for multiple wavelengths to make it far easier to maintain
* Fixed bug with user-defined aerosol profile

1.0
^^^
This is the first public release of Py6S, which includes all of the functionality detailed in the documentation.
