import pandas as pd
import numpy as np
"""
A file for scraping aggregate data into data structures which match a player to their career information
"""

#Loading in csv data
Famers = pd.read_csv("~/hall/HallofFame/Data/HallOfFame.csv").T
Seasons = pd.read_csv("~/hall/HallofFame/Data/Batting.csv").T
Players = pd.read_csv("~/hall/HallofFame/Data/People.csv").T

def famerMap():
    """
    Returns: The dictionary containing hall of famers
    """
    famerMap = {}
    for hf in Famers:
        ID = Famers.iloc[0, hf]
        famerMap.update({ID : 1})
    return famerMap

def careerMap():
    """
    Returns: The hashmaps from playerID's to their career batting statistics
    """
    careerMap = {}
    for player in Seasons:
        item = careerMap.get(Seasons.iloc[0, player] , [])
        if (item == []):
            careerMap.update({Seasons.iloc[0, player] : Seasons.iloc[5: , player].to_numpy()})
        else:
            careerMap.update({Seasons.iloc[0, player] : item + Seasons.iloc[5: , player].to_numpy()})
    return careerMap

def nameMap():
    """
    Returns: The hashmap from playerID's to their name
    """
    nameMap = {}
    for pl in Players:
        nameMap.update({Players.iloc[0, pl] : str(Players.iloc[13, pl]) + " " + str(Players.iloc[14, pl])})
    return nameMap

def DataPrep():
    """
    Outputs a tuple with the hashmaps from playerID's to hall of famers, playerID's to their career batting statistics, 
    and playerID's to their names, in that order
    Returns: A tuple with hashMaps of hall of famers, career statistics, and names to playerID's
    """
    return (famerMap(), careerMap(), nameMap())