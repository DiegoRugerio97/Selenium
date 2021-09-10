import logging
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import inspect

#To optimize the framework, define a new base class that will hold all the utilities needed,
#in this case, the fixture browserSetup
@pytest.mark.usefixtures("browserSetup")
class BaseClass():

    def verifyLinkPresence(self, linkText):
        #Wait for auto suggestion to show desired link
        wait = WebDriverWait(self.driver,6)
        #Wait until the link with the desired text is present
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, linkText)))

    def selectFromDropDown(self,webElement,text):
        selector = Select(webElement)
        selector.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName) 
        hdlr = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")    
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.DEBUG)
        return logger