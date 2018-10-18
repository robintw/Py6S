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

import numpy as np
from matplotlib.pyplot import *
import itertools
from multiprocessing.dummy import Pool
import copy


class Angles:

    @classmethod
    def run360(cls, s, solar_or_view, na=36, nz=10, output_name=None, n=None):
        """Runs Py6S for lots of angles to produce a polar contour plot.

        The calls to 6S for each angle will be run in parallel, making this function far faster than simply
        running a for loop over all of the angles.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance configured with all of the parameters you want to run the simulation with
        * ``solar_or_view`` -- Set to ``'solar'`` if you want to iterate over the solar zenith/azimuth angles or ``'view'`` if you want to iterate over the view zenith/azimuth angles
        * ``output_name`` -- (Optional) The name of the output from the 6S simulation to plot. This should be a string containing exactly what you would put after ``s.outputs`` to print the output. For example `pixel_reflectance`.
        * ``na`` -- (Optional) The number of azimuth angles to iterate over to generate the data for the plot (defaults to 36, giving data every 10 degrees)
        * ``nz`` -- (Optional) The number of zenith angles to iterate over to generate the data for the plot (defaults to 10, giving data every 10 degrees)
        * ``n`` -- (Optional) The number of threads to run in parallel. This defaults to the number of CPU cores in your system, and is unlikely to need changing.

        For example::

          s = SixS()
          s.ground_reflectance = GroundReflectance.HomogeneousWalthall(0.48, 0.50, 2.95, 0.6)
          s.geometry.solar_z = 30
          s.geometry.solar_a = 0
          data = SixSHelpers.Angles.run360(s, 'view', output_name='pixel_reflectance')
        """

        results = []

        azimuths = np.linspace(0, 360, na)
        zeniths = np.linspace(0, 89, nz)

        def f(args):
            azimuth, zenith = args
            s.outputs = None
            a = copy.deepcopy(s)

            if solar_or_view == 'view':
                a.geometry.view_a = azimuth
                a.geometry.view_z = zenith
            elif solar_or_view == 'solar':
                a.geometry.solar_a = azimuth
                a.geometry.solar_z = zenith
            else:
                raise ParameterException("all_angles", "You must choose to vary either the solar or view angle.")

            a.run()

            if output_name is None:
                return a.outputs
            else:
                return getattr(a.outputs, output_name)

        # Run the map
        if n is None:
            pool = Pool()
        else:
            pool = Pool(n)

        print("Running for many angles - this may take a long time")
        results = pool.map(f, itertools.product(azimuths, zeniths))
        pool.close()
        pool.join()

        results = np.array(results)

        return (results, azimuths, zeniths, s.geometry.solar_a, s.geometry.solar_z)

    @classmethod
    def plot360(cls, data, output_name=None, show_sun=True, colorbarlabel=None):
        """Plot the data returned from :meth:`run360` as a polar contour plot, selecting an output if required.

        Arguments:

        * ``data`` -- The return value from :meth:`run360`
        * ``output_name`` -- (Optional) The output name to extract (eg. "pixel_reflectance") if the given data is provided as instances of the Outputs class
        * ``show_sun`` -- (Optional) Whether to show the location of the sun on the resulting polar plot.
        * ``colorbarlabel`` -- (Optional) The label to use on the color bar shown with the plot
        """

        results, azimuths, zeniths, sa, sz = data

        if not isinstance(results[0], float):
            # The results are not floats, so a float must be extracted from the output
            if output_name is None:
                raise ParameterException("output_name", "You must specify an output name when plotting data which is given as Outputs instances")

            results = cls.extract_output(results, output_name)

        fig, ax, cax = cls.plot_polar_contour(results, azimuths, zeniths, colorbarlabel=colorbarlabel)

        if show_sun:
            ax.autoscale(False)
            ax.plot(np.radians(sa), sz, '*', markersize=20, markerfacecolor='yellow', markeredgecolor='red')
            show()

        return fig, ax

    @classmethod
    def run_and_plot_360(cls, s, solar_or_view, output_name, show_sun=True, na=36, nz=10, colorbarlabel=None):
        """Runs Py6S for lots of angles to produce a polar contour plot.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance configured with all of the parameters you want to run the simulation with
        * ``solar_or_view`` -- Set to ``'solar'`` if you want to iterate over the solar zenith/azimuth angles or ``'view'`` if you want to iterate over the view zenith/azimuth angles
        * ``output_name`` -- The name of the output from SixS to plot. This should be a string containing exactly what you would put after ``s.outputs`` to print the output. For example `pixel_reflectance`.
        * ``show_sun`` -- (Optional) Whether to place a marker showing the location of the sun on the contour plot (defaults to True, has no effect when ``solar_or_view`` set to ``'solar'``.)
        * ``na`` -- (Optional) The number of azimuth angles to iterate over to generate the data for the plot (defaults to 36, giving data every 10 degrees)
        * ``nz`` -- (Optional) The number of zenith angles to iterate over to generate the data for the plot (defaults to 10, giving data every 10 degrees)
        * ``colorbarlabel`` -- (Optional) The label to use on the color bar shown with the plot

        For example::

          s = SixS()
          s.ground_reflectance = GroundReflectance.HomogeneousWalthall(0.48, 0.50, 2.95, 0.6)
          s.geometry.solar_z = 30
          s.geometry.solar_a = 0
          SixSHelpers.Angles.run_and_plot_360(s, 'view', 'pixel_reflectance')

        """
        if solar_or_view == 'solar':
            show_sun = False

        res = cls.run360(s, solar_or_view, na, nz)
        plot_res = cls.plot360(res, output_name, show_sun, colorbarlabel=colorbarlabel)

        return plot_res

    @classmethod
    def extract_output(cls, results, output_name):
        """Extracts data for one particular SixS output from a list of SixS.Outputs instances.

        Basically just a wrapper around a list comprehension.

        Arguments:

        * ``results`` -- A list of :class:`.SixS.Outputs` instances
        * ``output_name`` -- The name of the output to extract. This should be a string containing whatever is put after the `s.outputs` when printing the output, for example `'pixel_reflectance'`.

        """
        results_output = [getattr(r, output_name) for r in results]

        return results_output

    @classmethod
    def plot_polar_contour(cls, values, azimuths, zeniths, filled=True, colorbarlabel=""):
        """Plot a polar contour plot, with 0 degrees at the North.

        Arguments:

        * ``values`` -- A list (or other iterable - eg. a NumPy array) of the values to plot on the contour plot (the `z` values)
        * ``azimuths`` -- A list of azimuths (in degrees)
        * ``zeniths`` -- A list of zeniths (that is, radii)
        * ``filled`` -- (Optional) Whether to plot a filled contour plot, or just the contours (defaults to filled)
        * ``yaxislabel`` -- (Optional) The label to use for the colorbar
        * ``colorbarlabel`` -- (Optional) The label to use on the color bar shown with the plot

        The shapes of these lists are important, and are designed for a particular use case (but should be more generally useful).
        The values list should be `len(azimuths) * len(zeniths)` long with data for the first azimuth for all the zeniths, then
        the second azimuth for all the zeniths etc.

        This is designed to work nicely with data that is produced using a loop as follows::

          values = []
          for azimuth in azimuths:
            for zenith in zeniths:
              # Do something and get a result
              values.append(result)

        After that code the azimuths, zeniths and values lists will be ready to be passed into this function.

        """
        theta = np.radians(azimuths)
        zeniths = np.array(zeniths)

        values = np.array(values)
        values = values.reshape(len(azimuths), len(zeniths))

        r, theta = np.meshgrid(zeniths, np.radians(azimuths))
        fig, ax = subplots(subplot_kw=dict(projection='polar'))
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        if filled:
            cax = ax.contourf(theta, r, values, 30)
        else:
            cax = ax.contour(theta, r, values, 30)
        cb = fig.colorbar(cax)
        cb.set_label(colorbarlabel)

        return fig, ax, cax

    @classmethod
    def run_principal_plane(cls, s, output_name=None, n=None):
        """Runs the given 6S simulation to get the outputs for the solar principal plane.

        This function runs the simulation for all zenith angles in the azimuthal line of the sun. For example,
        if the solar azimuth is 90 degrees, this function will run simulations for::

          Azimuth   Zenith
          90        85
          90        80
          90        75
          90        70
          90        65
          90        60
          90        55
          ...       ..
          90        0
          270       5
          270       10
          270       15
          ...       ..
          270       80
          270       85

        The calls to 6S for each angle will be run in parallel, making this function far faster than simply
        running a for loop over each angle.

        Arguments:

        * ``s`` -- A :class:`.SixS` instance configured with all of the parameters you want to run the simulation with
        * ``output_name`` -- (Optional) The output name to extract (eg. "pixel_reflectance") if the given data is provided as instances of the Outputs class
        * ``n`` -- (Optional) The number of threads to run in parallel. This defaults to the number of CPU cores in your system, and is unlikely to need changing.

        Return values:

        A tuple containing zenith angles and the corresponding values or Outputs instances (depending on the arguments given).
        The zenith angles returned have been modified so that the zenith angles on the 'sun-side' are positive, and those
        on the other side (ie. past the vertical) are negative, for ease of plotting.

        """

        # Get the solar azimuth and zenith angles from the SixS instance
        sa = s.geometry.solar_a

        # Compute the angles in the principal plane

        # Get the solar azimuth on the opposite side for the other half of the principal plane
        opp_sa = (sa + 180) % 360

        # Calculate the first side (the solar zenith angle side)
        first_side_z = np.arange(85, -5, -5)
        first_side_a = np.repeat(sa, len(first_side_z))

        # Calculate the other side
        temp = first_side_z[:-1]
        second_side_z = temp[::-1]  # Reverse array
        second_side_a = np.repeat(opp_sa, len(second_side_z))

        # Join the two sides together
        all_zeniths = np.hstack((first_side_z, second_side_z))
        all_zeniths_for_return = np.hstack((first_side_z, -1 * second_side_z))
        all_azimuths = np.hstack((first_side_a, second_side_a))

        def f(arg):
            zenith, azimuth = arg
            s.outputs = None
            a = copy.deepcopy(s)

            a.geometry.view_z = zenith
            a.geometry.view_a = azimuth
            a.run()

            if output_name is None:
                return a.outputs
            else:
                return getattr(a.outputs, output_name)

        # Run the map
        if n is None:
            pool = Pool()
        else:
            pool = Pool(n)

        print("Running for many angles - this may take a long time")
        results = pool.map(f, zip(all_zeniths, all_azimuths))
        pool.close()
        pool.join()
        
        results = np.array(results)

        results = np.array(results)

        return all_zeniths_for_return, results

    def plot_principal_plane(zeniths, values, y_axis_label):
        """Plot the results from a principal plane simulation (eg. a run of :meth:`.run_principal_plane`).

        Arguments:

        * ``zeniths`` -- A list of view zenith angles in degrees
        * ``values`` -- A list of simulated values for each of these angles
        * ``y_axis_label`` -- A string to use as the label for the y axis

        """

        plot(zeniths, values)
        xlabel("View zenith angle (degrees)")
        ylabel(y_axis_label)
        show()
