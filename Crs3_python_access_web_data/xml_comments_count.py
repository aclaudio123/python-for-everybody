#
# Title:   Extracting Data from XML
# Author: Claudio Asangong
#
# In this assignment you write a Python program that prompts for a URL, read
# the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file
#
# We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_174562.xml
#              (Sum ends with 19)
#
# Concepts: XML, urllib, ElementTree API

import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter data url: ')
    if len(url) < 1:
        break

    print('Retrieving', url)
    urlhandler = urllib.request.urlopen(url, context=ctx)
    # read in data and decode (utf-8 to Python unicode string)
    urldata = urlhandler.read().decode()

    print('Retrieved', len(urldata), 'characters')

    # parse url data into xml element tree
    tree = ET.fromstring(urldata)
    # extract all comment tags (parent of count tag)
    comments = tree.findall('.//comment')
    print('Count:', len(comments))
    total = 0
    for comment in comments:
        total += int(comment.find('count').text)
    print('Sum:', total)
