#
# Title:   Matching and extracting values from a File
# Author: Claudio Asangong
#
#
# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
#
# Concepts: file processing
# commit msg: Matching and extracting values from a File

fname = input("Enter file name: ")
# File error checking
try:
    fhandler = open(fname)
except Exception:
    print("File not found", fname)
    quit()

count = 0
total = 0
for line in fhandler:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = line.find(':')     # find index of colon
        value = line[pos+1:]     # extract substring 0.8475
        total = total + float(value)
print('Average spam confidence:', total/count)
