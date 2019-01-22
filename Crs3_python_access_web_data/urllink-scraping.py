#
# Title:   Following Links in HTML Using BeautifulSoup
# Author: Claudio Asangong
#
# A Python program that uses urllib to read the HTML from the data files below,
# extract the href= values from the anchor tags, scan for a tag that is in
# a particular position from the top and follow that link, repeat the process
# a number of times, and report the last name found.
#
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat
# this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret, Montgomery, Mhairade, Butchi, Anayah
# Last name in sequence: Anayah
#
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Orin.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat
# this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load
# is: T
#
# Concepts: Web Scraping with BeautifulSoup, html
# commit msg: 

import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Orin.html'

count = input('Enter count: ')
pos = input('Enter position: ')

for i in range(int(count)+1):
    html = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieving: ', url)
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the <a> tags into a resultset
    anchor_tags = soup('a')
    # Extract the href values in <a> - treating tag as dict (key=href)
    hrefs = [tag.get('href', None) for tag in anchor_tags]
    if len(hrefs) < 1:
        break
    url = hrefs[int(pos)-1]
