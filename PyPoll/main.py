import os

import csv

csv_path=os.path.join("PyPoll","Resources","election_data.csv")

with open(csv_path, newline='',encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    row_counter=0
    khan_total=0
    correy_total=0
    li_total=0
    otooley_total=0
    winner=""


    for row in csvreader:

        # start to sum the number of votes
        row_counter+=1

        # count rows for each candidate's vote
        if row[2]=="Khan":
            khan_total+=1
        elif row[2]=="Correy":
            correy_total+=1
        elif row[2]=="Li":
            li_total+=1
        elif row[2]=="O'Tooley":
            otooley_total+=1
        
# Figure out percentages of votes for each candidate
khan_percent=round(float(khan_total)/float(row_counter)*100,2)
correy_percent=round(float(correy_total)/float(row_counter)*100,2)
li_percent=round(float(li_total)/float(row_counter)*100,2)
otooley_percent=round(float(otooley_total)/float(row_counter)*100,2)

#find which candidate had the most votes
if khan_total>correy_total:
    if khan_total>li_total:
        if khan_total>otooley_total:
            winner="Kahn"
if correy_total>khan_total:
    if correy_total>li_total:
        if correy_total>otooley_total:
            winner="Correy"
if li_total>khan_total:
    if li_total>correy_total:
        if li_total>otooley_total:
            winner="Li"
if otooley_total>khan_total:
    if otooley_total>li_total:
        if otooley_total>correy_total:
            winner="O'Tooley"

            
# print results

# Specify the file to write to
output_path = os.path.join("PyPoll","results.txt")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {row_counter}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Khan: {khan_percent}% ({khan_total})"])
    csvwriter.writerow([f"Correy: {correy_percent}% ({correy_total})"])
    csvwriter.writerow([f"Li: {li_percent}% ({li_total})"])
    csvwriter.writerow([f"O'Tooley: {otooley_percent}% ({otooley_total})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])

print(" ",end = "\r\n")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {row_counter}")
print("-------------------------")
print(f"Khan: {khan_percent}% ({khan_total})")
print(f"Correy: {correy_percent}% ({correy_total})")
print(f"Li: {li_percent}% ({li_total})")
print(f"O'Tooley: {otooley_percent}% ({otooley_total})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
print("Results were saved in results.txt", end = "\r\n")
print(" ",end = "\r\n")