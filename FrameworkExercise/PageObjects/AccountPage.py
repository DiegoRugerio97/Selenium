from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By

#Account Page
#Page that loads up after performing the Sign In action in the app, through the Authentication Page.
#Test cases only need the accountButton text to verify if the correct user was logged in.

class AccountPage(BasePage):

    def __init__(self,driver):
        self.driver = driver
    
    #WebElements

    accountButton = (By.XPATH,"//a[@class='account']")

    def getAccountLabel(self):
        return self.driver.find_element(*AccountPage.accountButton).text