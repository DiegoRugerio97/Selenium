from selenium.webdriver.common.by import By

class AccountPage():

    def __init__(self,driver):
        self.driver = driver
    
    #WebElements

    accountButton = (By.XPATH,"//a[@class='account']")

    def getAccountLabel(self):
        return self.driver.find_element(*AccountPage.accountButton).text