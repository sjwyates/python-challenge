import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    