from Py6S import *
from Py6S.Params.wavelength import WavelengthType


test = SixS()

test.wavelength = WavelengthType.Wavelength(WavelengthType.ETM_B1)

test.write_input_file("test_input")

test.run()
#
#SixS.save_params(test, "params_output_2.yml")
#test = test.load_params("params_output.yml")
#print test.aero_soot


#f = open("test.yaml", "r")
#obj = yaml.load(f)
#print obj.aero_profile
#test.run()
#print test.outputs.direct_solar_irradiance

#print test.ground_reflectance

#test.aero_profile = AeroModel.MARITIME

#test.run()


#print test.outputs.fulltext

#print test.outputs.irradiance_direct