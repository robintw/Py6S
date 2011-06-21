from SixS import SixS
from SixSParams import *
import yaml
import pprint

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

test.aero_profile = AeroModel.MARITIME

test.run()


#print test.outputs.fulltext

#print test.outputs.irradiance_direct