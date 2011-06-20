# Py6S Documentation #

## Introduction ##
Py6S is a wrapper for the [6S radiative transfer model](http://6s.ltdri.org/). It allows programmatic
creation of 6S input files, and reading of 6S output files. It is designed to hide the difficulties
of creating correctly formatted input and output files and present a simple interface for parameterising,
running and processing output from 6S.

**WARNING:** Py6S is still in early development. If it destroys anything, don't blame me. If you want to see
what new features are planned then look at the [todo list](https://github.com/robintw/Py6S/blob/master/doc/todo.markdown).

## Installation ##

### Compiling 6S ###
Py6S is not a replacement for 6S, it is simply a *wrapper*. Therefore, it needs to have access to a
working 6S executable. The Fortran source for 6S can be downloaded from [here](ftp://kratmos.gsfc.nasa.gov/pub/eric/6S/).
Ensure you have a Fortran compiler installed (the Fortran compiler from the
[GNU Compiler Collection](http://gcc.gnu.org/) is a good choice) and then simply run `make` which will produce an executable.

### Helping Py6S find 6S ###
Py6S needs to know where to find the 6S executable. This can be done programmatically by setting the
location (see below) but it is better to ensure that the 6S executable is on your system PATH. On POSIX
systems (Linux, Unix, OS X) this can be done in two ways:
* Add the directory containing 6S to your `PATH` environment variable (this can normally be done through your shell initialisation files
, for example `.bashrc` for the BASH shell, and rename the executable to `sixs`
* Create a symbolic link in somewhere like `/usr/bin` to the 6S executable. For example, on my Mac I can do this by typing `ln -s /usr/bin/sixs /Users/robin/6S/SixSV1.1`

**Note:** The executable must be named `sixs` for Py6S to find it.

### Testing ###
In the directory where Py6S is installed, run `python SixS.py`. This should produce an output similar to that below:

```
6S wrapper script by Robin Wilson
Using 6S located at /usr/bin/sixs
```

## Usage ##

The general process for using Py6S is to:

  1. Instantiate the SixS class - for example, `model = SixS()`
  2. Set the parameters appropriately - for example, `model.solar_z = 50`
  3. Call the `run()` method to run the model - for example, `model.run()`
  4. Read the outputs from the `outputs` member variable - for example, `print model.outputs.irradiance_diffuse`

A heavily-commented example is shown below:

```python
import numpy as np # We're importing NumPy so that we can use the arange command below
from SixS import SixS # Import the SixS class
from SixSParams import * # Import the helper classes for specifying 6S parameters

model = SixS() # Instantiate the class

# Set a couple of simple numerical parameters
model.solar_z = 50
model.view_z = 23

# Set the atmospheric profile type. This uses the AtmosModel class which provides a list of the
pre-specified atmospheric profile types for ease of use.
model.atmos_profile = AtmosModel.MIDLATITUDE_SUMMER

# Set the aerosol profile in the same way
model.aero_profile = AeroModel.MARITIME

# For each wavelength in the range 0.4 to 0.8, stepping by 0.001 (ie. 0.400, 0.401, 0.402...)
for wavelength in np.arange(0.4, 0.8, 0.001):
	# Set the model to produce output for this wavelength
    model.wavelength = wavelength
    
    # Run the model
    model.run()
    
    # Print one of the output variables
    print "Wavelength = %f \t Direct Irradiance = %f" % (wavelength, model.outputs.irradiance_direct)
```