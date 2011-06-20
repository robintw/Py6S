# Py6S #

Py6S is a Python wrapper around the 6S radiative transfer model. This model is often used in remote
sensing and atmospheric sciences, and provides highly accurate results. However, it can only process
one band and one viewing geometry at a time. A number of applications require processing data for
multiple wavebands or viewing geometries, and this wrapper makes this easy.

For example:

```python
import numpy as np
from SixS import SixS

model = SixS()

for wavelength in np.arange(0.4, 0.8, 0.001):
    model.wavelength = wavelength
    model.write_input_file()
    model.run()
    
    print "Wavelength = %f \t Direct Irradiance = %f" % (wavelength, model.outputs.irradiance_direct)
```

For more details please see the
[full documentation](https://github.com/robintw/Py6S/blob/master/doc/docs.markdown).