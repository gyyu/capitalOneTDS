import pandas as pd
import numpy as np
from sklearn import tree

def predict(features, target, t):
    features_subset = []
    target_subset = []
    print(features)
    print(len(features))
    for x in range(len(features)):
        grade = features[x][1]
        if (int(grade) <= 4):
            print("good")
        else:
            features_subset.append(features[x])
            target_subset.append(target[x]) 
    
    print(t.score(features_subset, target_subset))

# load data sets
data = pd.read_csv("first.csv", encoding = "ISO-8859-1")
test = pd.read_csv("last.csv", encoding = "ISO-8859-1")

# estimators
estimators = ["loan_amnt", "sub_grade", "term", "int_rate", "emp_length", "home_ownership", "annual_inc", "issue_d", "dti", "delinq_2yrs", "open_acc", "total_acc", "initial_list_status"]

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
print(predict(testfeatures, testtarget, t))
