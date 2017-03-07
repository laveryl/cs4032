import socket
import sys

#assignments

message = "All work and no play makes Jack a dull boy!"

#create socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#assign socket address
host = ('localhost',8000)
#connect socket
sock1.connect(host)
#send a message
sock1.send("GET /echo.php?message="+message+" HTTP/1.1\r\n\r\n")
#receive message
data =sock1.recv(1024)
#close connection
sock1.close()
#return data
print data