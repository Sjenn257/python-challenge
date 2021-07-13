import os

import csv
from datetime import datetime

csv_path=os.path.join("PyBank","Resources","budget_data.csv")

with open(csv_path, newline='',encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    net_profit=0
    row_counter=0
   
   

    for row in csvreader:
        # keep total running for each month
        net_profit+=float(row[1])
        row_counter+=1
        print(row[0],float(row[1]),net_profit,row_counter)

    average_change=round(float(net_profit/row_counter),2)

    print("Financial Analysis")
    print("-" * 28)
    print(f"Total Months: {row_counter}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${average_change}")
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")
