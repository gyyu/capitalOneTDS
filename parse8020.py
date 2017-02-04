import pandas as pd
import numpy as np

df = pd.read_csv("first.csv", encoding = "ISO-8859-1")

bad = df[df["loan_status"] == 1]
t = bad.shape
#print(t)
bad = df[df["loan_status"] == 1]
good = df[df["loan_status"] == 0]

bad = bad.head(int(bad.shape[0]/2))

fin = pd.concat([bad, good])

fin.to_csv('firstBad.csv')
#bad.to_csv("balanced.csv")