__author__ = "Rohan Joshi"

'''
python imports
'''
from pymongo import MongoClient
import os
import sys
import yaml
'''
logging setup
'''
import logging

# set up basic logging
#logging.basicConfig(filename="logs/mother.log", level=logging.DEBUG, format='%(asctime)s %(module)s: %(funcName)5s() %(levelname)s:  %(message)s', datefmt='%I:%M:%S %p')

class DatabaseHandler:

    def __init__(self):
        logging.debug("[DatabaseHandler] initializing the database handler")
        self.startup()
        logging.debug("attempting to open connection to database")
        self.client = MongoClient(self.values_dict['mongo_instance'])
        self.db = self.client.apdata

    def startup(self):
        self.open_values()
        logging.debug("server_values.yaml has been opened, validated and registered")
        print("server_values.yaml has been opened, validated and registered")
        print("now attempting to open connection to mongo instance")

    def open_values(self):
        logging.debug("reading from server_values.yaml")
        if os.path.exists('../server_values.yaml'):
            logging.debug("server_values.yaml present")
        else:
            logging.error("cannot find server_values.yaml")
            sys.exit(1)
        self.values_dict = yaml.load(open('../server_values.yaml'))
        for key, value in self.values_dict.items():
            print(key + " is " + str(value))
            self.validate_values(key, value)

    def validate_values(self, key, value):
        logging.debug("checking " + str(key) + " in file_transfer_values.yaml")
        if value == " " or value == "default":
            logging.error(key + " is not valid, exiting")
            print("ERROR: " + str(key) + " is not valid, exiting")
            sys.exit(1)
