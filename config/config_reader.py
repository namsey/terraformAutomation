import json
import logging
import os


def read_config():
    try:
        # Construct the path to the config file relative to the project's root directory
        config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.json')

        with open(config_path) as config_file:
            config = json.load(config_file)
            logging.info("Configuration file loaded successfully.")
            return config
    except FileNotFoundError:
        logging.error("Configuration file (config.json) not found.")
        raise
    except KeyError as e:
        logging.error(f"KeyError: Missing key {e} in configuration file.")
        raise
