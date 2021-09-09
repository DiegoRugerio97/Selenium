import logging
import inspect

#Utility class, setting up the logger and returning it to be used in actual PyTest test files.
#In test file, import the logger utility class.

class LogClass():

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__) 
        hdlr = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")    
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)

        logger.setLevel(logging.DEBUG)

        return logger