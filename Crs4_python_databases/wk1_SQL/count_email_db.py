#
# Title:   Counting Emails in a Database
# Author: Claudio Asangong
#
# This application will read the mailbox data (mbox.txt) and count the number
# of email messages per organization (i.e. domain name of the email address)
# using a database with the following schema to maintain the counts.
#
#   CREATE TABLE Counts (org TEXT, count INTEGER)
#
# The data file used for this application is http://www.py4e.com/code3/mbox.txt
#
# Concepts: SQL, SQLite

import sqlite3
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# create a connection
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop table if exist
cur.execute('DROP TABLE IF EXISTS Counts')
# create new table
cur.execute('CREATE TABLE Counts(org TEXT, COUNT INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fhandler = open(fname)
for line in fhandler:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]
    org = email.split('@')[1]
    # use ? as placeholder value to prevent SQL injection
    # values should be given as tuple (value1,) if one value
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org, count) VALUES(?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org= ?',
                    (org,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
