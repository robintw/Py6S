import urllib2
from StringIO import StringIO
import numpy as np

def import_from_usgs(loc):
	"""Imports a spectral library from the USGS Spectral Library.

	Arguments:
      
      * ``loc`` -- Location of the data to import. Can either be a URL (eg. http://speclab.cr.usgs.gov/spectral.lib06/ds231/ASCII/V/russianolive.dw92-4.30728.asc)
      or a file path.

    Returns:

    A NumPy array with two columns: wavelength (um) and reflectance (fraction)
    """
	if loc.startswith("""http://"""):
		data = urllib2.urlopen(loc).read()
		f = StringIO(data)
	else:
		f = open(loc, "r")
	
	npdata = np.loadtxt(f, skiprows=16)
	f.close()
	npdata[npdata==-1.23e+34] = np.nan
	npdata = npdata[:, 0:2]

	return npdata

def import_from_aster(loc):
	"""Imports a spectral library from the ASTER Spectral Library

	Arguments:
      
      * ``loc`` -- Location of the data to import. Can either be a URL (eg.http://speclib.jpl.nasa.gov/speclibdata/jhu.becknic.vegetation.trees.conifers.solid.conifer.spectrum.txt)
      or a file path.

    Returns:

    A NumPy array with two columns: wavelength (um) and reflectance (fraction)
    """
	if loc.startswith("""http://"""):
		data = urllib2.urlopen(loc).read()
		f = StringIO(data)
	else:
		f = open(loc, "r")
	
	npdata = np.loadtxt(f, skiprows=26)
	f.close()
	npdata[:,1] = npdata[:,1] / 100
	return npdata