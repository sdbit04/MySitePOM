import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')
logging.error("This {} is error message".format(9))
logging.debug("This {} is debug message".format(10))
logging.warning("this is warning message")


#We could have used the above way to write log
#But if we use, a logger object we can mention the methode or class which has written the log
"""
def createLog():
    logger = logging.getLogger("LoggerMethodeName")
    hadler=logging.StreamHandler()
    formatter=logging.Formatter('%(name)s - %(levelname)s: %(message)s')
    hadler.setFormatter(formatter)
    logger.addHandler(hadler)
    logger.error(" This {} is error message".format(9))
createLog()
"""