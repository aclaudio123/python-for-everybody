#
# Title:   Scraping HTML data with BeautifulSoup
# Author: Claudio Asangong
#
# A Python program to use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers
# in the file
# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_174560.html
#              (Sum ends with 2)
#
# Concepts: Web Scraping with BeautifulSoup
# commit msg: Scraping HTML with BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
span_tags = soup('span')

total = 0
for tag in span_tags:
    # extract content of span tag
    content = tag.contents[0]
    total += int(content)
print(total)
