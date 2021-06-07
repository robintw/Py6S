import Py6S
from random import random
from IPython.parallel import Client
from IPython.parallel import depend, require, dependent
import numpy as np
import time


@require("random", "Py6S")
def run(azimuth, zenith):
    s = Py6S.SixS()
    s.ground_reflectance = Py6S.GroundReflectance.HomogeneousRoujean(0.037, 0.0, 0.133)
    s.geometry.view_a = azimuth
    s.geometry.view_z = zenith
    print(zenith)
    s.run()
    return s.outputs.pixel_radiance


pstart = time.time()
c = Client()

lv = c.load_balanced_view()

tasks = []

azimuths = np.linspace(0, 360, 36)
zeniths = np.linspace(0, 80, 8)

for azimuth in azimuths:
    for zenith in zeniths:
        tasks.append(lv.apply(run, azimuth, zenith))

result = [task.get() for task in tasks]
pend = time.time()
print(result)

sstart = time.time()
res = []
for azimuth in azimuths:
    for zenith in zeniths:
        res.append(run(azimuth, zenith))

send = time.time()

print("Parallel %f" % (pend - pstart))
print("Serial %f" % (send - sstart))
