mport datetime
import threadpool
import time
import os
import shutil

class Client:
    # Initialise a new File System client
    def __init__(self, id, socket, path_to_root):
        self.id = id
        self.socket = socket
        self.dir_level = 0
        # Path to root is the path to the root of the file_system
        self.dir_path = [path_to_root]

    #TODO will need  methods for working with directories



class FileSystemManager:

	#threadPool will contain threads managing the locks used
    file_system_manager_threadpool = threadpool.ThreadPool(1)

    # sctive client list
    active_clients = []

    # Next IDs for both variables
    next_client_id = 0
    next_event_id = 0

    # List of events and IDs
    # ( event_id , command, time )
    events = []


    def __init__(self, root_path):
        self.root_path = root_path
        #Add autorelease function to a new thread
        self.file_system_manager_threadpool.add_task(
            self.auto_release
        )

    # Generate a client ID and update next_client_id
    def gen_client_id(self):
        return_client_id = self.next_client_id
        self.next_client_id = self.next_client_id + 1
        return return_client_id

    # Generate a client ID and update next_event_id
    def gen_event_id(self):
        return_event_id = self.next_event_id
        self.next_event_id = self.next_event_id + 1
        return return_event_id



    # will change directory
    def change_directory(self, dir_name, client_id):

    	#TODO


    # list the contents of a directory
    def list_directory(self, client_id, item_name = ""):

    	#TODO

    # Returns  contents of a file as a string
    def read_item(self, client_id, item_name):

    	#TODO


    # will write a passed string to a file
    def write_item(self, client_id, item_name, file_contents):

    	#TODO



