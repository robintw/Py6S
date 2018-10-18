#!/usr/bin/env python
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

import os
from setuptools import setup


PROJECT_ROOT = os.path.dirname(__file__)


def read_file(filepath, root=PROJECT_ROOT):
    """
    Return the contents of the specified `filepath`.

    * `root` is the base path and it defaults to the `PROJECT_ROOT` directory.
    * `filepath` should be a relative path, starting from `root`.
    """
    with open(os.path.join(root, filepath)) as fd:
        text = fd.read()
    return text


LONG_DESCRIPTION = read_file("README.rst")
SHORT_DESCRIPTION = "A wrapper for the 6S Radiative Transfer Model to make it easy to run simulations with a variety of input parameters, and to produce outputs in an easily processable form."
REQS = [
    'pysolar==0.6',
    'matplotlib',
    'scipy'
]


setup(
    name                  = "Py6S",
    packages              = ['Py6S', 'Py6S.Params', 'Py6S.SixSHelpers'],
    install_requires      = REQS,
    version               = "1.7.2",
    author                = "Robin Wilson",
    author_email          = "robin@rtwilson.com",
    description           = SHORT_DESCRIPTION,
    license               = "GPL",
    test_suite            = 'nose.collector',
    url                   = "http://py6s.rtwilson.com/",
    long_description      = LONG_DESCRIPTION,
    classifiers           = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2"
    ],
)
