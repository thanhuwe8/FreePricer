
# from math import exp, sqrt, fabs, log
from numba import njit, boolean, int64, float64, vectorize
import numpy as np

PI = 3.14159265358979323846
INVROOT2PI = 0.3989422804014327

ONE_MILLION = 1000000
TEN_MILLION = 10000000
ONE_BILLION = 1000000000

###############################################################################
# TODO: Move this somewhere else.
###############################################################################



def heaviside(x: float):
    """ Calculate the Heaviside function for x """
    if x >= 0.0:
        return 1.0
    return 0.0

###############################################################################


def NPDF(x: float):
    """ Calculate the probability density function for a Gaussian (Normal)
    function at value x"""
    return np.exp(-x * x / 2.0) * INVROOT2PI

###############################################################################



def NCDF(x):
    """ Fast Normal CDF function based on Hull OFAODS  4th Edition Page 252.
    This function is accurate to 6 decimal places. """

    a1 = 0.319381530
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429
    g = 0.2316419

    k = 1.0 / (1.0 + g * np.abs(x))
    k2 = k * k
    k3 = k2 * k
    k4 = k3 * k
    k5 = k4 * k

    if x >= 0.0:
        c = (a1 * k + a2 * k2 + a3 * k3 + a4 * k4 + a5 * k5)
        phi = 1.0 - c * np.exp(-x*x/2.0) * INVROOT2PI
    else:
        phi = 1.0 - NCDF(-x)

    return phi

###############################################################################


###############################################################################
