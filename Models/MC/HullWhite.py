from PackagesSetup import *
from enum import Enum

class OptionTypeSwap(Enum):
    RECEIVER = 1.0
    PAYER = -1.0


def GeneratePathsHWEuler(nPaths, nSteps, T, P0T, lambd, eta):
    
    dt = 0.0001
    f0T = lambda t: -(np.log(P0T(t+dt)))
    