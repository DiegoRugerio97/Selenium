import logging
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import inspect

@pytest.mark.usefixtures("browserSetup")
class BaseClass():

    def moveToElement(self,webElement):
        ActionChains(self.driver).move_to_element(webElement)

    def verifyLinkPresence(self, linkText):
        #Wait for auto suggestion to show desired link
        wait = WebDriverWait(self.driver,6)
        #Wait until the link with the desired text is present
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, linkText)))

    def verifyElementPresenceByClass(self,className):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,className)))

    def selectFromDropDown(self,webElement,text):
        selector = Select(webElement)
        selector.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName) 
        hdlr = logging.FileHandler('..//utilities//logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")    
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.DEBUG)
        return logger

    