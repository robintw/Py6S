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
from scipy.interpolate import interp1d
import dateutil.parser
import warnings
from Py6S import *


class Aeronet:

    """Contains functions for importing AERONET measurements to set the 6S aerosol profile."""

    @classmethod
    def import_aeronet_data(cls, s, filename, time):
        """Imports data from an AERONET data file to a given SixS object.

        This requires a valid AERONET data file and the `pandas` package (see http://pandas.pydata.org/ for
        installation instructions).

        The type of AERONET file required is a *Combined file* for All Points (Level
        1.5 or 2.0)

        To download a file like this:

        1. Go to http://aeronet.gsfc.nasa.gov/cgi-bin/webtool_opera_v2_inv

        2. Choose the site you want to get data from

        3. Tick the box near the bottom labelled as "Combined file (all products without phase functions)"

        4. Choose either Level 1.5 or Level 2.0 data. Level 1.5 data is unscreened, so contains far more data meaning it is more likely for you to find data near your specified time.

        5. Choose All Points under Data Format

        6. Download the file

        7. Unzip

        8. Pass the filename to this function


        Arguments:

        * ``s`` -- A :class:`.SixS` instance whose parameters you would like to set with AERONET data
        * ``filename`` -- The filename of the AERONET file described above
        * ``time`` -- The date and time of the simulation you want to run, used to choose the AERONET data which is closest
          in time. Provide this as a string in almost any format, and Python will interpret it. For example, ``"12/03/2010 15:39"``. When dates are ambiguous, the parsing routine will favour DD/MM/YY rather than MM/DD/YY.

        Return value:

        The function will return ``s`` with the ``aero_profile`` and ``aot550`` fields filled in from the AERONET data.

        Notes:

        Beware, this function makes a number of assumptions and performs a number of possibly-inaccurate steps.

        1. The refractive indices for aerosols are only provided in AERONET data at a few wavelengths, but 6S requires
        them at 20 wavelengths. Thus, the refractive indices are extrapolated outside of their original range, to provide
        the necessary data. This is generally not a wonderful idea, but it is the only way to be able to use the data
        within 6S. In many cases the refractive indices seem to change very little - but please do check this yourself!

        2. The AERONET AOT measurement at the wavelength closest to 550nm (the wavelength required for the AOT
        specification in 6S) is used. This varies depending on the AERONET site, but may be 50-100nm (or more) away
        from 550nm. In future versions this code will interpolate the AOT at 550nm using the Angstrom coefficent.

        """
        try:
            import pandas
        except ImportError:
            raise ImportError("Importing AERONET data requires the pandas module. Please see http://pandas.pydata.org/ for installation instructions.")

        # Load in the data from the file
        try:
            df = pandas.read_csv(filename, skiprows=3, na_values=["N/A"])
        except:
            raise ParameterError("AERONET file", "Error reading AERONET file - does it exist and contain data?")

        # Parse the dates/times properly and set them up as the index
        df['Date(dd-mm-yyyy)'] = df['Date(dd-mm-yyyy)'].apply(cls._to_iso_date)
        df['timestamp'] = df.apply(lambda s: pandas.to_datetime(s['Date(dd-mm-yyyy)'] + " " + s['Time(hh:mm:ss)']), axis=1)
        df.index = pandas.DatetimeIndex(df.timestamp)

        given_time = dateutil.parser.parse(time, dayfirst=True)

        df['timediffs'] = np.abs(df.timestamp - given_time).astype('timedelta64[ns]')

        # Get the AOT data at the closest time that has AOT
        # (may be closer to the given_time than the closest
        # time that has full aerosol model information)
        aot = cls._get_aot(df)
        # print "AOT = %f" % aot

        refr_ind, refi_ind, wvs, radii_ind, radii = cls._get_model_columns(df)

        # Get the indices we're interested in from the main df
        inds = refr_ind + refi_ind + radii_ind + [len(df.columns) - 1]

        # and put them into a smaller df for just the aerosol-model-related components
        model_df = df.ix[:, inds]
        # Get rid of rows which don't have a full set of data
        model_df = model_df.dropna(axis=0, how='any')

        if model_df.shape[0] == 0:
            raise ValueError("No non-NaN data for aerosol model available in AERONET file.")

        # And get the closest to the given time
        rowind = model_df.timediffs.idxmin()

        # Extract this row as a series
        ser = model_df.ix[rowind]
        # Get the new relevant indices for this smaller df
        refr_ind, refi_ind, wvs, radii_ind, radii = cls._get_model_columns(model_df)

        wvs = np.array(wvs) / 1000.0

        # Interpolate both the real and imag parts of the refractive index
        # at the 6S wavelengths from the wavelengths given in the AERONET file
        sixs_wavelengths = [0.350, 0.400, 0.412, 0.443, 0.470, 0.488, 0.515, 0.550, 0.590, 0.633, 0.670, 0.694, 0.760,
                            0.860, 1.240, 1.536, 1.650, 1.950, 2.250, 3.750]

        refr_values = ser[refr_ind]
        f_interp_real = interp1d(wvs, refr_values, bounds_error=False)
        final_refr = f_interp_real(sixs_wavelengths)
        final_refr = pandas.Series(final_refr)
        final_refr = final_refr.fillna(method='pad')
        final_refr = final_refr.fillna(method='bfill')

        refi_values = ser[refi_ind]
        f_interp_imag = interp1d(wvs, refi_values, bounds_error=False)
        final_refi = f_interp_imag(sixs_wavelengths)
        final_refi = pandas.Series(final_refi)
        final_refi = final_refi.fillna(method='pad')
        final_refi = final_refi.fillna(method='bfill')

        dvdlogr = ser[radii_ind]

        s.aot550 = aot
        s.aero_profile = AeroProfile.SunPhotometerDistribution(radii, dvdlogr, final_refr, final_refi)

        return s

    @classmethod
    def _get_model_columns(cls, df):
        refr_ind = []
        refi_ind = []
        wvs = []
        radii_ind = []
        radii = []

        for i, col in enumerate(df.columns):
            if "REFR" in col:
                refr_ind.append(i)
            elif "REFI" in col:
                refi_ind.append(i)
                wv = int(col.replace("REFI", "").replace("(", "").replace(")", ""))
                wvs.append(wv)
            else:
                try:
                    rad = float(col)
                except:
                    continue
                radii_ind.append(i)
                radii.append(rad)

        return refr_ind, refi_ind, wvs, radii_ind, radii

    @classmethod
    def _to_iso_date(cls, s):
        """Converts the date which is, bizarrely, given as dd:mm:yyyy to the ISO standard
        of yyyy-mm-dd."""
        spl = s.split(":")
        spl.reverse()

        return "-".join(spl)

    @classmethod
    def _get_aot(cls, df):
        """Gets the AOT data from the AERONET dataset, choosing the AOT at the closest time
        to the time requested, and choosing the AOT measurement at the wavelength closest
        to 550nm."""
        wvs = []
        inds = []

        for i, col in enumerate(df.columns):
            if "AOT_" in col:
                inds.append(i)

        inds.append(len(df.columns) - 1)
        inds = np.array(inds)

        # Remove the columns for AOT wavelengths with no data
        aot_df = df.ix[:, inds]
        aot_df = aot_df.dropna(axis=1, how='all')
        aot_df = aot_df.dropna(axis=0, how='any')

        wvs = []
        inds = []
        for i, col in enumerate(aot_df.columns):
            if "AOT_" in col:
                wvs.append(int(col.replace("AOT_", "")))
                inds.append(i)

        wvs = np.array(wvs)
        inds = np.array(inds)

        wv_diffs = np.abs(wvs - 550)

        aot_col_index = wv_diffs.argmin()

        if (wv_diffs[aot_col_index] > 70):
            warnings.warn("Using AOT measured more than 70nm away from 550nm as nothing closer available - could cause inaccurate results.")

        rowind = aot_df.timediffs.idxmin()

        aot = aot_df.ix[rowind, aot_col_index]

        return aot
