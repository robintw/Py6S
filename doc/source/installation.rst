Installation
================================

Prerequisites
-------------
Before starting the installation process, ensure that you have a working Python installation with the following modules installed:

* ``numpy``
* ``scipy``
* ``matplotlib``
* ``python-dateutil``
* ``pysolar``

It will also be helpful to have the `IPython <http://ipython.org/>`_ installed for interactive testing of Py6S.

An easy way to sort all of this out is to use the `Enthought Python Distribution <http://enthought.com/products/epd.php>`_ which will install Python plus many modules which are
often used for scientific computing, along with many tools.

Compiling 6S   
-------------
Py6S is an interface to 6S, not a replacement, so to use Py6S the 6S executable must already exist on your system.
6S is provided as a number of Fortran 77 source-code files from the `6S website <http://6s.ltdri.org/>`_, and must be compiled for your specific computer system. Detailed instructions are provided in the sections below.

Windows
^^^^^^^^
These instructions were written based on testing with Windows 7, but should work with any version of Windows since Windows XP.

1. Download the 6S source code from http://6s.ltdri.org/. Choose *Download 6S* then *6SV1.1* and download the `.tar` file.
2. We need to download the ``make`` and ``tar`` tools to allow us to install 6S. The easiest way to get these is through a project called GNUWin32. Go to http://gnuwin32.sourceforge.net/packages.html and choose the setup link next to ``tar`` and ``make`` and download the files.
3. Run the two executable files you just downloaded and work through the setup wizard for each, accepting the default options.
4. To compile the 6S code we will need a Fortran 77 compiler. These are a little difficult to find, as most compilers are now based on the (more modern) Fortran 95 standard. However, for some reason 6S does not compile using these compilers, so we need to find a Fortran 77 compiler. The best place I've found to get one for Windows is http://www.cse.yorku.ca/~roumani/fortran/ftn.htm. Download the ``FORT99.zip`` file, and extract it somewhere. Copy the ``G77`` folder to the root of the C drive (so that the folder is ``C:\G77``).
5. We now need to edit the Windows path so that we can easily call the compiler and other tools. To do this, right-click on the My Computer icon on your desktop, or the Computer item on your Start Menu and select ``Properties``. Choose the ``Advanced System Settings`` option on the left-hand side of the resulting window and then click the ``Environment Variables`` button in the next dialog. Now scroll down in the bottom list box until you find a variable called ``PATH``. Click `Edit` and add the following string to the end of its contents::

    C:\Program Files\GNUWin32\bin;C:\G77\bin`

6. Open the command window by opening the start menu and typing ``cmd``.
7. Use the ``cd`` command to move to the folder where the .tar file you downloaded in step 1 is located, for example::

    cd C:\Users\robin\Downloads
    
8. Run the following commands, one after each other::

    tar -xvf 6SV-1.1.tar
  	cd 6SV1.1
    
#. Browse to the 6SV1.1 folder in Windows Explorer (it should in your Downloads folder). Inside the folder you should find a file called ``Makefile``. Open the file by double-clicking on it, and selecting Notepad when asked which program to open the file with. When the file has opened, find the text saying ``-lm`` (it will be near the end of the file) and delete it. Save the file.


#. Switch back to the command window and run the following command::

    make

9. If no errors have been produced, then test the 6S executable by typing::

    sixsV1.1 < ..\Examples\Example_In_1.txt

10. If this is working correctly you should see several screen's worth of output, finishing with something that looks like::

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
      
OS X
^^^^^^^^^^^^
These instructions were written based on testing with Mac OS X 10.7 (Lion), but should work with previous (and later) versions.

1. Download the 6S source code from http://6s.ltdri.org/. Choose *Download 6S* then *6SV1.1* and download the `.tar` file.

2. You will need to have ``gcc`` installed to compile 6S. If you already have the XCode developement environment for OS X installed then you've already got GCC, if not, go to https://github.com/kennethreitz/osx-gcc-installer/ and choose *Option 1: Downloading Pre-Built Binaries* and download the appropriate file for your version of OS X. Double-click the file to run it, and follow through the installer.

3. Download the f77 compiler from http://hpc.sourceforge.net/. You should choose one of the binary download links under the g77 3.4 heading. If you're not sure which binary you require then choose the Intel version, as that is what most modern Macs use.

4. Open the Terminal (Applications->Utilities->Terminal) and type the following commands (this assumes the files you downloaded above are located in your Downloads folder, and you will need to enter your password when prompted)::

    cd ~/Downloads
    sudo tar -xvf g77-bin.tar -C /

5. Now move Run the following commands, one after each other::

    tar -xvf 6SV-1.1.tar
  	cd 6SV1.1
  	make

#. If no errors have been produced, then test the 6S executable by typing::

    sixsV1.1 < ../Examples/Example_In_1.txt

#. If this is working correctly you should see a number of screen's worth of output, finishing with something that looks like::

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

Linux
^^^^^
Part of the problem with installation instructions for Linux is that there are so many distributions of Linux available, and they all
do things slightly differently. Therefore, the instructions below will be a bit more general than those above, but you should be able to
work out what to do.

1. Download the 6S source code from http://6s.ltdri.org/. Choose *Download 6S* then *6SV1.1* and download the `.tar` file.

#. You need to install ``gfortran`` - the GNU Fortran compiler. This may already be installed in your system - you can check by typing ``gfortran -v`` in a terminal, if you don't get an error, then it is installed. If not, install it using the standard installation method for your distribution. You can often do this via a GUI tool, such as Synaptic Package Manager, or via the command-line, for example::

    # For Debian/Ubuntu-based distributions
    sudo apt-get install gfortran
    # For Gentoo
    sudo emerge gfortran
    # For Arch
    sudo pacman -S gfortran

#. Extract the source code from the .tar file you downloaded::

    cd ~/Downloads (or wherever you put the file)
    tar -xvf 6SV-1.1.tar
    cd 6SV1.1

#. The ``Makefile`` that comes with 6S expects to use the ``g77`` compiler, so we need to instruct it to use ``gfortran`` instead. Open the file called ``Makefile`` in an editor of your choice, for example::

    nano Makefile
  
#. Change the line which contains::

    FC      = g77 $(FFLAGS)
  
#. to::
  
    FC      = gfortran -ffixed-line-length-132 -freal-loops $(FFLAGS)
  
#. Exit the editor and return to the command line.

#. Run ``make``

#. If no errors have been produced, then test the 6S executable by typing::

    sixsV1.1 < ../Examples/Example_In_1.txt

#. If this is working correctly you should see a number of screen's worth of output, finishing with something that looks like::

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


Installing 6S
-------------

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
  
Where ``<eggfile>`` is the correct egg file for your Python version. You will need to do this twice: once for ``Py6S-xxx.egg`` and once for ``Pysolar-xxx.egg``.

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

If you choose this method then remember to include the same path whenever you instantiate the :class:`.SixS` class, as follows::

  from Py6S import *
  s = SixS("C:\Test\sixsV1.1")