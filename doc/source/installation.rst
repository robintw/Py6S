Installation
================================

Recommended: Using conda
----------------------------
Py6S and all of its dependencies (including 6S itself) are available through the
``conda`` package manager on the ``conda-forge`` channel. This is by far the
easiest way to install Py6S, and is strongly recommended.

If you already have ``conda`` installed, then you can create a new environment containing Py6S and all
of its dependencies by running::

    $ conda create -n py6s-env -c conda-forge py6s

This will create a new environment called ``py6s-env``, and will then tell you how to 'activate'
the environment, which you should now do. You can now skip to `Testing Py6S`_.

If you don't already have ``conda`` installed then:

#. Install either `Miniconda <https://conda.io/miniconda.html>`_ or `Anaconda <https://www.anaconda.com/download>`_.
    These are two different distributions of Python, both of which include
    the ``conda`` package manager. Miniconda comes with the 'bare minimum' of Python, conda and
    a few essential libraries, whereas Anaconda comes with many libraries required for data science
    work in Python.

    Anaconda and Miniconda are available in Python 2 and Python 3 versions, although both of these can create
    'environments' using either version of Python. Py6S also works with both Python 2 and Python 3,
    although we recommend using Python 3.

    *If you don't know which one to choose, then choose Miniconda3.*

#. Open up a terminal window and create a new environment containing Py6S.
    To open up the command-line window, run a program called *Terminal* on OS X or Linux,
    and *Command Prompt* on Windows).

    In the terminal window, run::

        $ conda create -n py6s-env -c conda-forge py6s

    This will create a separate 'conda environment' for Py6S. In conda, environments are kept
    entirely separate, meaning that anything you install for Py6S won't affect any other Python
    installation you use on your system.

    You'll need to agree to the package installation plan that conda provides, and then it will
    download and install Py6S and its dependencies (including the underlying 6S model).

    If you want to use IPython or Jupyter (or any other python library) within this environment,
    then add them to the end of the installation command - for example::

        $ conda create -n py6s-env -c conda-forge py6s ipython Jupyter

#. Activate the environment by running the command shown at the end of the installation
    On Linux/OS X this is ``source activate py6s-env``.

    On Windows this is ``activate py6s-env``.

    Remember, you will need to do this **every** time before using Py6S.

You can now skip to `Testing Py6S`_.

Alternative: Manual installation
--------------------------------

Prerequisites
^^^^^^^^^^^^^

Executables
***********
* ``Python 2.7`` or greater
* ``6S v1.1`` (installation instructions below)

**NB: Py6S is an interface to 6S, not a replacement, so to use Py6S the 6S
executable MUST exist on your system.**

Python modules
**************
* ``nose``
* ``numpy``
* ``scipy``
* ``python-dateutil``
* ``matplotlib`` (optional: only used for plotting spectra)
* ``pysolar`` >=0.9 (optional: only required for setting the geometry from a location and time)
* ``pandas`` (optional: only required for importing AERONET data)
* ``ipython`` (recommended)

An easy way to sort all of this out is to use
`Anaconda <https://www.anaconda.com/download>`_ or the `Enthought Python
Distribution <http://enthought.com/products/epd.php>`_, either of which will install
Python plus many modules which are often used for scientific computing.

Installing 6S
^^^^^^^^^^^^^
6S is provided as a number of Fortran 77 source-code files from the
`6S website <http://6s.ltdri.org/>`_, and must be compiled for your
specific computer system. Detailed instructions are provided in the
sections below.

#. Download UNIX tools: (**Windows only**)

   #. We need to download the ``make`` and ``tar`` tools to allow us
      to install 6S. The easiest way to get these is through
      a project called GNUWin32. Go to the GnuWin32_ project and choose the
      setup link next to ``tar`` and ``make`` and download the files.

   #. Run the two executable files you just downloaded and work
      through the setup wizard for each, accepting the default
      options.

