class AtmosCorr:
  """Class representing options for selecting atmospheric correction settings for 6S."""

	@classmethod
	def NoAtmosCorr(cls):
    """Set 6S not to perform any atmospheric correction"""
		return """-1 No atm. corrections selected\n"""
	
	@classmethod
	def AtmosCorrLambertianFromRadiance(cls, radiance):
    """Set 6S to perform atmospheric correction assuming a Lambertian surface, using a given radiance value.
    
    Arguments:
    radiance -- Radiance of the surface.
    
    """
		return """0 Atm. correction Lambertian
%f radiance""" % radiance
		
	@classmethod
	def AtmosCorrLambertianFromReflectance(cls, reflectance):
    """Set 6S to perform atmospheric correction assuming a Lambertian surface, using a given reflectance value.
    
    Arguments:
    reflectance -- Reflectance of the surface.
    
    """
		return """0 Atm. correction Lambertian
%f reflectance""" % (reflectance * -1)

	@classmethod
	def AtmosCorrBRDFFromRadiance(cls, radiance):
    """Set 6S to perform atmospheric correction using a fully BRDF-represented surface, using a given radiance value.
    
    Arguments:
    radiance -- Radiance of the surface
    
    """
		return """1 BRDF
%f radiance""" % radiance

	@classmethod
	def AtmosCorrBRDFFromReflectance(cls, reflectance):
    """Set 6S to perform atmospheric correction using a fully BRDF-represented surface, using a given reflectance value.
    
    Arguments:
    reflectance -- Reflectance of the surface.
    
    """
		return """1 BRDF
%f reflectance""" % (reflectance * -1)