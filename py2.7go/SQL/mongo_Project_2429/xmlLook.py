import xml.etree.ElementTree as ET
from pprint import pprint as pp

osmName = 'smallStLou.osm'

way_attribs = {}
way_nodes = []
tags = []

#tagList = {}

#not functioning properply, the code isn't compiling all 'way' its just replacing the previous with the current

with open(osmName, 'r') as f:
    for event, element in ET.iterparse(f, events=("end",)):
        if element.tag == 'way':
            way_attribs = element.attrib



        # if element.tag not in tagList:
        #     tagList[element.tag] = 1
        # else:
        #     tagList[element.tag] += 1

#print tagList
pp({'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags})