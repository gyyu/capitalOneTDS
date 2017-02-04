import pandas as pd
import numpy as np
from sklearn import tree

mapData = pd.read_csv('train.csv', usecols = [0, 21, 22]) #input file
zips = pd.read_csv('zipCodes.csv')

zipNum = zips['ZIP'].values
xVal  = zips['LAT'].values
yVal = zips['LNG'].values

d = {zipNum[t]: [xVal[t], yVal[t]] for t in range(len(zipNum))}

x = []
y = []

for a in mapData.iterrows():
    k = a[1]['zip_code']
    k = int(k[0:3])*100 #get the numbers
    finding = True
    while finding ==True:
        if(k in d.keys()):
            x.append(d[k][0])
            y.append(d[k][1])
            finding = False
        k+=1 #try next zip

#print(x)

mapData["LAT"] = x
mapData['LNG'] = y

mapData.to_csv('mapData.csv')