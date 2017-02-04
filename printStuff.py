import pandas as pd
import math

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
gradesL= ["A", "B", "C", "D", "E", "F", "G"]
train = pd.read_csv("trainNum.csv", encoding="ISO-8859-1")
#print(train["issue_d"].value_counts())
#print(train.dtypes)

"""
train["Verdict"] = 0
train["Verdict"][train["loan_status"]=="Late (31-120 days)"]=1
train["Verdict"][train["loan_status"]=="Late (16-30 days)"]=1
train["Verdict"][train["loan_status"]=="Charged Off"]=1"""

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

for int_rate in range(50):
	print(int_rate)
	for grade in range(30):
		print(grade)
		for loanAmount in range(0, 102000, 20000):
			for income in range(0, 202000, 10000):
				print(income)
				for dti in range(0, 110, 10):
					count = train["loan_status"][train["int_rate"]>float(int_rate)][train["int_rate"]<float(int_rate+1)][train["sub_grade"]==grade][train["loan_amnt"]>loanAmount][train["loan_amnt"]<loanAmount+2000][train["annual_inc"]>income][train["annual_inc"]<income+2000][train["dti"]>dti][train["dti"]<dti+5]
					#count = train["loan_status"][train["int_rate"]>float(int_rate)][train["int_rate"]<float(int_rate+1)].value_counts(normalize=True)
					if(count.size==2):
						if(count[0]<0.5):
							print(dti, income, loanAmmount, grade, int_rate)
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




