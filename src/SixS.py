import subprocess
import os
from Outputs import Outputs
from SixSParams import *
from SixSExceptions import *
import yaml

class SixS(object):
    """Wrapper for the 6S Radiative Transfer Model"""

    # Stores the outputs from 6S as an instance of the Outputs class
    outputs = None
    
    def __init__(self):
        """Initialises the class and finds the right sixs executable to use"""
        self.sixs_path = self.find_path("sixs")
        
        self.atmos_profile = AtmosModel.MIDLATITUDE_SUMMER
        self.aero_profile = AeroModel.MARITIME
        
        self.ground_reflectance = 1.0
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
        """Finds the full path to a program, searching the $PATH environment
        variable and the current directory"""
        
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
        return '0 (User defined)\n%d %d %d %d %d %d\n' % (self.solar_z, self.solar_a, self.view_z, self.view_a, self.month, self.day)

    def create_atmos_aero_lines(self):
        # As long as we've selected one of the pre-specified aerosol models
        # (ie. not the user one) then simply return the numbers
        if self.aero_profile != AeroModel.USER:
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
        # If aot is set then use it
        if self.aot550 != None:
            return """0
%f value\n""" % self.aot550
        elif self.visibility != None:
            return """%f\n""" % self.visibility
            
    def create_elevation_lines(self):
        return """0 (target level)
0 (sensor level)\n"""

    def create_wavelength_lines(self):
        return """-1 monochromatic
%f\n""" % self.wavelength

    def create_surface_lines(self):
        return """0 Homogeneous surface
0 No directional effects
0 constant value for ro
%f\n""" % self.ground_reflectance

    def create_atmos_corr_lines(self):
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
        and writes it to a temporary file"""
        
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
        """Runs the 6S model and stores the outputs in the output variable"""
        
        if self.sixs_path == None:
            raise ExecutionError("6S executable not found.")     
        
        self.write_input_file("tmp_in.txt")
        
        # Run the process and get the stdout from it
        process = subprocess.Popen("%s < tmp_in.txt" % self.sixs_path, shell=True, stdout=subprocess.PIPE)
        self.outputs = Outputs(process.communicate()[0])

    @classmethod
    def save_params(cls, obj, filename):
        """Save the current parameter settings to the specified file"""
        with open(filename, "w") as f:
            yaml.dump(obj, f, default_flow_style=False)
    
    @classmethod   
    def load_params(cls, filename):
        """Load the parameter values from the specified file"""
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