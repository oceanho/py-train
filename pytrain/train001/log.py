import logging

logger = logging.getLogger('py-train.pytrain001.log')
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists')

def log_warn(msg):
    logger.warn("[API - log_warn] {msg}".format(msg=msg))