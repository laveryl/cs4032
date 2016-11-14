import sys
from socket import *
from Queue import Queue
from threading import Thread
import os
import signal

def _threads(runner):

	while True:

		thread_socket=runner.get()
		thread_address=runner.get()

		active=True
		while active==True:

			receive=thread_socket.recv(2048)

			if not receive: break

				#RECEIVING A MESSAGE AND ENDING THE THREAD
			if receive[:12]=="End_Thread":
				print "Ending The Thread!!"
				thread_socket.close()
				active=False

				#SENDING A MESSAGE
			elif receive[:4]=="Message":
				print "Message Received: "+receive
				
				#REPORT BACK
				msg="%sIP:%s\nPort:%s"%(receive,str(thread_address),thread_socket)
				thread_socket.sendall(msg)
				print "Message Sent"	

				#OTHER RECEIVED MESSAGE BEYOND DEFINED
			else:
				print "other Received:"+receive
				message=receive[:-2].upper()
				thread_socket.sendall(message)

				#KILL THE CONNECTION
		if active==False:
			os.kill(os.getpid(),signal.SIGINT)					
	
	work_socket.close()

def _server(hostname,port_number,numb_of_threads):

	sock=socket(AF_INET,SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sock.bind((hostname,port_number))
	sock.listen(10)	

	pool=Queue(numb_of_threads)

	for i in range(numb_of_threads):
		thread= Thread(target=_threads,args=(pool,))
		thread.daemon=True
		thread.start()

	while True:
		try:
			client_socket,address=sock.accept()
			pool.put(client_socket)
			pool.put(address)
		except KeyboardInterrupt:
			print "\nSTOPPED"
			break


if __name__ == '__main__':
	_server(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))