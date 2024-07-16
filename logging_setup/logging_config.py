import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_file='app.log'):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        handlers=[RotatingFileHandler(log_file, maxBytes=1000000, backupCount=3)])
