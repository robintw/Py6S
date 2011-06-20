class Outputs(object):
    fulltext = ""
    
    irradiance_direct = float('nan')
    irradiance_diffuse = float('nan')
    irradiance_env = float('nan')
    radiance_atm_intrinsic = float('nan')
    radiance_background = float('nan')
    radiance_pixel = float('nan')
    integrated_solar_spectrum = float('nan')
    
    def __init__(self, text):
        """Initialise the class with the text output from the model, and process
        it into the numerical outputs"""
        self.fulltext = text
        self.extract_results()
        
    def extract_results(self):
        """Extract the actual results (as appropriately typed variables
        from the text output of the model"""
        
        # Remove all of the *'s from the text as they just make it look pretty
        # and get in the way of analysing the output
        self.fulltext = self.fulltext.replace("*", "")
        
        # Split into lines
        lines = self.fulltext.splitlines()
        
        
        values = lines[97].split()
        self.irradiance_direct, self.irradiance_diffuse, self.irradiance_env = values
        
        values = lines[100].split()
        self.radiance_atm_intrinsic, self.radiance_background, self.radiance_pixel = values
        
        values = lines[104].split()
        self.integrated_solar_spectrum = values[0]