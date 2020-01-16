import logging
import time

logger = logging.getLogger('root')
n = 0
while 1:
    n += 1
    logger.debug(f'submodule message {n}')
    time.sleep(0.01)
