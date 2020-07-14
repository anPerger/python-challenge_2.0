import csv
import os
import sys

csvpath = os.path.join("Resources", "budget_data.csv")

stdoutOrigin=sys.stdout # Method I found on stackoverflow to export results
sys.stdout = open("log.txt", "w") # to a .txt file

rowcount = 0
net_total = 0
last_row = 0
start_profit = 0
current_row = 0
diff = 0  
changes = []  
biggest_increase = 0
biggest_decrease = 0

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        
        current_row = row[1]       
        net_total += float(row[1])
          
        if start_profit == 0:
                       
            start_profit = float(row[1])
            last_row = start_profit

        else:

            diff = float(row[1]) - last_row
            changes.append(float(diff))
            last_row = float(row[1])
       
            if int(row[1]) > biggest_increase:
                biggest_increase = int(row[1])
                increase_row = row
            
            elif int(row[1]) < biggest_decrease:
                biggest_decrease = int(row[1])
                decrease_row = row
            
        rowcount +=  1   
    
    avg_change = sum(changes) / (rowcount - 1)
    min_change = min(changes)
    max_change = max(changes)    
    
    
print()
print("Financial Data")
print("-----------------------------------------------------")
print("total_months:", rowcount)       
print("net total:", "$", net_total)    
print("average change:", "$", avg_change)
print("biggest increase:", increase_row[0], "|", "$", max_change) 
print("biggest decrease:", decrease_row[0], "|", "$", min_change)   

sys.stdout.close() 
sys.stdout=stdoutOrigin

print()
print("Financial Data")
print("-----------------------------------------------------")
print("total_months:", rowcount)       
print("net total:", "$", net_total)    
print("average change:", "$", avg_change)
print("biggest increase:", increase_row[0], "|", "$", max_change) 
print("biggest decrease:", decrease_row[0], "|", "$", min_change)
        
    