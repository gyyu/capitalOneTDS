import pandas as pd
import numpy as np
import re
import math

sgd1 = {'A':0, "B":1, "C":2, "D":3,"E":4, "F":5, "G":6}
month = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11, "Dec":12}
#print(month)
t = pd.read_csv('test.csv') #input file
#t = t.head()
for i, row in t.iterrows():
    s = row['sub_grade']
    v = sgd1[s[0]]*5 + int(s[1]) - 1
    t.set_value(i,'sub_grade', v)

    #format percentages
    t.set_value(i, "int_rate", row["int_rate"][:-1])
    #print(isinstance(row["revol_util"], str))
    if isinstance(row["revol_util"], str):
        t.set_value(i, "revol_util", row["revol_util"][:-1])

    #term
    if(row["term"] == '36 months'):
        t.set_value(i,'term',0)
    
    else:
        t.set_value(i,'term',1)

    if(row["home_ownership"]=='RENT'):
        t.set_value(i,'home_ownership',0)
    elif(row["home_ownership"]=='OWN'):
        t.set_value(i,'home_ownership',1)
    elif(row["home_ownership"]=='MORTGAGE'):
        t.set_value(i,'home_ownership',2)
    else:
        t.set_value(i,'home_ownership',3)
    
    mon  =row['issue_d'][:3]
    yr = row['issue_d'][6:8]
    t.set_value(i,'issue_d', (9-month[mon])+12*(16-int(yr)) ) #relative to 
    
    if(row["loan_status"]=="Fully Paid" or row["loan_status"]=="In Grace Period" or row["loan_status"]=="Current"):
        t.set_value(i, "loan_status", 0)
    else:
        t.set_value(i, "loan_status", 1)

    if(row['initial_list_status']=='f'):
        t.set_value(i, "initial_list_status", 0)
    else:
        t.set_value(i, "initial_list_status", 1)

    e = row['emp_length']
    match = re.findall('\d+',e)
    if(len(match)>0):
        t.set_value(i, "emp_length", match[0])
    else:
        t.set_value(i, "emp_length", -1)
#print(t)
t.to_csv("testNum.csv", index=False)
#print(t)