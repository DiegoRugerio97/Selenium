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

    def verifyElementPresence(self,byTuple):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.presence_of_element_located(byTuple))

    def verifyElementClickable(self,byTuple):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(byTuple))

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

    