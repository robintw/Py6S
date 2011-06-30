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


	6S wrapper script by Robin Wilson
	Using 6S located at /usr/bin/sixs


## Usage ##

### Basic Usage ###
The general process for using Py6S is to:

  1. Instantiate the SixS class - for example, `model = SixS()`
  2. Set the parameters appropriately - for example, `model.solar_z = 50` or `model.wavelength = WavelengthTypes.Wavelength(0.550, 0.600)`
  3. Call the `run()` method to run the model - for example, `model.run()`
  4. Read the outputs from the `outputs` member variable - for example, `print model.outputs.irradiance_diffuse`

A heavily-commented example is shown below:

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
		
### Loading and Saving Parameters ###
Once the SixS object has been initialised with a number of parameters, these can be saved to a file
to allow easy restoring of the values at a later time. Of course, the parameters could instead be written to a 6S
format input file, but there is no way to read these values in to this wrapper due to the format of the input file. By saving
using these methods the parameter values can be easily restored.

The file format in which the parameters are saved is the [YAML format](http://www.yaml.org/). This is plain-text-based, human-readable,
human-editable, and parsers exist for a large number of programming languages.


#### Saving parameters ####
To save the parameters, simply call the `save_params` class method, for example

	model = SixS()
	model.aero_soot = 0.5
	model.aero_water = 0.5

	SixS.save_params(model, "params_output.yml")
	
Note that the `save_params` method is called from the SixS class as opposed to the instance of the class (`model` in this case).
This will produce output like the following:

	!!python/object:SixS.SixS
	aero_dustlike: 0
	aero_oceanic: 0
	aero_soot: 0
	aero_water: 0
	aot550: 0.5
	day: 14
	ground_reflectance: 1.0
	month: 7
	sixs_path: /usr/bin/sixs
	solar_a: 264
	solar_z: 32
	view_a: 190
	view_z: 23
	visibility: null
	wavelength: 0.45300000000000001

All of the parameters are listed in alphabetical order, with human-readable names. This file can be
edited by hand simply by changing the values. The order of values is not important, but it is essential to keep the top line unchanged.

#### Loading parameters ####
To load the parameters from a previously saved (or manually created) file, simply call the `load_params` class method, for example:

	model = SixS.load_params("params_output.yml")
	
Again, note that this method is a class method as opposed to an instance method, so is called as such.

### Dealing with errors ###
A number of errors can occur when running 6S through Py6S. When these errors are encountered a Python exception is raised.
Some errors are convered by the built-in exceptions provided by Python (such as FileErrors and AttributeErrors), but some are
more specialised. Therefore, three new exceptions have been created for Py6S:

* `ParameterError` - raised if there is an error in the 6S parameter specification (for example, an impossible combination of parameters)
* `ExecutionError` - raised if there is an error executing the 6S model (for example the executable cannot be found)
* `OutputParsingError` - raised if there is an error parsing the text output produced by 6S (for example, the output file was not produced properly)

These are defined in the SixSExceptions module, and must be imported if they are to be used in a `try...except` block.
All of these errors will only be raised during the `run()` method (and the methods that this calls), therefore any `try...except` block should
be around the call to `run()`.
