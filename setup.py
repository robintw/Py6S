import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name                  = "Py6S",
        packages              = ['Py6S', 'Py6S.Params', 'Py6S.SixSHelpers'],
        requires              = ['pysolar', 'numpy', 'matplotlib', 'scipy'],
        install_requires      = ['pysolar', 'numpy', 'matplotlib', 'scipy'],
        version               = "1.1.1",
        author                = "Robin Wilson",
        author_email          = "robin@rtwilson.com",
        description           = ("""A wrapper for the 6S Radiative Transfer Model to make it easy to run simulations
        with a variety of input parameters, and to produce outputs in an easily processable form."""),
        license               = "BSD",
        url                   = "http://packages.python.org/Py6S",
        long_description      =read('README'),
        classifiers           =[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python"
        
        ],
)
