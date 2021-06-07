import numpy as np
import pandas as pd
from scipy.interpolate import interp1d


def import_from_excel(filename, sheetid):
    df = pd.read_excel(filename, sheetid)
    f = interp1d(df.iloc[:, 0], df.iloc[:, 1])
    minwv = df.iloc[:, 0].min()

    newwvs = np.arange(minwv, df.iloc[:, 0].max(), 2.5)

    maxwv = newwvs.max()

    values = f(newwvs)

    print("%.3f, %.3f,\nnp.%s)" % (minwv / 1000.0, maxwv / 1000.0, values.__repr__()))


def process_band(df, bandid):
    data = df[[0, bandid]]
    data.columns = [0, 1]
    f = interp1d(data.iloc[:, 0], data.iloc[:, 1])

    indices = np.where(data.iloc[:, 1] > 0.001)[0]
    print(indices)
    minwv = data.iloc[indices.min(), 0]
    maxwv = data.iloc[indices.max(), 0]
    newwvs = np.arange(minwv, maxwv, 2.5)

    values = f(newwvs)

    values[values < 0.001] = 0.0

    print("%.3f, %.3f,\nnp.%s)" % (minwv / 1000.0, maxwv / 1000.0, values.__repr__()))
