# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:09:02 2015

@author: jpaukov
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        aL = soup.find(id="AirportList")
        for option in aL.find_all('option'):
            if option['value'] != 'All' and option['value'] != 'AllOthers' and option['value'] != 'AllMajors':
                data.append(option['value'])
    return data


def test():
    data = extract_airports(html_page)
    print data
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()