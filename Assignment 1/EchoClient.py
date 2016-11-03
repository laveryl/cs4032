import socket
import sys

#assignments
host = sys.argv[1]
port = int(sys.argv[2])
message = "All work and no play makes Jack a dull boy!"

#create socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect socket
sock1.connect((host,port))
#send a message
s.send("GET /echo.php?message="+message+" HTTP/1.1\r\n\r\n")
#receive message
data =s.recv(1024)
#close connection
s.close()
#return data
print data