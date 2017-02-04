import pandas as pd
import numpy as np
from sklearn import tree

data = pd.read_csv("trainNum.csv", encoding = "ISO-8859-1")
test = pd.read_csv("testNum.csv", encoding = "ISO-8859-1")
pred = pd.read_csv("mitophace.csv", encoding = "ISO-8859-1")

target = data["loan_status"].values
# print(target)
estimators = ["loan_amnt", "sub_grade", "term", "int_rate", "emp_length", "home_ownership", "annual_inc", "issue_d", "dti", "delinq_2yrs", "open_acc", "total_acc", "initial_list_status"]
features = data[estimators].values

t = tree.DecisionTreeClassifier()
t.fit(features, target)

ans = t.predict(test[estimators])
#ans = t.predict_proba(test[estimators])

pred['prediction'] = ans
test['loan_status'] = ans

print(ans)
print(t.feature_importances_)

pred.to_csv("mitophace.csv", index=False)
test.to_csv("testNumPred.csv", index=False)