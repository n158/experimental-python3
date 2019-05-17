import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s %(levelname)-8s %(message)s')

try:
    assert True == False, "You can't overcome the truth."
except AssertionError:
    logging.error("Nothing is real but I can't quit...", exc_info = True)

logging.info("You shall pass now.")
