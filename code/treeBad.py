import pandas as pd
import numpy as np
from sklearn import tree
import pydotplus
import os
'''
def predict(features, target, t):
    features_subset = []
    target_subset = []
    for row in features:
        grade = row[1]
        if (int(grade) <= 4):
            print("good")
        else:
            features_subset.append(row)
            target_subset.append(target[i])
    print(t.score(features_subset, target_subset))
'''

# load data sets
data = pd.read_csv("balanced.csv", encoding = "ISO-8859-1")
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

guess = t.predict(testfeatures)

#f = pd.DataFrame({'guess': guess, "answers": testtarget})

#f.to_csv('brierTest.csv', index=False)
compare = [] 
for x in range(len(guess)):
    if guess[x]!=testtarget[x]:
        compare.append('WRONG')
    else:
        compare.append("RIGHT")

test['RESULT'] = compare

test.to_csv("resultsTest.csv")

# run tree
print(t.feature_importances_)
print(t.score(testfeatures, testtarget))

#dot_data = tree.export_graphviz(t, out_file='display.dot') 
#graph = pydotplus.graph_from_dot_data(dot_data) 
#print("writing pdf")
#graph.write_pdf("image.pdf") 
