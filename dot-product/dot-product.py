import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    return float(np.dot(x,y))

    # manual method
    # dot_product = 0
    # x = np.asarray(x).ravel()
    # y = np.asarray(y).ravel()
    # for i in range(len(x)):
    #     dot_product += x[i] * y[i]

    # return float(dot_product)
