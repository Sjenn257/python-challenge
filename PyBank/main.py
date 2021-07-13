import os

import csv
from datetime import datetime

csv_path=os.path.join("PyBank","Resources","budget_data.csv")

with open(csv_path, newline='',encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    
    for row in csvreader:
        print(row[0],float(row[1]))
