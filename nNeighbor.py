import pandas as pd
import numpy as np
from DataPrep import DataPrep
from sklearn.preprocessing import normalize

"""
A file for running the K-Nearest Neighbor algorithm on baseball batting data
"""
#Retrieving our data
(famerMap, careerMap, careerIndList, nameMap) = DataPrep()
# Converting our dictionary into a normalized numPy array
bigVec = np.array(list(careerMap.values()))
# careerVec = bigVec / bigVec.max(axis=0)
bigVec = np.nan_to_num(bigVec, 0.0)
careerVec = normalize(bigVec, axis=0, norm='max')



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

def nNeighbor(input, k, player = False, inpID = ""):
    """
    nNeighbor(input, k, player, inpID) finds the n nearest players to input statistics
    k, and returns how many of those are in the hall of fame, how many aren't, 
    and those players names.
    
    Finds the k nearest neighbors of input in careerVec
    
    Input:
    input: one numPy row vector of dimensionality 18
    k: the number of nearest neighbors we want
    player: true if the user inputted a player name, false if precise statistics
    inpID: the player ID of the input play, empty string if no input player
    
    Output:
    indices = (k, m) matrix, where indices(i,j) is the i^th nearest neighbor of xTe(j,:)
    inHall: number of the k nearest neighbors in the hall of fame
    notIn: number of the k nearest neighbors not in the hall of fame
    playerNames: names of the k nearest players to the input
    """
    D = eucDistance(careerVec, input) 
    indices = np.argsort(D,axis=0)
    playerIDs = []
    playerNames = []
    inHall = 0
    notIn = 0
    for i in range(k+1): #Finding the k nearest neighbors, plus an extra if input was a player and not statistics
        playerIDs.append(careerIndList[indices[i,0]])
    end = k
    if (player): #Checking if input was a player, don't want to check the player with himself (same statistics)
        end += 1
    for pl in playerIDs[:end]:
        if (pl == inpID): continue
        playerNames.append(nameMap.get(pl))
        fame = famerMap.get(pl, 0)
        if (fame == 0):
            notIn += 1
        elif (fame == 1):
            inHall += 1
        else: print("famerMap error")
    return inHall, notIn, playerNames