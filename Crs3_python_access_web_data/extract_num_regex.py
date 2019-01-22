#
# Title:  Extracting Data with Regular Expressions
# Author: Claudio Asangong
#
# In this assignment, you write a Python program to read through and parse
# a file with text and numbers. Then extract all the numbers in the file
# and compute the sum of the numbers.
# Data Files:
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
#              (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_174558.txt
#              (There are 80 values and the sum ends with 294)
#
# Concepts: regular expression

import re

fname = input("Enter file name: ")
try:
    fhandler = open(fname)
except Exception as e:
    print("File not found: ", fname)
    quit()
total = 0

for line in fhandler:
    # find all digits in the line - returns a list
    numlist = re.findall('[0-9]+', line)
    for i in numlist:
        total += int(i)
print(total)
