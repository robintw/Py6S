from Py6S import *
from Py6S.Params.ground_reflectance import GroundReflectance

test = SixS()
#
#SixS.save_params(test, "params_output_2.yml")
#test = test.load_params("params_output.yml")
#print test.aero_soot


#f = open("test.yaml", "r")
#obj = yaml.load(f)
#print obj.aero_profile
#test.run()
#print test.outputs.direct_solar_irradiance

print GroundReflectance.HomogeneousLambertian(GroundReflectance.LakeWater)

#print test.ground_reflectance

#test.aero_profile = AeroModel.MARITIME

#test.run()


#print test.outputs.fulltext

#print test.outputs.irradiance_direct