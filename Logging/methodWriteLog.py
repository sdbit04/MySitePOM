import logging
from Logging.customLogger import customLogger as CL


def method1():
    logger=CL(logging.DEBUG)
    logger.error("this is an error")
    logger.warning("this is warning")


def method2():
    logger=CL(logging.DEBUG)
    logger.info("this is an warning")
    logger.critical("this is critical")


def method3():
    logger=CL(logging.ERROR)
    logger.warning("this is an warning")
    logger.critical("This is critical ")


method1()
method2()
method3()
