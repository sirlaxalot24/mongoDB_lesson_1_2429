import csv
from pprint import pprint as pp


with open('nodes_tags.csv', 'r') as f:
    tags = csv.DictReader(f)
    for row in tags:
        if row['key'] == 'FIXME':
            pp(row)
