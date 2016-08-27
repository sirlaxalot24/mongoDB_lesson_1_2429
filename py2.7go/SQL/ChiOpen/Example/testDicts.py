import csv
from pprint import pprint as pp


with open('nodes.csv', 'r') as f:
    john = csv.DictReader(f)
    for row in john:
        pp(row)
