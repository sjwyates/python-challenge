import os
import csv

# Dictionary to store tallies as name: votes
tally_dict = {}
# Counter for total votes
total_votes = 0

# Input and output file paths
input_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Output', 'election_results.txt')

# Open up the CSV file and instantiate the CSV reader
with open(input_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Ignore the header row
    next(csv_reader)

    # For each remaining row...
    for row in csv_reader:
        # If that candidate isn't in the dictionary yet...
        if row[2] not in tally_dict:
            # Add them and start their tally at 1 vote
            tally_dict[row[2]] = 1
        # Otherwise...
        else:
            # Increment their existing tally by 1 vote
            tally_dict[row[2]] += 1
        # Either way, increment total votes by 1
        total_votes += 1

# Find the max value in the dictionary and return its key
winner = max(tally_dict, key=tally_dict.get)

# Function to calc vote percent and return formatted string
def get_pct(candidate, votes):
    vote_pct = round(100 * votes / total_votes, 3)
    return f"{candidate}: {vote_pct}% ({votes})"

# List comprehension applies that function to each item in the dictionary
result_list = [get_pct(candidate, votes) for candidate, votes in tally_dict.items()]

# Because the same bar is used 4 times
bar = "-------------------------"
# Make a list of strings, each representing 1 line in the analysis,
# by combining 3 lists (which is super simple in Python)
analysis = ["Election Results", bar, f"Total Votes: {total_votes}", bar] + result_list + [bar, f"Winner: {winner}", bar]

with open(output_path, 'w') as results_file:
    # Single loop to print to terminal and write to file
    for line in analysis:
        print(line)
        # printf format string to add line breaks after each line
        results_file.write("%s\n" % line)