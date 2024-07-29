import logging
import json
import os


def setup_logging():
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.json')

    with open(config_path) as config_file:
        config = json.load(config_file)
        logging_config = config.get('logging', {})

        level = logging_config.get('level', 'INFO')
        format = logging_config.get('format', '%(asctime)s %(levelname)s %(message)s')

        logging.basicConfig(level=level,
                            format=format,
                            handlers=[logging.StreamHandler()])
        logging.info("Logging configured successfully with level: %s and format: %s", level, format)
