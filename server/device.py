import logging

# set up basic logging
logging.basicConfig(filename="device.log", level=logging.DEBUG, format='%(asctime)s %(funcName)5s() %(levelname)s:  %(message)s', datefmt='%I:%M:%S %p')


class Device:

    def __init__(self):
        logging.debug("initializing device")
        self.name = ""
        self.address = ""
        self.family = ""