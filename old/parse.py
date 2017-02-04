import pandas as pd
import numpy as np

df = pd.read_csv('train.csv') #input file



tempDf = df.head(n=30)


tempDf['sub_grade'] = tempDf['sub_grade'].astype('category')

cat_columns = tempDf.select_dtypes(['category']).columns

tempDf[cat_columns] = tempDf[cat_columns].apply(lambda x: x.cat.codes)

print(tempDf['sub_grade'])

"""
m = np.array(tempDf)

s = set(m[:,5])

e = np.zeros(len(m[:,5]))

for i,name in enumerate(s):
    e[m[:,5]==name] = int(i)

tempDf['sorted'] = e
"""
#print(tempDf)
#print(tempDf.dtypes)
#m['sub_grade']
#print(m)
#cols_to_transform = [ 'subgrade', 'term', 'home_owner' ]
#df_with_dummies = pd.get_dummies(tempDf, columns = cols_to_transform )


#

#print(cat_columns)

#

#sprint(tempDf.dtypes)

#print('result')
#print(tempDf['sub_grade'].cat.codes)