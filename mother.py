__author__ = "Rohan Joshi"

import logging

# set up basic logging
logging.basicConfig(filename="mother.log", level=logging.DEBUG, format='%(asctime)s %(funcName)5s() %(levelname)s:  %(message)s', datefmt='%I:%M:%S %p')

class Server:

    def __init__(self):
        logging.debug("starting mother")