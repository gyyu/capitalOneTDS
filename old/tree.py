import pandas as pd
import numpy as np
from sklearn import tree

data = pd.read_csv("trainNum2.csv", encoding = "ISO-8859-1")
target = data["loan_status"].values
# print(target)
estimators = ["loan_amnt", "sub_grade", "term", "int_rate", "emp_length", "home_ownership", "annual_inc", "issue_d", "dti", "delinq_2yrs", "open_acc", "total_acc", "initial_list_status"]
features = data[estimators].values

t = tree.DecisionTreeClassifier()
t.fit(features, target)
print(t.feature_importances_)