.. Py6S documentation master file, created by
   sphinx-quickstart on Thu Feb 16 12:07:44 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Py6S - A Python interface to 6S
================================

Py6S is a Python programming language interface to the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) Radiative Transfer Model. It allows you to run many 6S simulations using a simple Python syntax, rather than dealing with the rather cryptic 6S input and output files. As well as generally making it easier to use 6S, Py6S adds new features including:

* The ability to run many simulations easily and quickly, with no manual editing of input files
* The ability to run for many wavelengths and/or angles and easily plot the results
* The ability to import real-world data to parameterise 6S, from radiosonde measurements and AERONET sun photometer measurements

Py6S was originally created as part of my PhD, to allow me to easily run a number of 6S simulations - to perform sensitivity analyses, for example - but has now been extended to cover the entire range of 6S functionality. **Anything that can be done using the standard 6S model can be done through Py6S.** 

This is the index of the Py6S documentation. The pages below will introduce Py6S, show how to install it and show how to use the various features. If you need further help, or just want to send me some comments about Py6S, then visit the :doc:`support` page. If you use Py6S as part of some research you publish then please ensure you cite the first paper listed on the :doc:`publications` page.

The :doc:`releasenotes` give information on what has changed in recent releases, and the :doc:`roadmap` describes plans for future features.

Py6S is copyright Robin Wilson and the contributors listed `here <https://github.com/robintw/Py6S/blob/master/CONTRIBUTORS>`_, and is released under the `GNU Lesser General Public License <http://www.gnu.org/copyleft/lesser.html>`_.

.. toctree::
   :maxdepth: 2
  
   introduction
   audience
   installation
   quickstart
   sixs
   outputs
   params
   helpers
   casestudy
   
  
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

