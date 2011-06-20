from SixS import SixS
from SixSParams import *

test = SixS()

test.aero_profile = AeroModel.MARITIME
test.write_input_file()
test.run()

print test.outputs.fulltext

print test.outputs.irradiance_direct