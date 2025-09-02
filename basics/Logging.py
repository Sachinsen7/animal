import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%M/%D/%Y %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')


import logging
logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logging.error('This is an error')