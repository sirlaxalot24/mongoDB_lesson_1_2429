import xml.etree.ElementTree as ET
import pprint

osmName = 'chicago_illinois.osm'

tree = ET.iterparse(osmName)

print(tree)

tagList = {}

for tag in tree:
    if tag in tagList:
        next(tag)
    else:
        tagList.update(tag[1])

print(tagList)