import os

import csv

csv_path=os.path.join("PyBank","Resources","budget_data.csv")

with open(csv_path, newline='',encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    net_profit_total=0
    row_counter=0
    change_diff=0
    prev_date=''
    prev_profit=0
    cumul_change=0
    great_inc_date=''
    great_inc_profit=0
    great_dec_date=''
    great_dec_profit=0
   
    for row in csvreader:
        net_profit_total+=round(float(row[1]),2)
        row_counter+=1

        if row_counter == 1:
            change_diff=float('0')
        else:
            change_diff=float(row[1])-prev_profit
        
        if prev_profit>float(row[1]):
            great_inc_date=prev_date
            great_inc_profit=prev_profit
        else:
            great_inc_date=row[0]
            great_inc_profit=float(row[1])

        #check difference between positive and negative floats
        #may need to separate them
        if prev_profit<float(row[1]):
            great_dec_date=prev_date
            great_dec_profit=prev_profit
        else:
            great_dec_date=row[0]
            great_dec_profit=float(row[1])
        
        cumul_change+=change_diff

        #set up for next row calc
        prev_profit_change=float(row[1])
        prev_date=row[0]

        print(row[0],float(row[1]),row_counter, change_diff, prev_profit)

    average_change=round(cumul_change/float(row_counter),2)
    #works but need to figure out how to skip first data row for change or make it zero

    print("Financial Analysis")
    print("-" * 28)
    print(f"Total Months: {row_counter}")
    print(f"Total: ${net_profit_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_inc_profit})")
    print(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_profit})")
