import itertools
import numpy as np

def test(i):
  for res in i:
    print res

def named_product(**items):
    names = items.keys()
    vals = items.values()
    for res in itertools.product(*vals):
        yield dict(zip(names, res))


i = named_product(a = "12", b = "ab")
test(i)

solar_z = np.arange(0, 70, 10)
solar_a = np.arange(0, 360, 45)

i = named_product(solar_z = solar_z, solar_a = solar_a)
test(i)


#def create_lut()
#  [GroundReflectance.HomogeneousLambertian(x) for x in np.arange(0, 10)]