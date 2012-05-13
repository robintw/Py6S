import itertools
import numpy as np
import sixs
from Params import *

def test(i):
  for res in i:
    print res

def named_product(**items):
    names = items.keys()
    vals = items.values()
    for res in itertools.product(*vals):
        yield dict(zip(names, res))
        
def named_product_from_dict(d):
    names = d.keys()
    vals = d.values()
    for res in itertools.product(*vals):
        yield dict(zip(names, res))
        
def set_attrs_from_dict(sixs, d):
  for key, value in d.iteritems():
    if "." in key:
      # We've got a parameter which isn't just s.param but s.param.param
      # For example, s.geometry.solar_z
      s = key.split(".")
      obj = getattr(sixs, s[0])
      attrib = s[1]
    else:
      # We have a simple attribute
      obj = sixs
      attrib = key
    setattr(obj, attrib, value)


i = named_product(a = "12", b = "ab")
test(i)

solar_z = np.arange(0, 70, 10)
solar_a = np.arange(0, 360, 45)

i = named_product_from_dict({'geometry.view_z' : solar_z, 'geometry.view_a' : solar_a})

s = sixs.SixS()
s.aero_profile = AeroProfile.Urban
s.ground_reflectance = GroundReflectance.HomogeneousRoujean(0.037, 0.0, 0.133)
s.geometry = GeometryUser()
s.geometry.solar_z = 30
s.geometry.solar_a = 0

for params in i:
  #print params
  set_attrs_from_dict(s, params)
  s.run()
  print s.outputs.pixel_reflectance


#  [GroundReflectance.HomogeneousLambertian(x) for x in np.arange(0, 10)]

# Creates a lookup table by running 6S with all the combinations of the parameters given.
# Parameters:
# 1: SixS object with the standard parameters you want
# 2: Dictionary with keys equal to the parameter name (the bit after the s. when setting it), and values an iterable with
# the range of values wanted
#def create_lut(s, dict):
  