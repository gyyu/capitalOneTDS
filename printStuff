import pandas as pd
import math

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
gradesL= ["A", "B", "C", "D", "E", "F", "G"]
train = pd.read_csv("trainNum.csv")
#print(train["issue_d"].value_counts())
#print(train.dtypes)


train["Verdict"] = 0
train["Verdict"][train["loan_status"]=="Late (31-120 days)"]=1
train["Verdict"][train["loan_status"]=="Late (16-30 days)"]=1
train["Verdict"][train["loan_status"]=="Charged Off"]=1

#df = train["issue_d"]
#list1 = []
#list2 = []
"""for yr in range(2007, 2017):
	for mon in months:
		#date_string = str(mon) + "/1/" + str(yr)
		date_string = str(mon) + "-" + str(yr)
		print(date_string)
		count = train["Verdict"][train["issue_d"]==date_string].value_counts(normalize = True)
		print(count)
		count.to_csv("out.csv")
		#list1.append(train["Verdict"][train["issue_d"]==date_string].value_counts(normalize = True))
		"""
"""for g in gradesL:
	for i in range(1, 6):
		gradeS = g + str(i)
		count = train["Verdict"][train["sub_grade"]==gradeS].value_counts(normalize=True)
		
		#print(count[0])

		print(gradeS)
		print(count)"""

for i in range(20):
	count = train["Verdict"][train["int_rate"]>float(i)][train["int_rate"]<float(i+1)].value_counts(normalize=True)
	print(i)
	print(count)


#for i in range(1, 100):
	#print(train["Verdict"][train["delinq_2yrs"]==i].value_counts(normalize=True))
#print(train["Verdict"][train["initial_list_status"]=="w"].value_counts(normalize=True))



#train.round({'dti':0})
#print(train.head())

"""for i in range(20):
	for g in gradesL:
		for j in range(1, 6):
			gradeS = g + str(j)
			count = train["Verdict"][train["sub_grade"]==gradeS][train["dti"]>float(i*5)][train["dti"]<float(i*5)+5.0].value_counts(normalize=True)
			#if count["0"]<0.5:
			if(count.size==2):
				if(count[0]<0.5):
					print(gradeS)
					print(str(i*5) + "-"+str(i*5+5))
					print(count)"""

#print(train["Verdict"][train["verification_status"]=="Not Verified"].value_counts(normalize=True))

"""print(train["Verdict"][train["home_ownership"]=="OWN"].value_counts(normalize=True))
print(train["Verdict"][train["home_ownership"]=="RENT"].value_counts(normalize=True))
print(train["Verdict"][train["home_ownership"]=="MORTGAGE"].value_counts(normalize=True))"""




