__author__ = "Rohan Joshi"

'''
imports for local classes
'''
from DatabaseHandler import DatabaseHandler
from device import Device


'''
python imports
'''


'''
logging setup
'''
import logging

logging.basicConfig(filename="logs/mother.log", level=logging.DEBUG, format='%(asctime)s %(module)s: %(funcName)5s() %(levelname)s:  %(message)s', datefmt='%I:%M:%S %p')

class Server:

    def __init__(self):
        print("STARTING...")
        print("startup process, will be notified when startup is successful")
        print("startup will open connection to mongodb, if not successful, server will crash")
        print("\n")
        logging.debug("starting mother, setting name, address, family to '' ")
        logging.debug("initializing database handler")
        self.databasehandler = DatabaseHandler()
        logging.debug("initializing self.devices to empty list")
        self.devices = []


server = Server()