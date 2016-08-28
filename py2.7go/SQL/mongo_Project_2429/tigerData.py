import csv
from pprint import pprint as pp


tigerData = []

with open('ways_tags.csv', 'r') as f:
    tags = csv.DictReader(f)
    for row in tags:
        if row['type'] == 'tiger':
            tigerData.append(row)

        # if row['type'] in crazyVals:
        #     pass
        # else:
        #     crazyVals.append(row['type'])


#pp(tigerData[:10])
pp("Amount of Tiger Tags: " + str(len(tigerData)))

crazyVals = []

with open('ways.csv', 'r') as f:
    tags = csv.DictReader(f)
    for row in tags:
        if row['user'] == 'Millbrooky':
            crazyVals.append(row)

        # if row['user'] in crazyVals:
        #     pass
        # else:
        #     crazyVals.append(row['user'])


pp(sorted(crazyVals))
pp(len(crazyVals))