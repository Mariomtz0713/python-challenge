import os
import csv
election_data = os.path.join('Resources', 'election_data.csv')

county = []
candidate = []

charles = "Charles Casper Stockham"
diana = "Diana DeGette"
raymon = "Raymon Anthony Doane"

def candidate_votes(person):
    total_vote = 0
    for x in range(len(county)):
        if candidate[x] == person:
            total_vote += 1
    return total_vote

def vote_percentage(person):
    percent = round(candidate_votes(person)/len(county)*100, 3)
    return percent

def winnings():
    if vote_percentage(charles) > vote_percentage (diana):
        winner = charles
    elif vote_percentage(diana) > vote_percentage(raymon):
        winner = diana
    else:
        winner = raymon
    return winner

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        county.append(row[1])
        candidate.append(row[2])


print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(county)}")
print("-------------------------")
print(f"{charles}: {vote_percentage(charles)}% ({candidate_votes(charles)})")
print(f"{diana}: {vote_percentage(diana)}% ({candidate_votes(diana)})")
print(f"{raymon}: {vote_percentage(raymon)}% ({candidate_votes(raymon)})")
print("-------------------------")
print(f"Winner: {winnings()}")
print("-------------------------")

#Writing Analysis
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as txtfile:   
  
   txtfile.write("Election Results\n")
   txtfile.write("-------------------------\n")
   txtfile.write(f"Total Votes: {len(county)}\n")
   txtfile.write("-------------------------\n")
   txtfile.write(f"{charles}: {vote_percentage(charles)}% ({candidate_votes(charles)})\n")
   txtfile.write(f"{diana}: {vote_percentage(diana)}% ({candidate_votes(diana)})\n")
   txtfile.write(f"{raymon}: {vote_percentage(raymon)}% ({candidate_votes(raymon)})\n")
   txtfile.write("-------------------------\n")
   txtfile.write(f"Winner: {winnings()}\n")
   txtfile.write("-------------------------\n")