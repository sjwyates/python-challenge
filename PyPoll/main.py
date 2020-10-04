import os
import csv

tally_dict = {}
total_votes = 0

input_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Output', 'election_results.txt')

with open(input_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        if row[2] not in tally_dict:
            tally_dict[row[2]] = 1
        else:
            tally_dict[row[2]] += 1
        total_votes += 1

winner = max(tally_dict, key=tally_dict.get)

def get_pct(candidate, votes):
    vote_pct = round(100 * votes / total_votes, 3)
    return f"{candidate}: {vote_pct}% ({votes})"

result_list = [get_pct(candidate, votes) for candidate, votes in tally_dict.items()]

bar = "-------------------------"
analysis = ["Election Results", bar, f"Total Votes: {total_votes}", bar] + result_list + [bar, f"Winner: {winner}", bar]

with open(output_path, 'w') as results_file:
    for line in analysis:
        print(line)
        results_file.write("%s\n" % line)