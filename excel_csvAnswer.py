# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
datafile = 'C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429\J2013_ERCOT_Hourly_Load_Data.xls'
filename = 'C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429\Testrun.csv'
outfile = 'C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429\2013_Max_Loads.csv'


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []
    header = 'Station, Year, Month, Day, Hour, Max Load'.split(',')
    i = 1
    while i < len(sheet.row_values(0))-1:
        column = sheet.col_values(i, start_rowx=1, end_rowx=None)
        name = str(sheet.cell_value(0, i))
        max_load = max(column)
        max_place = column.index(max_load)+1
        max_time = xlrd.xldate_as_tuple(sheet.cell_value(max_place, 0), 0)
        row = [name, max_time[0], max_time[1], max_time[2], max_time[3], max_load]
        data.append(row)
        i += 1
    return data

def save_file(data, filename):
    with open(filename, 'wb') as f:
        w = csv.writer(f, delimiter='|')
        header = ['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']
        w.writerow(header)
        for line in data:
            w.writerow(line)

    
def test():
    open(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]

        
test()