import os
import csv

election_data_path = os.path.join("Resources","election_data.csv")

candidates = []
candidateResults = []
candidateVotes = []
electionResults = {}


total_votes = 0

with open(election_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)
    
    for row in csv_reader:
        total_votes +=1
        if row[2] in electionResults.keys():
            electionResults[row[2]] = electionResults[row[2]] + 1
        else:
            electionResults[row[2]] = 1
    
    # Read through each row of data after the header

    for key, value in electionResults.items():
        candidates.append(key)
        candidateVotes.append(value)

vote_percentage = []

for n in candidateVotes:
    vote_percentage.append(round(n/total_votes*100))
        
new_db = list(zip(candidates, vote_percentage, candidateVotes))

electionWinner_list = []

for name in new_db:
    if max(candidateVotes) == name[2]:
        electionWinner_list.append(name[0])

winner = electionWinner_list[0]

# Print Results to Terminal
###############################################################
print(f"Election Results")
print(f"----------------------------------------")
print(f"Total Votes: {int(total_votes)}")
print(f"----------------------------------------")

for entry in new_db:
    print(f"{str(entry[0])}: {int(entry[1])}%   ({str(entry[2])})")

print(f"----------------------------------------")
print(f"Winner:  {str(electionWinner_list[0])}")
print(f"----------------------------------------")
################################################################

# Print Results to File
################################################################
output_file = os.path.join("Output", "election_results.txt")

with open(output_file, 'w') as txtfile:
    txtfile.writelines("Election Results \n----------------------------------------\nTotal Votes: " + str(total_votes) + "\n----------------------------------------\n")

    for entry in new_db:
        txtfile.writelines(entry[0] + ": " + str(entry[1]) + "% (" + str(entry[2]) + ")\n")
    txtfile.writelines("----------------------------------------\nWinner: " + winner + "\n----------------------------------------")
################################################################

