import subprocess
import os
import yaml

from Py6S.Params import *
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
    
    def __init__(self):
        """Initialises the class and finds the right sixs executable to use"""
        self.sixs_path = self.find_path("sixs")
                
        self.atmos_profile = AtmosModel.MIDLATITUDE_SUMMER
        self.aero_profile = AeroModel.MARITIME
        
        self.ground_reflectance = GroundReflectance.HomogeneousLambertian(1.0)
        self.solar_z = 32
        self.solar_a = 264
        self.view_z = 23
        self.view_a = 190
        self.day = 14
        self.month = 7
        self.wavelength = 0.453
        self.aot550 = 0.5
        self.visibility = None
        
        self.aero_dustlike = 0
        self.aero_water = 0
        self.aero_oceanic = 0
        self.aero_soot = 0
        
        self.atmos_corr = AtmosCorr.NO_ATMOS_CORR
        self.atmos_corr_reflectance = None
        self.atmos_corr_radiance = None
    
    def find_path(self, program):
        """Finds the full path to a given program name, searching the $PATH environment
        variable and the current directory.
        
        Used in this context to find the 6S executable."""
        
        # Get the paths from the $PATH environment variable
        paths_to_search = os.environ.get('PATH', '').split(':')
        # Add the current directory to that path
        paths_to_search.append(os.getcwd())
        
        # For each path, check it exists and isn't a directory, if so then return it
        for path in paths_to_search:
            if os.path.exists(os.path.join(path, program)) and \
               not os.path.isdir(os.path.join(path, program)):
                return os.path.join(path, program)
        return None
        

    def create_geom_lines(self):
        if self.solar_z == None:
            raise ParameterError("solar_z", "You must set the solar zenith angle.")
        if self.solar_a == None:
            raise ParameterError("solar_a", "You must set the solar azimuth angle.")
        if self.view_z == None:
            raise ParameterError("view_z", "You must set the view zenith angle.")
        if self.view_a == None:
            raise ParameterError("view_a", "You must set the view azimuth angle.")
        if self.month < 1 or self.month > 12:
            raise ParameterError("month", "You must set a valid month.")
        if self.day < 1 or self.day > 31:
            raise ParameterError("day", "You must set a valid day.")
        return '0 (User defined)\n%d %d %d %d %d %d\n' % (self.solar_z, self.solar_a, self.view_z, self.view_a, self.month, self.day)

    def create_atmos_aero_lines(self):
        """Creates the atmosphere and aerosol lines for the input file"""
        # As long as we've selected one of the pre-specified aerosol models
        # (ie. not the user one) then simply return the numbers
        if self.aero_profile == None:
            raise ParameterError("aero_profile", "You must specify an aerosol profile.")
        elif self.aero_profile != AeroModel.USER:
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
        if self.atmos_corr == AtmosCorr.NO_ATMOS_CORR:
            return """-1 No atm. corrections selected\n"""
        else:
            if self.atmos_corr_radiance != None and self.atmos_corr_reflectance != None:
                raise ParameterError("atmos_corr_reflectance", "Both radiance and reflectance are given for atmospheric correction. I can't decide which one to use!")
            elif self.atmos_corr_radiance != None:
                # Use radiance
                value = self.atmos_corr_radiance
            elif self.atmos_corr_reflectance != None:
                # Use reflectance
                value = -1 * self.atmos_corr_reflectance
            else:
                raise ParameterError("atmos_corr_reflectance", "Atmospheric correction is enabled, but no radiance or reflectance values are given.")
            
            return """%d\n%f\n""" % (self.atmos_corr, value)

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

    @classmethod
    def save_params(cls, obj, filename):
        """Save the current parameter settings to the specified file. Note that this is a class method,
        therefore it must be called from the class name. For example:
        
        >>> from Py6S import *
        >>> model = SixS()
        >>> model.solar_z = 23
        >>> SixS.save_params(model, "SavedParams.yml")        
        
        """
        with open(filename, "w") as f:
            yaml.dump(obj, f, default_flow_style=False)
    
    @classmethod   
    def load_params(cls, filename):
        """Load the parameter values from the specified file. Note that this is a class method,
        therefore it must be called from the class name. For example:
        
        >>> from Py6S import *
        >>> SixS.load_params(model, "SavedParams.yml")        
        
        """
        
        with open(filename, "r") as f:
            obj = yaml.load(f)
            print obj.aero_soot
            return obj
        
#########################################################################################
# If this file is run itself then print output showing which sixs executable will be used
if __name__ == "__main__":
    test = SixS()
    print "6S wrapper script by Robin Wilson"
    sixs_path = test.find_path("sixs")
    if sixs_path == None:
        print "Error: cannot find sixs executable in $PATH or current directory."
    else:
        print "Using 6S located at %s" % sixs_path