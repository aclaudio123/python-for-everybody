#
# Title:   File processing 4: string parsing
# Author: Claudio Asangong
#
# 8.5 Open the file mbox-short.txt and read it line by line. When you find a
# line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in
# the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#
# Concepts: file processing, string parsing, error handling

fname = input("Enter file name: ")
try:
    fhandler = open(fname)
except Exception e:
    print("File not found", fname)
    quit()

count = 0
for line in fhandler:
    if line.startswith('From '):
        llist = line.split()
        print(llist[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
