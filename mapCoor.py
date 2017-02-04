import pandas as pd
import numpy as np

f = open('googleCoor.txt', 'w')

mapData = pd.read_csv('mapData.csv')

lng = mapData['LNG'].values
lat = mapData['LAT'].values

for x in range(len(lng)):
    f.write("{location: new google.maps.LatLng(" + 
                        str(lat[x]) + ", " +str(lng[x])+"), weight: 1},")

f.close() #close the file