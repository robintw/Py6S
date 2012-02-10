class AtmosCorr:
  """Class representing options for selecting atmospheric correction settings for 6S"""

	@classmethod
	def NoAtmosCorr(cls):
    """No atmospheric correction to be performed"""
		return """-1 No atm. corrections selected\n"""
	
	@classmethod
	def AtmosCorrLambertianFromRadiance(cls, value):
    """Perform atmospheric correction assuming a Lambertian surface, using a given radiance value"""
		return """0 Atm. correction Lambertian
%f radiance""" % value
		
	@classmethod
	def AtmosCorrLambertianFromReflectance(cls, value):
    """Perform atmospheric correction assuming a Lambertian surface, using a given reflectance value"""
		return """0 Atm. correction Lambertian
%f reflectance""" % (value * -1)

	@classmethod
	def AtmosCorrBRDFFromRadiance(cls, value):
    """Perform atmospheric correction using a fully BRDF-represented surface, using a given radiance value"""
		return """1 BRDF
%f radiance""" % value

	@classmethod
	def AtmosCorrBRDFFromReflectance(cls, value):
    """Perform atmospheric correction using a fully BRDF-represented surface, using a given reflectance value"""
		return """1 BRDF
%f reflectance""" % (value * -1)