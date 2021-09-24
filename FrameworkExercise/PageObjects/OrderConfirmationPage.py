from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

#Order Confirmation Page
#Final page in the checkout process.

class OrderConfirmationPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #WebElements

    message = (By.XPATH, "//p[@class='alert alert-success']")

    #Methods

    def getMessageText(self):
        return self.driver.find_element(*OrderConfirmationPage.message).text