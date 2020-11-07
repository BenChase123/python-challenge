# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyPoll\Resources', 'election_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    count = 0
    candidates = []
    votes = [0,0,0,0]
    percentage = [0,0,0,0]
    winning_votes = 0
    winner = ''
    for row in csvreader:
        count = count + 1
        if row[2] not in candidates:
            candidates.append(row[2])
        for i in range(len(candidates)):
            if candidates[i] == row[2]:
                votes[i] = votes[i] + 1
    for i in range(4):
        percentage[i] = votes[i]/count
    for i in range(4):
        if votes[i] > winning_votes:
            winning_votes = votes[i]
            winner = candidates[i]

    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {count}")
    print("--------------------")
    for i in range(4):
        print(f"{candidates[i]}: {percentage[i]}% ({votes[i]})")
    print(f"Winner: {winner}")

    output_path = os.path.join("..", "PyPoll\Analysis", "poll_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
    outF = open(output_path, "w")
    outF.write("Election Results")
    outF.write("\n")
    outF.write("--------------------")
    outF.write("\n")
    outF.write(f"Total Votes: {count}")
    outF.write("\n")
    outF.write("--------------------")
    outF.write("\n")
    for i in range(4):
        outF.write(f"{candidates[i]}: {percentage[i]}% ({votes[i]})")
        outF.write("\n")
    outF.write(f"Winner: {winner}")
    outF.write("\n")
    outF.close()
    
    
    