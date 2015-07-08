# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 13:52:33 2015

@author: jpaukov
"""

import os

DATADIR = "C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429"
DATAFILE = "Beatles_diskography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break
            
            fields = line.split(",")
            entry = {}
            
            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()   
                
            data.append(entry)
            counter +=1
                
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)    
    
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22-Mar-63', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10-Jul-64', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline
    print d[0]
    print firstline
    print d[9]
    print tenthline    
    
    
test()
