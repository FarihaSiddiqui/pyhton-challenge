# Modules
import os
import csv

# Path for file
csvpath = os.path.join( "Resources", "election_data.csv")

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    total_votes = 0
    unique_list = []
    candidate_list = []
    candidate_votes = []
    candidate_votes_percentage = []

    for row in csvreader:
        total_votes += 1
        if row[2] not in unique_list:
            unique_list.append(row[2])

        candidate_list.append(row[2])
    for x in unique_list:
        candidate_votes.append(candidate_list.count(x))

    for y in candidate_votes:
        candidate_votes_percentage.append("{:.3%}".format(y/total_votes))

    winner_votes = max(candidate_votes)
    index_winner = candidate_votes.index(winner_votes)
    winner = candidate_list[index_winner]
    
print ("Election Results")
print ("-------------------------------")
print(f"Total Votes: {total_votes}")
print ("-------------------------------")
print (f"{unique_list[0]}: {candidate_votes_percentage[0]} ({candidate_votes[0]})")
print (f"{unique_list[1]}: {candidate_votes_percentage[1]} ({candidate_votes[1]})")
print (f"{unique_list[2]}: {candidate_votes_percentage[2]} ({candidate_votes[2]})")
print (f"{unique_list[3]}: {candidate_votes_percentage[3]} ({candidate_votes[3]})")
print ("-------------------------------")
print(f"Winner: {winner}")
print ("-------------------------------")

output_path = os.path.join("Analysis","PyPoll Analysis.txt")

with open(output_path, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write ("-------------------------------\n")
    text_file.write(f"{unique_list[0]}: {candidate_votes_percentage[0]} ({candidate_votes[0]})\n")
    text_file.write (f"{unique_list[1]}: {candidate_votes_percentage[1]} ({candidate_votes[1]})\n")
    text_file.write (f"{unique_list[2]}: {candidate_votes_percentage[2]} ({candidate_votes[2]})\n")
    text_file.write(f"{unique_list[3]}: {candidate_votes_percentage[3]} ({candidate_votes[3]})\n")
    text_file.write ("-------------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write ("-------------------------------\n")