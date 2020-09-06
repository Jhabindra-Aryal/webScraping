import scrapping
import csvwritermodule
import csvreadermodule
record=[]
newcases=recoveredtoday=deathstoday=totalcase=totalinfected=totalrecovered=totaldeath=0
paragraph=scrapping.beautifulsoup().find_all('p')
for i in range(len(paragraph)):
	record.append(paragraph[i].contents)

	if record[i][0]=='New Cases':
		newcases=record[i-1][0]
	elif record[i][0]=='Recovered' and i<6:
		recoveredtoday=record[i-1][0]
	elif record[i][0]=='Deaths' and i<6:
		deathstoday=record[i-1][0]
	elif record[i][0]=='Total Cases':
		totalcase=record[i-1][0]
	elif record[i][0]=='Total Infected':
		totalinfected=record[i-1][0]
	elif record[i][0]=='Recovered':
		totalrecovered=record[i-1][0]
	elif record[i][0]=='Deaths':
		totaldeath=record[i-1][0]

	else:
		message="no further record"

rows=[[newcases,recoveredtoday,deathstoday,totalcase,totalinfected,totalrecovered,totaldeath]]
	

csvwritermodule.csvwrite(rows) #Writing to csv file
csvreadermodule.reader()#Reading from csv file