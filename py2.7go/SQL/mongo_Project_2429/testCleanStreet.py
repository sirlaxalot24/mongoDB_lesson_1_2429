import csv
from pprint import pprint as pp
import cleanStreeZip


crazyVals = []

with open('nodes_tags.csv', 'r') as f:
    tags = csv.DictReader(f)
    for row in tags:
        if row['key'] == 'street':
            street = cleanStreeZip.clean_street_name(row['value']).split()[-1]

            if street in crazyVals:
                pass
            else:
                crazyVals.append(street)


pp(sorted(crazyVals))