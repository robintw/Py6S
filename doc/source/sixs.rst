The SixS class
================================

The SixS class is the heart of Py6S. It has attributes and methods that allow you to set parameters, run 6S and access the outputs. These are described in detail below, but the basic usage pattern is::

  from Py6S import *
  s = SixS() # Instantiate the class
  s.aero_profile = AeroProfile.PredefinedType(AeroProfile.Maritime) # Set various parameters
  s.run() # Run the model
  print s.outputs.pixel_irradiance # Access the outputs
  

.. autoclass:: Py6S.SixS
  :members:

Attributes
----------
.. py:attribute:: sixs_path

  The sixs path