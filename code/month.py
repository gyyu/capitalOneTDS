import pandas as pd
import numpy as np

df = pd.read_csv('train.csv')
df = df.head()
d={}

for i, row in df.iterrows():
    if row['issue_d'] not in d.keys():
        d[row['issue_d']] = [0,0]

    if(row["loan_status"]=="Fully Paid" or row["loan_status"]=="In Grace Period" or row["loan_status"]=="Current"):
        d[row['issue_d']][0]+=1
    d[row['issue_d']][1]+=1

#print(d)

df2 = pd.DataFrame.from_dict(d, orient="index")

df2['ratio'] = df2[0] / df2[1]

#print(df2)

df2.to_csv('test2.csv')