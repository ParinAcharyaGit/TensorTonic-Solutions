import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()
    diff = x - y
    dist = np.sqrt(np.sum(diff ** 2))
    return float(dist)