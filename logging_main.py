# Use logging.getLogger(name) to create a named global logger.
# https://docs.python.org/3/library/logging.html#logging.getLogger

import logging_setup

log_file_size = 10485700  # ~10Mbyte
logger = logging_setup.setup_custom_logger_rotating_f('root', '.\log', 'dsa', log_file_size)
logger.debug('main message')

import logging_submodule
