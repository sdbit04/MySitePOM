import logging
import inspect


def customLogger(loglevel):
    LoggerName=inspect.stack()[1][3]
    logger=logging.getLogger(LoggerName)
    logger.setLevel(logging.DEBUG)

    StrmHandler=logging.StreamHandler()
    StrmHandler.setLevel(loglevel)

    formatter=logging.Formatter('%(name)s - %(levelname)s: %(message)s')

    StrmHandler.setFormatter(formatter)
    logger.addHandler(StrmHandler)

    return logger
