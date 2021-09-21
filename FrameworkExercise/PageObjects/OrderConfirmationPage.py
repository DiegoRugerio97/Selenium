from selenium.webdriver.common.by import By

class OrderConfirmationPage():

    def __init__(self,driver):
        self.driver = driver

    #WebElements

    message = (By.XPATH, "//p[@class='alert alert-success']")

    #Methods

    def getMessageText(self):
        return self.driver.find_element(*OrderConfirmationPage.message).text