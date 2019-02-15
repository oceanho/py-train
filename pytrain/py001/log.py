import logging

handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)

class Logger(object):
  def __init__(self,name):
    self.logger = logging.getLogger(name)
    self.logger.addHandler(handler)
    self.logger.setLevel(logging.INFO)