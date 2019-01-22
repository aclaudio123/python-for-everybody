#
# Title:   Retrieving web pages over Network Sockets
# Author: Claudio Asangong
#
# Simple Python program to retrieve a web page over a Network socket and
# display the headers and content from the web server. An alternative to
# opening the URL in a web browser with a developer console and manually
# examine the headers that are returned.
#
# Concepts: Network Sockets, HTTP

import socket

# make a Network socket connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# send request as UTF-8 bytes
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# loop to read file
while True:
    data = mysock.recv(512)
    # when end of file break the loop
    if len(data) < 1:
        break
    # decode UTF-8 bytes to python unicode strings    
    print(data.decode(), end='')

mysock.close()
