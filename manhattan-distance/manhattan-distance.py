import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x, y = np.asarray(x).ravel(), np.asarray(y).ravel()
    dist = np.sum(np.abs(x - y)) # elementwise arithmetic
    return float(dist)