# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 13:07:46 2015

@author: jpaukov
"""

import xlrd
import os
import csv
datafile = 'C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429\J2013_ERCOT_Hourly_Load_Data.xls'
filename = 'C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429\Testrun.csv'


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

with open(filename, 'wb') as f:
    w = csv.writer(f, delimiter='|')
    header = ['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']
    w.writerow(header)
    for line in data:
        w.writerow(line)



    
print data