import csv
from pprint import pprint as pp
import cleanStreeZip


topVar = 'key'
bVar = 'value'
param = 'street'

crazyVals = {}

with open('nodes_tags.csv', 'r') as f:
    tags = csv.DictReader(f)
    for row in tags:
        if row[topVar] == param:
            # zipCode = cleanStreeZip.clean_street_name(row[bVar])
            if row[bVar] not in crazyVals:
                crazyVals[row[bVar]] = 1
            else:
                crazyVals[row[bVar]] += 1


        # if row[bVar] not in crazyVals:
        #     crazyVals[row[bVar]] = 1
        # else:
        #     crazyVals[row[bVar]] += 1

pp(crazyVals)