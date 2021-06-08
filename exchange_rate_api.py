import os
import logging
import requests
import configparser
import logging.config


class ExchangeRateAPI:

    def __init__(self, api):

        # Accessing config file path
        config = configparser.ConfigParser()
        config.read(os.path.dirname(__file__) + '/config.ini')
        self.url = config.get(api, 'url')
        self.header = {'content-type': 'application/json'}

        # Configure the logger
        # loggerConfigFileName: The name and path of your configuration file
        logging.config.fileConfig(os.path.normpath("log_config.conf"))

    def get(self):

        response_data = {}
        try:
            response = requests.get(self.url, headers=self.header)
            response_data = dict(response.json())
        except Exception as e:
            print("Connection error: " + str(e))

        # Create the logger
        # Admin_Client: The name of a logger defined in the config file
        my_logger = logging.getLogger('Admin_Client')
        msg = 'This is a debug message'
        my_logger.debug(msg)
        my_logger.info(msg)
        my_logger.warn(msg)
        my_logger.error(msg)
        my_logger.critical(msg)

        # Shut down the logger
        logging.shutdown()

        return response_data
