#
# Title:   Simple File processing
# Author: Claudio Asangong
#
#
# 7.1 Write a program that prompts for a file name, then opens that file and
# reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output.
# You can download the sample data at http://www.py4e.com/code3/words.txt
#
# Concepts: file processing

fname = input('Enter name of File: ')
fhandler = open(fname)
for line in fhandler:
    line = line.rstrip()  # right strip newline character at end of line
    print(line.upper())  # convert to uppercase
