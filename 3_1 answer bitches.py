# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 07:58:28 2015

@author: jpaukov
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'C:\Users\jpaukov\Documents\Udacity\mongoDB\mongoDB_lesson_1_2429\Cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

 
    
def audit_file(filename, fields):
    fieldtypes = {}
    with open(filename, 'r') as f:
        data = csv.DictReader(f)
        for i in range(3):
            data.next()
        
        for i in fields:
            fieldtypes[i] = set()
            
        for row in data:
            for i in fields:
                x = set()
                newType = strType(row[i])
                iType = type(newType)
                x.add(iType)
                fieldtypes[i].add(iType)
                
    return fieldtypes          


def strType(value):
    try:
        return float(value)
    except ValueError:
        try:
            return int(value)
        except ValueError:
            try:            
                None(value)
            except:
                try:
                    if value.startswith("{"):    
                        return list(value)
                except ValueError:
                    return str(value)
                    

def test():
    fieldtypes = audit_file(CITIES, FIELDS)


    pprint.pprint(fieldtypes)

    
if __name__ == "__main__":
    test()            
                

     