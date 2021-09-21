from PageObjects.OrderConfirmationPage import OrderConfirmationPage
from selenium.webdriver.common.by import By

class CheckOutPaymentPage:

    def __init__(self,driver):
        self.driver = driver
    
    #WebElements

    wirePaymentButton = (By.XPATH, "//a[@class='bankwire']")
    checkPaymentButton = (By.XPATH, "//a[@class='cheque']")
    confirmOrderButton = (By.XPATH, "//p/button[@type='submit']")

    #Methods

    def getWirePaymentButton(self):
        return self.driver.find_element(*CheckOutPaymentPage.wirePaymentButton)

    def getCheckPaymentButton(self):
        return self.driver.find_element(*CheckOutPaymentPage.checkPaymentButton)

    def goToOrderConfirmationPage(self):
        self.driver.find_element(*CheckOutPaymentPage.confirmOrderButton).click()
        return OrderConfirmationPage(self.driver)