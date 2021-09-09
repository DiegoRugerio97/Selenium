#In-built Python package for logging test information in another file.
import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__) 

    #To indicate the log file use .addHandler(hdlr)
    # hdlr needs to be an instance of class FilehHandler, which saves the location of the log file.
    #Each run of the script, logging will continue to write logs on same file, previous content won't be overwritten.
    hdlr = logging.FileHandler('logfile.log')

    #Indicate to the logger, the format of the message to be logged.
    # %(variable)s to be evaulated at run time. 
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")    
    #Pass Formatter info to the FileHandler instance
    hdlr.setFormatter(formatter)

    #Pass handler to the logger instance
    logger.addHandler(hdlr)

    #Finally, set the level to filter the logs
    #This will filter the logs from INFO category onwards, meaning no DEBUG logs will be logged.
    logger.setLevel(logging.INFO)


    #There is a hierarchy of the log levels:
    #1- One of the log types : DEBUG
    logger.debug("Debug statement is executed")

    #2- One of the log types : INFO
    logger.info("Information on execution")

    #3- One of the log types : WARNING
    logger.warning("This is a warning")

    #4- One of the log types : ERROR
    #Used for assertion fail statement
    logger.error("This is an error message")

    #5- One of the log types : CRITICAL
    logger.critical("CRITICAL")
