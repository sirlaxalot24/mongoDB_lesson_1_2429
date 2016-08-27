import csv
from pprint import pprint as pp


with open('nodes.csv', 'r') as j:
    node = csv.DictReader(j)

with open('nodes_tags.csv', 'r') as f:
    tags = csv.DictReader(f)
    for row in john:
        if row['key'] == 'FIXME':
            pp(row)
