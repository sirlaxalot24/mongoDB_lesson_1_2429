import csv
from pprint import pprint as pp



# I used this file to look through csv for users with Nodes with no user

with open('nodes.csv', 'r') as f:
    john = csv.DictReader(f)
    for row in john:
        if row['user'] == '00000':
            pp(row)
