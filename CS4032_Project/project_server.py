import socket
import threadpool
import os

server_threads = threadpool.ThreadPool(300)
active_threads=True

port_number = 8080
ip_address = socket.gethostbyname(socket.gethostname())

def create_server_socket():
    # create socket  and initialise to localhost:8080
    sockie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('127.0.0.1', port_number)
    print "starting up on %s port %s" % server_address

    # bind socket to server address and wait for incoming connections4
    sockie.bind(server_address)
    sockie.listen(1)

    while True:
        # sock.accept returns a 2 element tuple
        connect, client_address = sockie.accept()
        

        # allow other thread to deal with the client 
        server_thread_pool.add_task(
            start_client_interaction,
            connect,
            client_address
        )


def commands(connect, client_address):
	while active_threads:

		client_id = file_system_manager.add_client(connect)

		msg=connect.recv(1024)
		data_inputs = seperate_input_data(msg)
		
		# Respond to the appropriate message
		#if message is kill service
        if data == "KILL_SERVICE":
                kill_service(connect)

        #if message is list directory
        elif data_inputs[0] == "ls":
                ls(connect, data_inputs, client_id)

        #if message is change directory
        elif data_inputs[0] == "cd":
                cd(connect,data_inputs,client_id)

        #read stores information entered
		elif data_inputs[0] =="read":
				read(connect,data_inputs, client_id)

		#sends message to another user
		elif data_inputs[0] =="write":
				write(connect, data_inputs, client_id)

		# error message
		else:
			errmsg="ERROR_CODE:1\nERROR_DESCRIPTION: Parse error\n"
			connect.sendall(errmsg)



def kill_service(connect):
	response = "Killing Service"
    connection.sendall("%s" % response)
    connection.close()
    os._exit(0)

def ls(connect, data_inputs, client_id)
     response = ""
    	
        #TODO implement list firectory in model
        #send response
        connect.sendall(response)
    
    else:
        error_response(connection, 1)


def cd (connect, client_id, data_inputs)
	response = ""
    	
        #TODO implement list firectory in model
        #send response
        connect.sendall(response)
    
    else:
        error_response(connection, 1)




def read (connect, client_id, data_inputs)
	response = ""
    	
        #TODO implement list firectory in model
        #send response
        connect.sendall(response)
    
    else:
        error_response(connection, 1)




def write (connect, client_id, data_inputs)
	response = ""
    	
        #TODO implement list firectory in model
        #send response
        connect.sendall(response)
    
    else:
        error_response(connection, 1)

