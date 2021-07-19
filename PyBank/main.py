import os

import csv

csv_path=os.path.join("PyBank","Resources","budget_data.csv")

with open(csv_path, newline='',encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    net_profit_total=0
    row_counter=0
    change_diff=0
    prev_profit=0
    cumul_change=0
    great_inc_date=''
    great_inc_profit=0
    great_dec_date=''
    great_dec_profit=0
   
    for row in csvreader:

        # start to sum each profit to get total at the end
        net_profit_total+=round(float(row[1]),2)

        # keeping track of which row and to get total count
        row_counter+=1

        # calculating the profit change from previous date except for the first row
        if row_counter == 1:
            change_diff=float('0')
        else:
            change_diff=float(row[1])-prev_profit

        # start to sum each change in profit in order to get an average change in the end which will be (total of changes/count in the end)
        cumul_change+=change_diff
        
        # getting the greatest increase data and putting it in placeholder until a new greater increase is found
        if float(row[1])>great_inc_profit:
            great_inc_date=row[0]
            great_inc_profit=float(row[1])
        
        # getting the greatest decrease data and putting it in a placeholder until a new greater decrease is found

        #check difference between positive and negative floats
        #may need to separate them
        if float(row[1])<great_dec_profit:
            great_dec_date=row[0]
            great_dec_profit=float(row[1])
                
        # put in placeholder to use in next loop for next row calculation
        prev_profit=float(row[1])
        

    # assign variable to average change calculation with whatever the cumul_change and row counter ended up as
    average_change=round(cumul_change/float(row_counter),2)


# Specify the file to write to
output_path = os.path.join("PyBank","analysis.txt")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-" * 28])
    csvwriter.writerow([f"Total Months: {row_counter}"])
    csvwriter.writerow([f"Total: ${net_profit_total}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {great_inc_date} (${great_inc_profit})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_profit})"])

    print(" ",end = "\r\n")
    print("Financial Analysis")
    print("-" * 28)
    print(f"Total Months: {row_counter}")
    print(f"Total: ${net_profit_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_inc_profit})")
    print(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_profit})")
    print(" ",end = "\r\n")
    print("Results were saved in PyBank/analysis.txt", end = "\r\n")
    print(" ",end = "\r\n")

