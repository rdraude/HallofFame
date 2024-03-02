import pandas as pd
import numpy as np
from DataPrep import DataPrep

"""
A file for running the K-Nearest Neighbor algorithm on baseball batting data
"""
#Retrieving our data
(famerMap, careerMap, nameMap) = DataPrep()

def eucDistance(X,Z):
    """ 
    Calculates the euclidean distance between input numpy vector(s) Z and each vector in our data X.
    Paramaters: X, Z input NumPy vectors
    Returns: A matrix of vectors with the euclidean distances from each vector in Z to each vector in X
    """
    n,d1=X.shape
    m,d2=Z.shape
    assert (d1==d2), "Inputs do not have matching dimensions"
    G = np.dot(X,Z.T)
    S = np.diag(np.dot(X,X.T))
    S = np.tile(S, (m,1)).T
    R = np.diag(np.dot(Z,Z.T))
    R = np.tile(R, (n,1))
    twoD = S - 2 * G + R
    twoD = np.where(twoD>=0, twoD, np.zeros([n,m]))
    D = np.sqrt(twoD)
    return D