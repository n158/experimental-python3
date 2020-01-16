import os
import time
import logging
from logging.handlers import RotatingFileHandler


def get_filename(paths):
    # Get logs directory
    log_directory, filename = os.path.split(paths)
    # Get file name w/o extensions
    split = os.path.splitext
    filename = split(split(filename)[0])[0]
    # Create new file name
    timestamp = time.strftime("_%m%d-%H%M")
    filename = os.path.join(log_directory, filename+timestamp)

    # Don't add index if not necessary
    f = f'{filename}.log'
    if not os.path.exists(f):
        return f
    else:  # avoiding data loss due to fast logging by adding index to the end of filename
        index = 0
        f = f'{filename}.{index}.log'
        while os.path.exists(f):
            index += 1
            f = f'{filename}.{index}.log'
        return f


def setup_custom_logger_f(name, path, filename):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as ex:
        print(f"Exception while creating logging directory. \n{ex}")
        raise ex

    timestamp = time.strftime("_%Y%m%d-%H%M%S.log")
    full_path = os.path.join(path, filename + timestamp)

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    handler_s = logging.StreamHandler()
    handler_s.setFormatter(formatter)
    handler_f = logging.FileHandler(full_path)
    handler_f.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler_s)
    logger.addHandler(handler_f)
    return logger


def setup_custom_logger_rotating_f(name, path, filename, max_bytes):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as ex:
        print(f"Exception while creating logging directory. \n{ex}")
        raise ex

    timestamp = time.strftime("_%y%m%d-%H%M.log")
    full_path = os.path.join(path, filename + timestamp)

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    handler_s = logging.StreamHandler()
    handler_s.setFormatter(formatter)
    handler_f = RotatingFileHandler(full_path, maxBytes=max_bytes, backupCount=1)
    handler_f.namer = get_filename  # custom log file namer
    handler_f.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler_s)
    logger.addHandler(handler_f)
    return logger
