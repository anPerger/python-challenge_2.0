import csv
import os
import operator
import sys

csvpath = os.path.join("resources", "election_data.csv")

stdoutOrigin=sys.stdout # Method I found on stackoverflow to export results
sys.stdout = open("log.txt", "w") # to a .txt file

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    total_votes = 0
    results = {}
    vote_tally = {}
    pct_tally = {}

    for row in csvreader:
        
        candidate = row[2]
        total_votes += 1
         
        try:
            current_vote = vote_tally[candidate] + 1
            vote_tally[candidate] = current_vote
            pct_tally[candidate] = (vote_tally[candidate] / total_votes) * 100

        except:
            vote_tally[candidate] = 1

# Easiest and quickest method i found online to grab winner 
winner = max(vote_tally.items(), key=operator.itemgetter(1))[0] 


print("Election Results")
print("----------------------------")
print(f"Total votes: {total_votes}")
print("----------------------------")
   
print(vote_tally)
print(pct_tally)
print("----------------------------")
print("Winner: ", winner)

sys.stdout.close()
sys.stdout=stdoutOrigin

print("Election Results")
print("----------------------------")
print(f"Total votes: {total_votes}")
print("----------------------------")
print(vote_tally)
print(pct_tally)
print("----------------------------")
print("Winner: ", winner)
