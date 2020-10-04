import os
import csv
import operator as op

budget_list = []
total = 0

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    column_names = next(csv_reader)

    for row in csv_reader:
        budget_list.append((row[0], int(row[1])))
        total += int(row[1])

budget_list.sort(key = lambda x: x[1])

num_months = len(budget_list)
avg_change = total / num_months
greatest_inc = budget_list[-1]
greatest_dec = budget_list[1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {greatest_inc[0]} ({greatest_inc[1]})")
print(f"Greatest Decrease in Profits: {greatest_dec[0]} ({greatest_dec[1]})")