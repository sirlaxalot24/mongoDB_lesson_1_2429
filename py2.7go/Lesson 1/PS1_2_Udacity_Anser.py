# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:00:23 2016

@author: jlubuntu
"""

import xlrd
import os
import csv
import pprint

datafile = r'J2013_ERCOT_Hourly_Load_Data.xls'
outfile = r'/home/jlubuntu/Udacity/mongoDB_lesson_1_2429/py2.7go/2013_Max_Loads2.csv'

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    # process all rows that contain station data
    for n in range (1, 9):
        station = sheet.cell_value(0, n)
        cv = sheet.col_values(n, start_rowx=1, end_rowx=None)

        maxval = max(cv)
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos, 0)
        realtime = xlrd.xldate_as_tuple(maxtime, 0)
        data[station] = {"maxval": maxval,
                         "maxtime": realtime}                         
    pprint.pprint(data)
    return data

def save_file(data, filename):
    with open(filename, "w") as f:
        w = csv.writer(f, delimiter='|')
        w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for s in data:
            year, month, day, hour, _ , _= data[s]["maxtime"]
            w.writerow([s, year, month, day, hour, data[s]["maxval"]])
            
            
def test():
    open(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

test()          