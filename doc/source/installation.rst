Installation
================================

Prerequisites
-------------
Before starting the installation process, ensure that you have a working Python installation with the ``numpy`` module installed. It will also be helpful
to have the IPython installed for interactive testing of Py6S. An easy way
to sort all of this out is to use the Enthought Python Distribution (see http://enthought.com/products/epd.php) which will install Python and NumPy along
with many other useful modules and tools.

Installing 6S   
-------------
Py6S is an interface to 6S, not a replacement, so to use Py6S the 6S executable must already exist on your system.
6S is provided as a number of Fortran 77 source-code files from http://6s.ltdri.org/, and must be compiled for your specific computer system. Detailed compilation
instructions are beyond the scope of this article, but in brief:

1. Get hold of a Fortran 77 compiler for your platform. For Windows try Fort99 (http://www.cse.yorku.ca/~roumani/fortran/ftn.htm) or Cygwin (http://www.cygwin.com/), for OS X try the g77 compiler from the HPC Mac OSX project (http://hpc.sourceforge.net/) and for Linux you should be able to install g77 or equivalent from your package manager.
2. Install the compiler, move to the directory containing the 6S .f files and run ``make``
3. Check the resulting executable is working correctly by passing it one of the example input files, for example::
  > ./sixsV1.1 < ../Examples/Example_In_1.txt

If this is working correctly you should see a number of screen's worth of output, finishing with something that looks like::

  *******************************************************************************
  *                        atmospheric correction result                        *
  *                        -----------------------------                        *
  *       input apparent reflectance            :    0.100                      *
  *       measured radiance [w/m2/sr/mic]       :   38.529                      *
  *       atmospherically corrected reflectance                                 *
  *       Lambertian case :      0.22187                                        *
  *       BRDF       case :      0.22187                                        *
  *       coefficients xa xb xc                 :  0.00685  0.03870  0.06820    *
  *       y=xa*(measured radiance)-xb;  acr=y/(1.+xc*y)                         *
  *******************************************************************************
  
Once you have compiled 6S, you must place the executable (which is, by default, called ``sixsV1.1``) somewhere where Py6S can find it. The best thing to do is
place it somewhere within your system path, as defined by the PATH environment variable. There are two ways to do this:

* **Modify your system path to include the location of 6S:** To do this, leave 6S where it is (or place it anywhere else that you want) and then edit the PATH environment variable to include that folder. The method to do this varies by platform, but a quick Google search should show you how to accomplish this.
* **Move 6S to a location which is already in the path:** This is fairly simple as it just involves copying a file. Sensible places to copy to include ``/usr/bin`` (on Linux or OS X) and ``C:\Windows\System32`` on Windows.

If it is impossible (for some reason) to place the 6S executable on the PATH it is possible to specify the location manually when running Py6S (see below).

Installing Py6S
---------------

Installation from PyPI
^^^^^^^^^^^^^^^^^^^^^^

.. warning::
  This method of installing Py6S will not work at the moment, as the code has not been uploaded to PyPI yet. Please use one of the methods below instead.

The easiest way to install Py6S is from the Python Package Index (PyPI; http://pypi.python.org/pypi). Simply open a command prompt and type::

  > pip install Py6S
  
If you get an error saying that ``pip`` cannot be found or is not installed, simply run::

  > easy_install pip
  
and then perform the installation as above.

Installation from a .egg file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Py6S is also distributed as a Python Egg file, with a name like ``Py6S-0.51-py2.7.egg``. You will need to choose the correct egg file for your version of python. To find out your Python version run::

  > python -V
  Python 2.7.2 -- EPD 7.1-2 (64-bit)
  
Then simply run::

  > easy_install <eggfile>
  
Where ``<eggfile>`` is the correct egg file for your Python version.

Testing Py6S
------------
To check that both 6S and Py6S have been installed correctly, and that Py6S can find the 6S executable, run ``ipython`` from the command line, and then run the following commands::

  from Py6S import *
  SixS.test()
  
The output should look like this::

  6S wrapper script by Robin Wilson
  Using 6S located at C:\_Work\Py6S\6S\sixs.exe
  Running 6S using a set of test parameters
  The results are:
  Expected result: 619.158000
  Actual result: 619.158000
  #### Results agree, Py6S is working correctly
  
This shows where the 6S executable that Py6S is using has been found (``C:\_Work\Py6S\6S\sixs.exe`` in this case). If the executable cannot be found then it is possible to specify the locationmanually::

  from Py6S import *
  SixS.test("C:\Test\sixsV1.1")

If you choose this method then remember to include the same path whenever you instantiate the class:`.SixS` class, as follows::

  from Py6S import *
  s = SixS("C:\Test\sixsV1.1")