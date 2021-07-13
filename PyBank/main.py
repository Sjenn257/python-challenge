import os

import csv
from datetime import datetime

csv_path=os.path.join("PyBank","Resources","budget_data.csv")

with open(csv_path, newline='',encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    net_profit=0
    row_counter=0
    row_diff=0
    change_diff=0
    profit_change=0
    cumul_change=0
   
    for row in csvreader:
        net_profit+=round(float(row[1]),2)
        row_counter+=1

        if row_counter == 1:
            change_diff=float('0')
        else:
            change_diff=float(row[1])-profit_change
        
        cumul_change+=change_diff

        #set up for next row calc
        profit_change=float(row[1])

        print(row[0],float(row[1]),row_counter, change_diff, profit_change)

    average_change=round(cumul_change/float(row_counter),2)
    #works but need to figure out how to skip first data row for change or make it zero

    print("Financial Analysis")
    print("-" * 28)
    print(f"Total Months: {row_counter}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${average_change}")
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")
