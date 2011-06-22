import pprint
from src.SixSExceptions import OutputParsingError

class Outputs(object):
    # Stores the full textual output from 6S
    fulltext = ""
    
    # Stores the numerical values extracted from the textual output as a dictionary
    values = {}
    
    def __init__(self, text):
        """Initialise the class with the text output from the model, and process
        it into the numerical outputs"""
        self.fulltext = text
        self.extract_results()
        
    def __getattr__(self, name):
        """Executed when an attribute is referenced and not found. This method is overridden
        to allow the user to access the outputs as output.variable rather than using the dictionary
        explicity"""
        if self.values.has_key(name):
            return self.values[name]
        else:
            raise OutputParsingError("The specifed output variable does not exist.")
        
    def extract_results(self):
        """Extract the actual results from the text output of the model"""
        
        # Remove all of the *'s from the text as they just make it look pretty
        # and get in the way of analysing the output
        self.fulltext = self.fulltext.replace("*", "")
        
        # Split into lines
        lines = self.fulltext.splitlines()
        
        CURRENT = 0
        
        # The dictionary below specifies how to extract each variable from the text output
        # of 6S.
        # The dictionary key is the text to search for. When this is found, the line corresponding
        # to the first value in the tuple is found. If this is CURRENT (ie. 0) then it is the line on whic
        # the text was found, if it is 1 then it is the next line, 2 the one after that etc.
        # The next item in the tuple is the index of the split line to extract the value from, and the
        # third item is the key to store it in in the values dictionary. The final item is the type to convert
        # it to - the type conversion function must be specified. More specific functions such as math.floor can
        # be used here if desired.
        
        #              Search Term             Line   Index DictKey   Type
        extractors = { "solar zenith angle" : (CURRENT, 3, "solar_z", self.to_int),
                       "ground pressure" : (CURRENT, 3, "ground_pressure", float),                  
                       "irr. at ground level" : (2, 0, "direct_solar_irradiance", float),
                       "irr. at ground level (w/" : (2, 1, "diffuse_solar_irradiance", float),
                       "irr. at ground level (w/m2/mic)" : (2, 2, "environmental_irradiance", float),
                       "% of irradiance" : (2, 0, "percent_direct_solar_irradiance", float),
                       "% of irradiance at" : (2, 1, "percent_diffuse_solar_irradiance", float),
                       "% of irradiance at ground level" : (2, 2, "percent_environmental_irradiance", float),
                       "sol. spect (in w/m2/mic)" : (1, 0, "solar_spectrum", float),
                       "scattering angle:" : (CURRENT, 2, "scattering_angle", float),
                       "azimuthal angle difference:" : (CURRENT, 7, "azimuthal_angle_difference", float),
                       "visibility :" : (CURRENT, 2, "visibility", float),
                       "opt. thick. 550 nm :" : (CURRENT, 9, "aot550", float),
                       "apparent reflectance" : (CURRENT, 2, "integrated_apparent_reflectance", float)
                      }
                
        for index in range(len(lines)):
            current_line = lines[index]
            for label, details in extractors.iteritems():
                # If the label we're searching for is in the current line
                if label in current_line:
                    # See if the data is in the current line (as specified above)
                    if details[0] == CURRENT:
                        extracting_line = current_line
                    # Otherwise, work out which line to use and get it
                    else:
                        extracting_line = lines[index + details[0]]
                    
                    funct = details[3]
                    items = extracting_line.split()
                    self.values[details[2]] = funct(items[details[1]])
                    
        pp = pprint.PrettyPrinter(indent=4)
         
        pp.pprint(self.values)
        
    def to_int(self, str):
        """Converts to int by converting to float and then converting that to int, meaning that
        converting "5.00" to an integer will actually work"""
        return int(float(str))