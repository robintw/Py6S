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


class Error(Exception):

    """Base class for exceptions raised in the process of running 6S."""
    pass


class ParameterError(Error):

    """Exception raised for errors in parameter specifications.

    Call as:

    ParameterError(parameter_name, message)

    """

    def __init__(self, param_name, msg):
        self.param_name = param_name
        self.msg = msg

    def __str__(self):
        return "%s: %s" % (self.param_name, self.msg)


class OutputParsingError(Error):

    """Exception raised for errors when parsing the 6S output.

    Call as:

    OutputParsingError(message)

    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ExecutionError(Error):

    """Exception raised for errors when running the 6S model.

    Call as:

    ExecutionError(message)

    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
