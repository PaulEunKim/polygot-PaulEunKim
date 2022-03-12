# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:18:39 2021

@author: paule
"""
# Write you web scraping code here.

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

dr = webdriver.Chrome(executable_path='C:/Users/paule/Chrome Driver/chromedriver.exe')

dr.get("https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1")

bs = BeautifulSoup(dr.page_source,"html5")

# pre-build data frame
playerDf = pd.DataFrame(columns = ["index", "name", "team", "age", "gp", "w", "l", "min", "pts",
                                   "fgm", "fga", "fgp", "threepm", "threepa", "threepp", "ftm", "fta", "ftp", 
                                   "oreb", "dreb","reb","ast","tov", "stl", "blk", "pf", "fp", 
                                   "dd2", "td3", "plusminus"])

# find all elements that are table rows 'tr'
listOfRows = bs.find_all('tr')

# for each tr, there are several td that represent the statistics for a player
for tr in listOfRows:
    tdList = tr.findChildren("td")
    player = []
    
    # first put all stats into array called player
    for td in tdList:
        player.append(td.get_text().strip())
    
    # sanity check to see what kind of data is being scraped
    print(len(player))
    
    # if player has 30 attributes as expected, then input into data frame 
    if(len(player) == 30):
        data = {"index": player[0], "name": player[1], "team": player[2], "age": player[3], "gp": player[4], "w": player[5], "l": player[6], "min": player[7], "pts": player[8], 
                "fgm": player[9], "fga": player[10], "fgp": player[11], "threepm": player[12], "threepa": player[13], "threepp": player[14], "ftm": player[15], "fta": player[16], "ftp": player[17], 
                "oreb": player[18], "dreb": player[19],"reb": player[20],"ast": player[21],"tov": player[22], "stl": player[23], "blk": player[24], "pf": player[25], "fp": player[26], 
                "dd2": player[27], "td3": player[28], "plusminus": player[29]}    
        playerDf = playerDf.append(data, ignore_index=True)

playerDf.to_csv('../R/App/data/nba.csv')
    

   