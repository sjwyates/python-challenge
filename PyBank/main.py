import os
import csv
import operator as op

budget_list = []
total_pl = 0

input_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Output', 'budget_results.txt')

with open(input_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        budget_list.append((row[0], int(row[1])))
        total_pl += int(row[1])

budget_list.sort(key = lambda x: x[1])

num_months = len(budget_list)
avg_change = total_pl / num_months
greatest_inc = budget_list[-1]
greatest_dec = budget_list[0]

analysis = ["Financial Analysis", "----------------------------", 
f"Total Months: {num_months}", f"Total: ${total_pl}", f"Average Change: ${round(avg_change, 2)}", 
f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})", 
f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})"]

with open(output_path, 'w') as results_file:
    for line in analysis:
        print(line)
        results_file.write("%s\n" % line)