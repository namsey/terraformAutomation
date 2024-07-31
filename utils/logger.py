import logging
from config.config import read_config


def setup_logging(config_path):
    logging_config = read_config(config_path,'logging')
    level = logging_config.get('logging_level', 'DEBUG')
    formatter = logging_config.get('logging_format', '%(asctime)s %(levelname)s %(message)s')
    log_file = logging_config.get('logging_file', 'terraform_automation.log')

    logging.basicConfig(
        filename=log_file,
        level=level,
        format=formatter
    )
