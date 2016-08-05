import xml.etree.ElementTree as ET
import pprint

osmName = 'sample.osm'

tagList = {}

with open(osmName, 'r') as f:
    for event, element in ET.iterparse(f, events=("end",)):
        if element.tag not in tagList:
            tagList[element.tag] = 1
        else:
            tagList[element.tag] += 1

print tagList