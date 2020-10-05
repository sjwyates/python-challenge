import os
import csv

# List of tuples (month, profits/losses) to hold slightly cleaned data
budget_list = []
# Incrementing tally for total profits/losses
total_pl = 0
# List of month-to-month change in profits/losses
pl_changes = []

# File paths
input_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Output', 'budget_results.txt')

# Open CSV raw data file and instantiate the CSV reader
with open(input_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip header row, then get data from first row
    next(csv_reader)
    first_row = next(csv_reader)
    prev_pl = int(first_row[1])
    budget_list.append((first_row[0], prev_pl))

    # For each row after the first...
    for row in csv_reader:
        # Get date and profits/losses, coerced to integer
        date = row[0]
        pl = int(row[1])
        # Append a tuple with the date and profits/losses
        budget_list.append((date, pl))
        # Increment total profits/losses by current value
        total_pl += pl
        # Subtract previous value and append to changes list
        pl_changes.append(pl - prev_pl)
        # Reset previous previous profits/losses to current value
        prev_pl = pl
        
# Sort list by the 1nth item in each tuple (profits/losses)
budget_list.sort(key = lambda x: x[1])

# Get number of months
num_months = len(budget_list)
# Sum the changes list and divide by num_months to get the average
avg_change = sum(pl_changes) / (num_months - 1)
# Greatest increase is last item in sorted list; greatest decrease is the first
greatest_inc = budget_list[-1]
greatest_dec = budget_list[0]

# Create a list of strings corresponding to each line of the output
analysis = ["Financial Analysis", "----------------------------", 
f"Total Months: {num_months}", f"Total: ${total_pl}", f"Average Change: ${round(avg_change, 2)}", 
f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})", 
f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})"]

# Open up the new text file to write the results to
with open(output_path, 'w') as results_file:
    # Single loop to print to terminal and write to file
    for line in analysis:
        print(line)
        # printf format string to add line breaks after each line
        results_file.write("%s\n" % line)