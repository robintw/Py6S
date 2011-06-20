class Outputs(object):
    fulltext = ""
    
    values = {}
    
#    irradiance_direct = float('nan')
#    irradiance_diffuse = float('nan')
#    irradiance_env = float('nan')
#    radiance_atm_intrinsic = float('nan')
#    radiance_background = float('nan')
#    radiance_pixel = float('nan')
#    integrated_solar_spectrum = float('nan')
#    solar_z = float('nan')
    
    def __init__(self, text):
        """Initialise the class with the text output from the model, and process
        it into the numerical outputs"""
        self.fulltext = text
        self.extract_results()
        
    def __getattr__(self, name):
        if self.values.has_key(name):
            return self.values[name]
        else:
            raise AttributeError
        
    def extract_results(self):
        """Extract the actual results (as appropriately typed variables
        from the text output of the model"""
        
        # Remove all of the *'s from the text as they just make it look pretty
        # and get in the way of analysing the output
        self.fulltext = self.fulltext.replace("*", "")
        
        # Split into lines
        lines = self.fulltext.splitlines()
        
        
        CURRENT = 0
        
        extractors = { "solar zenith angle" : (CURRENT, 3, "solar_z"),
                       "ground pressure" : (CURRENT, 3, "ground_pressure"),                  
                       "irr. at ground level" : (2, 0, "direct_solar_irradiance")
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
                        
                    items = extracting_line.split()
                    self.values[details[2]] = items[details[1]]
                
        print self.solar_z
        print self.ground_pressure
        print self.direct_solar_irradiance
        #values = lines[97].split()
        #self.irradiance_direct, self.irradiance_diffuse, self.irradiance_env = values
        
        #values = lines[100].split()
        #self.radiance_atm_intrinsic, self.radiance_background, self.radiance_pixel = values
        
        #values = lines[104].split()
        #self.integrated_solar_spectrum = values[0]