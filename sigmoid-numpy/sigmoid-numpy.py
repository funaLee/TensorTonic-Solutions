import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    np_x = np.asarray(x, dtype=float)
    return 1/(1 + np.exp(-np_x))