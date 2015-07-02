# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 16:52:46 2015

@author: jpaukov
"""

import os
import pandas

DATADIR = "C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429"
DATAFILE = "Beatles_diskography_3.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break
            
            fields = line.split(",")
            entry = {}
            
            for i, value in enumerate(fields):
                entry[i] = value.strip()
                
                data.append(entry)
                counter +=1
                
    return data

datafile = os.path.join(DATADIR, DATAFILE)

d = parse_file(datafile)

print d         