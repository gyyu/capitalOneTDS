import pandas as pd
import numpy as np

df = pd.read_csv('trainNum.csv', encoding = "ISO-8859-1")
#df = df.head()
d={}
d2={}

for i, row in df.iterrows():
    """
    if row['issue_d'] not in d.keys():
        d[row['issue_d']] = [0,0]

    if(row["loan_status"]==0):
        d[row['issue_d']][0]+=1
    d[row['issue_d']][1]+=1
    """
    if row['sub_grade'] not in d2.keys():
        d2[row['sub_grade']] = [0,0]

    if(row["loan_status"]==0):
        d2[row['sub_grade']][0]+=1
    d2[row['sub_grade']][1]+=1
#print(d)

#df2 = pd.DataFrame.from_dict(d, orient="index")
df22 = pd.DataFrame.from_dict(d2, orient="index")


#df2['ratioIssue'] = df2[0] / df2[1]
df22['ratioGrade'] = df22[0] / df22[1]

#final = pd.DataFrame(index=index, columns=columns)


#final = df22['ratioGrade']
#final['Grades'] = d2.keys()

#print(df2)
#print(final)
#final.to_csv('prop.csv', index=False)
print(df22)
df22.to_csv('prop.csv')