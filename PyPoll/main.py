# Modules
import os
import csv

# Path for file
csvpath = os.path.join( "Resources", "election_data.csv")

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    header = next(csvreader)

    # Defining variables
    total_votes = 0
    unique_list = []
    candidate_list = []
    candidate_votes = []
    candidate_votes_percentage = []

    # Read through each row of the data 
    for row in csvreader:

        # Calculate the total number of votes
        total_votes += 1

        # Calculate a list of candidates who received votes
        if row[2] not in unique_list:
            unique_list.append(row[2])

        # Setting column 3 as a [list] for further calculations
        candidate_list.append(row[2])

    # Calculate the total number of votes each candidate won
    for x in unique_list:
        candidate_votes.append(candidate_list.count(x))

    # Calculate the percentage of votes each candidate won 
    for y in candidate_votes:
        candidate_votes_percentage.append("{:.3%}".format(y/total_votes))

    # Election winner = max votes, use index to determine the winner
    winner_votes = max(candidate_votes)
    index_winner = candidate_votes.index(winner_votes)
    winner = candidate_list[index_winner]

# Print results to terminal    
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

# Write the results into a text file
# Specify the path of the file to write to
output_path = os.path.join("Analysis","PyPoll Analysis.txt")

# Open the file using the "write" mode
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