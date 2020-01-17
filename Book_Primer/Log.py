import logging
from datetime import datetime


logging.basicConfig(level='DEBUG', filename='sample.log')
logger = logging.getLogger('Python')

msg = str(datetime.now()) +  ':sample debug message'
logger.debug(msg)

msg = str(datetime.now()) +  ':sample warning message'
logger.warning(msg)