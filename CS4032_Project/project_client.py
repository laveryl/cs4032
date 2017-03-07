import socket
import threadpool
import time
import os



client_thread_pool = threadpool.ThreadPool(5)

ip_address = socket.gethostbyname(socket.gethostname())

port_num = 8080

response_var = ""

def connect_to_server_userin():

    sockie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', port_num)
    print "connecting to %s on port %s\n" % server_address
    sockie.connect(server_address)

     sockie.close()

def get_server_response(socket):
    global response_var
    while True:
        data = socket.recv( 1024 )
        response_var = data
        if (data != None):
            # if reading cache item
            if(len(data.split("////")) == 2):
                split_data = data.split("////")
                add_to_cache(split_data[0], split_data[1])
                print split_data[1]
            else:
                print data