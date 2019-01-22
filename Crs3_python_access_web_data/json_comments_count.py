#
# Title:   Extracting Data from JSON API
# Author: Claudio Asangong
#
# In this assignment you will write a Python program that prompts for a URL,
# read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file
#
# We provide two files for this assignment. One is a sample file where we give
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_174563.json
#              (Sum ends with 40)
#
# Concepts: JSON, urllib
# commit msg: Extracting data using JSON API

import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input("Enter data url: ")
    if len(url) < 1:
        break
    print('Retrieving', url)
    urlhandler = urllib.request.urlopen(url, context=ctx)
    urldata = urlhandler.read().decode()
    print('Retrieved', len(urldata), 'characters')

    # parse the json data into python object (deserialize)
    try:
        js = json.loads(urldata)
    except Exception:
        print('==== Failure To Retrieve ====')
        print(urldata)
        continue

    print('Count:', len(js['comments']))
    total = 0
    for d in js['comments']:
        total += d['count']
    print('Sum:', total)
