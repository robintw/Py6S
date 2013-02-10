Release Notes 
-------------

Details on the changes in recent versions of Py6S can be found below. More detailed information is available by examining the `commit history <https://github.com/robintw/Py6S/commits/master/>`_ via Github.

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