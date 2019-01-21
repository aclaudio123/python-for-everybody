#
# Title:   top email sender
# Author: Claudio Asangong
#
# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.
#
# Concepts: dictionary, for loop, file processing
# commit msg: Searching top email sender in mbox.txt

fname = input("Enter file name: ")
try:
    fhandler = open(fname)
except Exception:
    print("File not found", fname)
    quit()

address = dict()
for line in fhandler:
    if line.startswith('From '):
        llist = line.split()
        email = llist[1]
        # retrieve/create/update counter - replaces dict() if/else
        address[email] = address.get(email, 0) + 1

max_val = max(address.values())
for k, v in address.items():
    if v == max_val:
        print(k, v)