#. Install the Fortran compiler:

   :Windows: To compile the 6S code we will need a Fortran 77
             compiler. These are a little difficult to find, as most compilers
             are now based on the (more modern) Fortran 95 standard. However,
             for some reason 6S does not compile using the newer compilers, so
             we need to find a Fortran 77 compiler. The best place I've found
             to get one for Windows is:
             http://www.cse.yorku.ca/~roumani/fortran/ftn.htm.
             #. Download the ``FORT99.zip`` file, and extract it somewhere.

             #. Copy the ``G77`` folder to the root of the C drive (so that
                the folder is ``C:\G77``).

             #. Right-click on the **My Computer** icon on your desktop, or
                the Computer item on your Start Menu and select
                **Properties**.

             #. Choose the **Advanced System Settings** option on the
                left-hand side of the resulting window and then click the
                **Environment Variables** button in the next dialog.

             #. Scroll down in the bottom list box until you find a
                variable called ``PATH``. Click **Edit** and add the following
                string to the end of its contents::
                  C:\Program Files\GNUWin32\bin;C:\G77\bin

   :OS X: Install ``gfortran`` with Homebrew_.

          ::

             $ brew install gcc

   :Linux: This may already be installed in your system.  To find out,run::

              $ gfortran -v

           If you don't get an error, it is installed.  If not, install it
           using the standard installation method for your distribution. You
           can often do this via a GUI tool, such as Synaptic Package
           Manager, or via the command-line, for example::
             $ sudo apt-get install gfortran  # Debian/Ubuntu-based distributions or...
             $ sudo emerge gfortran           # Gentoo or...
             $ sudo pacman -S gfortran        # Arch or... etc.

#. Download the source code for 6SV1.1_.
    *Do not use the current available versions (v2.1 or v1.0Beta) from*
    *http://6s.ltdri.org/ as they are not yet supported*
    *by Py6S*

#. Extract the download:

   :Windows: Open the command window by opening the **Start Menu** and
             typing *'cmd'*.  In the terminal::
               $ MD C:\Users\robin\source
               $ MD C:\Users\robin\build\6SV\1.1
               $ MOVE C:\Users\robin\Downloads\6SV-1.1.tar C:\Users\robin\source
               $ CD C:\Users\robin\build\6SV\1.1
               $ tar -xvf C:\Users\robin\source\6SV-1.1.tar .
               $ CD 6SV1.1

   :Linux/OS X:

      ::

         $ mkdir source
         $ mv ~/Downloads/6SV-1.1.tar source/
         $ mkdir -p build/6SV/1.1
         $ cd build
         $ tar -xvf ../source/6SV-1.1.tar .
         $ cd 6SV1.1

#. Edit Makefile:

   :Windows: Browse to the 6SV1.1 folder in **Windows Explorer** (it
             should in your **Downloads** folder). Inside the folder
             you should find a file called ``Makefile``. Open the file
             by double-clicking on it, and selecting Notepad (*not
             Word*) when asked which program to open the file
             with. When the file has opened, find the text saying
             ``-lm`` (it will be near the end of the file) and delete
             it. Save the file.

   :Linux/OS X: The ``Makefile`` that comes with 6S expects to use the ``g77``
                compiler, so we need to instruct it to use ``gfortran``
                instead. Open the file called ``Makefile`` in an editor of your
                choice, for example::

                  $ nano Makefile

                Change the line::

                  FC      = g77 $(FFLAGS)

                to::

                  FC      = gfortran -std=legacy -ffixed-line-length-none -ffpe-summary=none $(FFLAGS)

                  (*Note:* The ``-ffpe-summary=none`` flag isn't available when using
                  GCC 4.8.4. Some people have had success leaving it out, but others
                  have found problems. Ideally use GCC > 4.8.4, but if that is impossible
                  then try without this flag.)

