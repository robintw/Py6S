class AtmosCorr:

	@classmethod
	def NoAtmosCorr(cls):
		return """-1 No atm. corrections selected\n"""
	
	@classmethod
	def AtmosCorrLambertianFromRadiance(cls, value):
		return """0 Atm. correction Lambertian
%f radiance""" % value
		
	@classmethod
	def AtmosCorrLambertianFromReflectance(cls, value):
		return """0 Atm. correction Lambertian
%f reflectance""" % (value * -1)

	@classmethod
	def AtmosCorrBRDFFromRadiance(cls, value):
		return """1 BRDF
%f radiance""" % value

	@classmethod
	def AtmosCorrBRDFFromReflectance(cls, value):
		return """1 BRDF
%f reflectance""" % (value * -1)