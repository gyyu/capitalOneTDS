import pandas as pd
#import xlrd
#book = xlrd.open_workbook("brierTest.csv")


scores = pd.read_csv("brierTest.csv")

score = 0
ind = 0

#sheet = book.sheet_by_index(0)
#for row in range(10002):



for row in scores.iterrows():
	#print(type(row[1]))
	#print(row[1][0])
	score += (float(row[1][1])-float(row[1][0]))*(float(row[1][1])-float(row[1][0]))
	#score += float(row[1][1])*float(row[1][1])
	ind+=1
print(score/ind)