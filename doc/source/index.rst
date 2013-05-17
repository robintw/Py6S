Py6S - A Python interface to 6S
================================

Py6S is a interface to the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) atmospheric Radiative Transfer Model through the Python programming language. It allows you to run many 6S simulations using a simple Python syntax, rather than dealing with the rather cryptic 6S input and output files. As well as generally making it easier to use 6S, Py6S adds a number of new features including:

* The ability to run many simulations easily and quickly, with no manual editing of input files
* The ability to run for many wavelengths and/or angles and easily plot the results
* The ability to import real-world data to parameterise 6S, such as radiosonde measurements, AERONET sun photometer measurements and ground reflectance spectra from spectral libraries

Py6S was originally created as part of my PhD, to allow me to easily run a number of 6S simulations - to perform sensitivity analyses, for example - but has now been extended to cover the entire range of 6S functionality. **Anything that can be done using the standard 6S model can be done through Py6S.** 

If you've just arrived here for the first time then you might like to read the :doc:`introduction` and :doc:`audience` pages to see whether Py6S is suitable for your needs, and then follow the :doc:`installation` instructions and then the :doc:`quickstart` guide. The `Py6S posts <http://blog.rtwilson.com/category/my-software/py6s/>`_ on my blog may also be of interest to you, as these explain various features of Py6S using case studies and example code. Full documentation of every function in Py6S can be accessed from the Table of Contents below.

If you need further help, or just want to send me some comments about Py6S, then visit the :doc:`support` page, where you will find details of the Py6S mailing list. If you use Py6S as part of some research you publish then you **must** cite the first paper listed on the :doc:`publications` page.

Py6S is fully-working, but also under active development. The :doc:`releasenotes` give information on what has changed in recent releases, and the :doc:`roadmap` describes plans for future features.

Py6S is copyright Robin Wilson and the contributors listed `here <https://github.com/robintw/Py6S/blob/master/CONTRIBUTORS>`_, and is released under the `GNU Lesser General Public License <http://www.gnu.org/copyleft/lesser.html>`_. The code is available at `GitHub <http://github.com/robintw/py6s>`_

Table of Contents
==================

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
   support
   releasenotes
   roadmap
   publications
   
  
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

