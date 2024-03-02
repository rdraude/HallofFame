import numpy as np
# import unittest
from nNeighbor import eucDistance
from DataPrep import DataPrep

#Retrieving our data for testing
(famerMap, careerMap, nameMap) = DataPrep()

"""
A script for some basic tests for our data preparation and distance calculation
"""

def DistanceTests():
    """
    Some basic tests of our euclidean distance function. Errors out on assertion if any fail.
    """
    x1=np.array([[0,1]])
    x2=np.array([[1,0]])
    x1.shape
    x2.shape
    assert(abs(np.linalg.norm(eucDistance(x1,x2)[0,0]-np.sqrt(2)))<1e-9)
    assert(abs(np.linalg.norm(eucDistance(x2,x2)[0,0]))<1e-9)

    ###
    ###

def DataTests():
    """
    Some basic tests to check that our data collection is correct. Errors on assertion if any fail.
    Mostly important for our career statistics, because we only had access to season-by-season data,
    and had to combine it to get career statistics.
    """
    #All time home run leader aggregation check
    assert(careerMap["bondsba01"][6] == 762)
    #All time hits leader aggregation check
    assert(careerMap["rosepe01"][3] == 4256)
    


DistanceTests()
print("We've passed all distance tests")
DataTests()
print("We've passed all data preparation tests")