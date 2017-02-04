import pandas as pd
import numpy as np
from sklearn import tree

data = pd.read_csv("../trainNum.csv")
target = data["loan_status"].values
# print(keys)
features = data[["int_rate", "annual_inc"]].values
# print(interest)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, target)
print(clf.feature_importances_)
print(clf.score(features, target))
