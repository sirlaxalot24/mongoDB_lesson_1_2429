#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429\Cities.csv'


def countZero(val1, val2):
    
    val1 = str(val1)
    val2 = str(val2)
    count1 = 0
    count2 = 0
    for i in range(len(val1)):
        if val1[i] != '0' and val1[i] != '.':
            count1 = count1 + 1
    
    for i in range(len(val2)):
        if val2[i] != '0'and val2[i] != '.':
            count2 = count2 + 1

    return count1, count2

def strType(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        try:
            if value.startswith('{'):            
                return value
        except ValueError:    
            None(value)



def fix_area(area):
    
    area = strType(area)
    
    if type(area) == str:
        area = area.split('|')
        area1 = area[0]
        area2 = area[1]
        tArea1 = float(area1[1:])
        tArea2 = float(area2[:-1])

        chooser = countZero(tArea1, tArea2)        
        
        print chooser        
        
        if chooser[0] <= chooser[1]:
            area = tArea2
        else:
            area = tArea1
        
    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra matadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
                data.append(line)
            
    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(0,39):
        pprint.pprint(data[n]["areaLand"])

    assert data[8]["areaLand"] == 55166700.0
    assert data[3]["areaLand"] == None

if __name__ == "__main__":
    test()