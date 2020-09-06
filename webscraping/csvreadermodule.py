import csv
from datetime import date
today=str(date.today())
filename="covid_Nepal's_report-"+today+".csv"
fields=[]
rows=[]
def reader():
    with open(filename,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        fields=next(csvreader)
        for row in csvreader:
            rows.append(row)
    for field in fields:
        print(field,end=' ')
    for row in rows[:]: 
        for col in row: 
            print("%10s"%col, end=' '), 
        print('\n') 
