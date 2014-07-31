# This file is part of Py6S.
#
# Copyright 2012 Robin Wilson and contributors listed in the CONTRIBUTORS file.
#
# Py6S is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Py6S is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Py6S.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from Py6S import *
import numpy as np

class RunAllWavelengthsTests(unittest.TestCase):

    def test_run_all_wavelengths(self):
        s = SixS()
        attribs = dir(SixSHelpers.Wavelengths)
        for f in attribs:
        	if "run" in f and f != 'run_wavelengths':
        		func = eval('SixSHelpers.Wavelengths.' + f)
        		results = func(s, output_name='apparent_radiance')

        		results = func(s)

    def test_extract_output(self):
    	s = SixS()
    	wvs, values = SixSHelpers.Wavelengths.run_landsat_etm(s, output_name='apparent_reflectance')
    	wvs, objs = SixSHelpers.Wavelengths.run_landsat_etm(s)

    	obj_values = SixSHelpers.Wavelengths.extract_output(objs, 'apparent_reflectance')

    	self.assertTrue(np.all(values == obj_values))