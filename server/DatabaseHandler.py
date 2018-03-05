__author__ = "Rohan Joshi"


'''
python imports
'''
from pymongo import MongoClient
'''
logging setup
'''
import logging

# set up basic logging
#logging.basicConfig(filename="logs/mother.log", level=logging.DEBUG, format='%(asctime)s %(module)s: %(funcName)5s() %(levelname)s:  %(message)s', datefmt='%I:%M:%S %p')

class DatabaseHandler:

    def __init__(self):
        logging.debug("[DatabaseHandler] initializing the database handler")