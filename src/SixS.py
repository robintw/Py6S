import subprocess
import os
from Outputs import Outputs

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
        
    def write_input_file(self):
        """Writes the generated 6S input file to a temporary file"""
        f = open("tmp_in.txt", "w")
        f.write("0 (User defined)\n")
        f.write('%d %d %d %d %d %d\n' % (self.solar_z, self.solar_a, self.view_z, self.view_a, self.month, self.day))
        f.write("""2 Midlatitude Summer
2 Maritime Model
0\n""")
        f.write('%f value\n' % self.aot550)
        f.write("""0 (target level)
0 (sensor level)
-1 monochromatic\n""")
        f.write('%f \n' % self.wavelength)
        f.write("""0 Homogeneous surface
0 No directional effects
0 constant value for ro
1.0
-1 No atm. corrections selected
""")

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
    print "Using 6S located at %s" % sixs_path