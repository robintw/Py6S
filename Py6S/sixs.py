import subprocess
import os
import yaml

from Params import *
from sixs_exceptions import *
from outputs import *

class SixS(object):
    """
    Wrapper for the 6S Radiative Transfer Model. This is the main class which can be used
    to instantiate an object which has the key methods for running 6S.
    
    The most import method in this class is the L{run} method which writes the 6S input file,
    runs the model and processes the output.
    
    The parameters of the model are set as the attributes of this class - for example, C{solar_z},
    C{day} and C{wavelength}.
    
    For example:
    
    >>> from Py6S import *
    >>> model = SixS()
    >>> model.wavelength = 0.640
    >>> model.run()
    >>> model.outputs.direct_solar_irradiance
    695.0
    
    For a simple test to ensure that Py6S has found the correct executable for 6S simply
    execute this file and it will print a test message.
    
    """

    # Stores the outputs from 6S as an instance of the Outputs class
    outputs = None
    
    def __init__(self, path=None):
        """Initialises the class and finds the right sixs executable to use"""
        self.sixs_path = self.find_path(path)

        self.atmos_profile = AtmosProfile.MIDLATITUDE_SUMMER
        self.aero_profile = AeroProfile.MARITIME
        
        self.ground_reflectance = GroundReflectance.HomogeneousLambertian(0.0)
        
        self.geometry = GeometryUser()
        self.geometry.solar_z = 32
        self.geometry.solar_z = 32
        self.geometry.solar_a = 264
        self.geometry.view_z = 23
        self.geometry.view_a = 190
        self.geometry.day = 14
        self.geometry.month = 7
        
        
        self.wavelength = Wavelength.Wavelength(0.500)
        
        self.aot550 = 0.5
        self.visibility = None
        
        self.aero_dustlike = 0
        self.aero_water = 0
        self.aero_oceanic = 0
        self.aero_soot = 0
        
        self.atmos_corr = AtmosCorr.NoAtmosCorr()
    
    def find_path(self, path):
		if path != None:
			return path
		else:
			return self.which('sixs.exe') or self.which('sixs') or self.which('sixsV1.1') or self.which('sixsV1.1.exe')
        
    def which(self, program):
        def is_exe(fpath):
            return os.path.exists(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None
        

    def create_geom_lines(self):
      return str(self.geometry)

    def create_atmos_aero_lines(self):
        """Creates the atmosphere and aerosol lines for the input file"""
        # As long as we've selected one of the pre-specified aerosol models
        # (ie. not the user one) then simply return the numbers
        if self.aero_profile == None:
            raise ParameterError("aero_profile", "You must specify an aerosol profile.")
        elif self.aero_profile != AeroProfile.USER:
            if self.aero_dustlike + self.aero_oceanic + self.aero_soot + self.aero_water > 0.0:
                raise ParameterError("aero_profile", "Individual aerosol components are set but the aerosol model is not set to USER.")
            return """%d
%d\n""" % (self.atmos_profile, self.aero_profile)
        # Otherwise, check we've been given all of the parameters and put them in
        else:
            if self.aero_dustlike + self.aero_oceanic + self.aero_soot + self.aero_water != 1.0:
                raise ParameterError("aero_*", "Incorrect specification of User-defined Aerosol Components - must sum to 1.0")
            return """%d
%d
%f %f %f %f""" % (self.atmos_profile, self.aero_profile, self.aero_dustlike, self.aero_water, self.aero_oceanic, self.aero_soot)

    def create_aot_vis_lines(self):
        """Create the AOT or Visibility lines for the input file"""
        # If aot is set then use it
        if self.aot550 != None:
            return """0
%f value\n""" % self.aot550
        elif self.visibility != None:
            return """%f\n""" % self.visibility
        else:
            raise ParameterError("aot550", "You must set either the AOT at 550nm or the Visibility in km.")
            
    def create_elevation_lines(self):
        """Create the elevation lines for the input file"""
        return """0 (target level)
0 (sensor level)\n"""

    def create_wavelength_lines(self):
        """Create the wavelength lines for the input file"""
        return self.wavelength

    def create_surface_lines(self):
        """Create the surface reflectance lines for the input file"""
        return self.ground_reflectance

    def create_atmos_corr_lines(self):
        """Create the atmospheric correction lines for the input file"""
        return self.atmos_corr

    def write_input_file(self, filename):
        """Generates a 6S input file from the parameters stored in the object
        and writes it to the given filename.
        
        The input file is guaranteed to be a valid 6S input file which can be run manually if required
        
        """
        
        with open(filename, "w") as f:
            input_file = self.create_geom_lines()
            
            input_file += self.create_atmos_aero_lines()
            
            input_file += self.create_aot_vis_lines()
            
            input_file += self.create_elevation_lines()
            
            input_file += self.create_wavelength_lines()
            
            input_file += self.create_surface_lines()
    
            input_file += self.create_atmos_corr_lines()
    
            f.write(input_file)

    def run(self):
        """Runs the 6S model and stores the outputs in the C{output} variable"""
        
        if self.sixs_path == None:
            raise ExecutionError("6S executable not found.")     
        
        self.write_input_file("tmp_in.txt")
        
        # Run the process and get the stdout from it
        process = subprocess.Popen("%s < tmp_in.txt" % self.sixs_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        outputs = process.communicate()
        self.outputs = Outputs(outputs[0], outputs[1])

    def test(self):
        test = SixS()
        print "6S wrapper script by Robin Wilson"
        sixs_path = test.find_path("sixs")
        if sixs_path == None:
            print "Error: cannot find sixs executable in $PATH or current directory."
        else:
            print "Using 6S located at %s" % sixs_path
            print "Running 6S using a set of test parameters"
            test.run()
            print "The results are:"
            print "Expected result: %f" % 619.158
            print "Actual result: %f" % test.outputs.diffuse_solar_irradiance
            if (test.outputs.diffuse_solar_irradiance - 619.158 < 0.01):
                print "#### Results agree, Py6S is working correctly"