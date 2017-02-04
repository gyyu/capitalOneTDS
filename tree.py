import pandas as pd
import numpy as np
from sklearn import tree

def predict(features, target, t):
    predictions = []
    for i in range(len(features)):
        grade = features[i][1]
        if (int(grade) <= 20):
            predictions.append(0)
        else:
            predictions.append(t.predict(features[i])[0])
    print(predictions)
    return predictions

# load data sets
data = pd.read_csv("balanced.csv", encoding = "ISO-8859-1")
test = pd.read_csv("testNum.csv", encoding = "ISO-8859-1")

# estimators
estimators = ["loan_amnt", "sub_grade", "annual_inc", "issue_d", "dti", "open_acc", "total_acc", "home_ownership"]

# train tree
features = data[estimators].values
target = data["loan_status"].values

t = tree.DecisionTreeClassifier()
t.fit(features, target)

# test features and target
testfeatures = test[estimators].values
testtarget = test["loan_status"].values

# run tree
print(t.feature_importances_)
print(t.score(testfeatures, testtarget))
test["prediction"] = predict(testfeatures, testtarget, t)
test.to_csv("model3.csv", encoding = "ISO-8859-1")
