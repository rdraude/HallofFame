import pandas as pd
import numpy as np
#Loading in csv data
Famers = pd.read_csv("~/hall/HallofFame/Data/HallOfFame.csv").T
Seasons = pd.read_csv("~/hall/HallofFame/Data/Batting.csv").T

#Returns the dictionary containing hall of famers
def famerMap():
    famerMap = {}
    for hf in Famers:
        ID = Famers.iloc[0, hf]
        famerMap.update({ID : 1})
    return famerMap

#Returns the hashmaps from playerID's to their career batting statistics
def careerMap():
    careerMap = {}
    for player in Seasons:
        item = careerMap.get(Seasons.iloc[0, player] , [])
        if (item == []):
            careerMap.update({Seasons.iloc[0, player] : Seasons.iloc[5: , player].to_numpy()})
        else:
            careerMap.update({Seasons.iloc[0, player] : item + Seasons.iloc[5: , player].to_numpy()})
    return careerMap

#Returns the hashmaps from playerID's to hall of famers and playerID's to their career batting statistics
def DataPrep():
    return famerMap(), careerMap()