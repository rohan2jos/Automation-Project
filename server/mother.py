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
        logging.debug("starting mother, setting name, address, family to '' ")
        logging.debug("initializing database handler")
        self.databasehandler = DatabaseHandler()
        logging.debug("initializing self.devices to empty list")
        self.devices = []

    def contact_db(self):
        logging.debug("opening connection to mongo db")

server = Server()