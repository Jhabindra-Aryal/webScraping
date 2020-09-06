import csv
from datetime import date
today=str(date.today())
fields=['New Cases',"Today's Recovered","Today's Deaths","Toal Cases","Total Infected","Total Recovered","Total Deaths"]
def csvwrite(rows):
    filename="covid_Nepal's_report-"+today+".csv"
    with open(filename,'w') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)