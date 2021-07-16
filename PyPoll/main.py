#expected output
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
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
    winner=''


    for row in csvreader:

        # start to sum the number of votes
        row_counter+=1

        if row[2]=="Khan":
            khan_total+=1
        elif row[2]=="Correy":
            correy_total+=1
        elif row[2]=="Li":
            li_total+=1
        elif row[2]=="O'Tooley":
            otooley_total+=1
        
khan_percent=round(float(khan_total)/float(row_counter)*100,2)
correy_percent=round(float(correy_total)/float(row_counter)*100,2)
li_percent=round(float(li_total)/float(row_counter)*100,2)
otooley_percent=round(float(otooley_total)/float(row_counter)*100,2)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {row_counter}")
print("-------------------------")
print(f"Khan: {khan_percent}% ({khan_total})")
print(f"Correy: {correy_percent}% ({correy_total})")
print(f"Li: {li_percent}% ({li_total})")
print(f"O'Tooley: {otooley_percent}% ({otooley_total})")
print("-------------------------")
print("Winner: ")
print("-------------------------")


#Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------