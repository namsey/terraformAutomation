import logging
from config.config import read_config


def setup_logging(config):
    level = config.get('logging_level', 'DEBUG')
    formatter = config.get('logging_format', '%(asctime)s %(levelname)s %(message)s')
    log_file = config.get('logging_file', 'terraform_automation.log')

    logging.basicConfig(
        filename=log_file,
        level=level,
        format=formatter
    )
