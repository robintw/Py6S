Compiling and installing 6S
================================

Windows
-------------
These instructions were written based on testing with Windows 7, but should work with any version of Windows since Windows XP.

 1. Download the 6S source code from http://6s.ltdri.org/. Choose *Download 6S* then *6SV1.1* and download the `.tar` file.
 2. We need to download the ``make`` and ``tar`` tools to allow us to install 6S. The easiest way to get these is through a project called GNUWin32. Go to http://gnuwin32.sourceforge.net/packages.html and choose the setup link next to ``tar` and ```make`` and download the files.
 3. Run the two executable files you just downloaded and work through the setup wizard for each, accepting the default options.
 4. To compile the 6S code we will need a Fortran 77 compiler. These are a little difficult to find, as most compilers are now based on the (more modern) Fortran 95 standard. However, for some reason 6S does not compile using these compilers, so we need to find a Fortran 77 compiler. The best place I've found to get one for Windows is http://www.cse.yorku.ca/~roumani/fortran/ftn.htm. Download the ``FORT99.zip`` file, and extract it somewhere. Copy the ``G77`` folder to the root of the C drive (so that the folder is ``C:\G77``).
 5. We now need to edit the Windows path so that we can easily call the compiler and other tools. To do this, right-click on the My Computer icon on your desktop, or the Computer item on your Start Menu and select ``Properties``. Choose the ``Advanced System Settings`` option on the left-hand side of the resulting window and then click the ``Environment Variables`` button in the next dialog. Now scroll down in the bottom list box until you find a variable called `PATH`. Click `Edit` and add the following string to the end of its contents `;C:\Program Files\GNUWin32\bin;C:\G77\bin`
 6. Open the command window by opening the start menu and typing ``cmd``.
 7. Use the ``cd`` command to move to the folder where the .tar file you downloaded in step 1 is located, for example::

      cd C:\Users\robin\Downloads
      
 8. Run the following commands, one after each other::

      tar -xvf 6SV-1.1.tar
    	cd 6SV1.1
    	make
  
 9. If no errors have been produced, then test the 6S executable by typing::

      sixsV1.1 < ..\Examples\Example_In_1.txt
  
 10. If this is working correctly you should see a number of screen's worth of output, finishing with something that looks like::

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