#. Compile 6S:

   #. Compile the source code: ``$ make``

   #. If no errors have been produced, then test the 6S executable by
      typing:

      :Windows: ``$ sixsV1.1.exe < ..\Examples\Example_In_1.txt``
      :Linux/OS X: ``$ sixsV1.1 < ../Examples/Example_In_1.txt``

      Note: on Windows, make sure you run this in the standard Command Prompt
      (cmd.exe), not Powershell (PowerCmd.exe).

   #. If this is working correctly you should see a number of screen's
      worth of output, finishing with something that looks like::
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

Using 6S
^^^^^^^^^

Once you have compiled 6S, you must place the executable (which is, by
default, called ``sixsV1.1`` or ``sixsV1.1.exe``) somewhere where Py6S can find it. The
best thing to do is place it somewhere within your system path, as defined by the ``PATH``
environment variable. There are three ways to do this:

* **Modify your system PATH to include the location of 6S:**
  To do this, leave 6S where it is (or place it anywhere else that you
  want) and then edit the ``PATH`` environment variable (see above) to include that
  folder. The method to do this varies by platform, but a quick Google
  search should show you how to accomplish this.

* **Move 6S to a location which is already in the PATH:**
  This is fairly simple as it just involves copying a file. Sensible
  places to copy to include ``/usr/local/bin`` (Linux/OS X) or
  ``C:\Windows\System32`` (Windows).

* **Link 6S to a location on your** ``PATH``:

  :Windows: ``$ MKLINK sixsV1.1.exe C:\Windows\System``
  :Linux/OS X: ``$ ln sixsV1.1 /usr/local/bin/sixs``

If it is impossible (for some reason) to point to the 6S executable
with ``PATH``, it is possible to specify the location manually when
running Py6S (see below).


Installing Py6S
^^^^^^^^^^^^^^^^^^

Installation from PyPI
***********************
The easiest way to install Py6S is from the Python Package Index
(PyPI; http://pypi.python.org/pypi). Simply open a command prompt and
type::
  $ pip install Py6S

If you get an error saying that ``pip`` cannot be found or is not
installed, simply run::
  $ easy_install pip
  $ pip install Py6S


Installation from a .egg file
******************************
Py6S is also distributed as a Python Egg file, with a name like
``Py6S-0.51-py2.7.egg``. You will need to choose the correct egg file
for your version of python. To find out your Python version run::

  $ python -V
  Python 2.7.2 -- EPD 7.1-2 (64-bit)

Then simply run the following code, which will install PySolar (required for some Py6S functions), and then Py6S itself::

  $ pip install PySolar
  $ easy_install <eggfile>

Where ``<eggfile>`` is the correct egg file for your Python version.

Testing Py6S
-------------

To check that Py6S can find the 6S executable::

  $ python
  >>> from Py6S import *
  >>> SixS.test()
  6S wrapper script by Robin Wilson
  Using 6S located at <PATH_TO_SIXS_EXE>
  Running 6S using a set of test parameters
  The results are:
  Expected result: 619.158000
  Actual result: 619.158000
  #### Results agree, Py6S is working correctly

This shows where the 6S executable that Py6S is using has been found
at <PATH_TO_SIXS_EXE>. If the executable cannot be found then it is
possible to specify the location manually (this is unlikely to be necessary
if you are using the ``conda``-based installation method)::

  $ python
  >>> from Py6S import *
  >>> SixS.test("C:\Test\sixsV1.1")

If you choose this method then remember to include the same path
whenever you instantiate the ``SixS`` class, as follows::

  >>> from Py6S import *
  >>> s = SixS("C:\Test\sixsV1.1")

To run the full test suite to verify that both 6S and Py6S have been
installed correctly (recommended)::

  $ python
  >>> import os.path
  >>> import Py6S; print(os.path.dirname(Py6S.__file__))
  <PATH_TO_PY6S_MODULE>
  >>> exit()
  cd <PATH_TO_PY6S_MODULE>
  $ py.test

.. _GnuWin32: http://gnuwin32.sourceforge.net/packages.html
.. _Homebrew: http://brew.sh
.. _6SV1.1: https://rtwilson.com/downloads/6SV-1.1.tar
