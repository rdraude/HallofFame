import numpy as np
# import unittest
from nNeighbor import eucDistance
from nNeighbor import nNeighbor
from DataPrep import DataPrep

#Creating a normalization array to multiply our data by
normDiv = np.array([1/3562, 1/14053, 1/2295, 1/4256, 1/792, 1/309, 1/762, 1/2297, 1/1406, 1/335, 1/2558, 1/2597, 1/688, 1/287, 1/512, 1/128, 1/426, 1/234])

#Retrieving our data for testing
(famerMap, careerMap, careerIndList, nameMap) = DataPrep()

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

def NeighborTests():
    """
    Some basic tests to check that our K-NN algorithm functions as intended
    """
    inH, niH, names = nNeighbor(normDiv * np.array([careerMap.get("bondsba01")]) , 3, False)
    print(names)
    print("Are names different for Barry Bonds when we say it IS a player input?")
    inH2, niH2, names2 = nNeighbor(normDiv * np.array([careerMap.get("bondsba01")]) , 3, True, "bondsba01")
    print(names2)
    print("Now Olerud:")
    inH, niH, names = nNeighbor(normDiv * np.array([careerMap.get("olerujo01")]) , 3, False)
    print(names)
    print("Are names different for John Olerud when we say it IS a player input?")
    inH2, niH2, names2 = nNeighbor(normDiv * np.array([careerMap.get("olerujo01")]) , 3, True, "olerujo01")
    print(names2)


DistanceTests()
print("We've passed all distance tests")
DataTests()
print("We've passed all data preparation tests")
NeighborTests()