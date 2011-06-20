import subprocess
import os
from Outputs import Outputs
from SixSParams import *

class SixS(object):
    """Wrapper for the 6S Radiative Transfer Model"""

    # Variables which control what is put into the 6S input file
    solar_z = 32
    solar_a = 264
    view_z = 23
    view_a = 190
    day = 14
    month = 7
    wavelength = 0.453
    aot550 = 0.5
    ground_reflectance = 1.0
    
    aero_dustlike = 0
    aero_water = 0
    aero_oceanic = 0
    aero_soot = 0
    
    atmos_profile = AtmosModel.MIDLATITUDE_SUMMER
    aero_profile = AeroModel.MARITIME
    
    # Path to the SixS executable - filled in by the constructor
    sixs_path = ""
    
    # Stores the outputs from 6S as an instance of the Outputs class
    outputs = None
    
    def __init__(self):
        """Initialises the class and finds the right sixs executable to use"""
        self.sixs_path = self.find_path("sixs")
    
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
        """Create the line for the input file specifying the geometeries and the day/month"""
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
                print "Incorrect specification of User-defined Aerosol Components: Must add up to 1.0"
                return ""
            return """%d
%d
%f %f %f %f""" % (self.atmos_profile, self.aero_profile, )
            

    def create_aot_vis_lines(self):
        # If aot is set then use it
        if self.aot550 != None:
            return """0
%f value\n""" % self.aot550
            
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
        return """-1 No atm. corrections selected\n"""

    def write_input_file(self):
        """Generates a 6S input file from the parameters stored in the object
        and writes it12"""
        
        f = open("tmp_in.txt", "w")
        
        input_file = self.create_geom_lines()
        
        input_file += self.create_atmos_aero_lines()
        
        input_file += self.create_aot_vis_lines()
        
        input_file += self.create_elevation_lines()
        
        input_file += self.create_wavelength_lines()
        
        input_file += self.create_surface_lines()

        input_file += self.create_atmos_corr_lines()

        f.write(input_file)

    def run(self):
        """Runs the 6S model and stores the output in the output variable"""
        if self.sixs_path == None:
            print "6S executable not found. Stopping"        
        
        # Run the process and get the stdout from it
        process = subprocess.Popen("%s < tmp_in.txt" % self.sixs_path, shell=True, stdout=subprocess.PIPE)
        self.outputs = Outputs(process.communicate()[0])




# If this file is run itself then print output showing which sixs executable will be used
if __name__ == "__main__":
    test = SixS()
    print "6S wrapper script by Robin Wilson"
    sixs_path = test.find_path("sixs")
    if sixs_path == None:
        print "Error: cannot find sixs executable in $PATH or current directory."
    else:
        print "Using 6S located at %s" % sixs_path