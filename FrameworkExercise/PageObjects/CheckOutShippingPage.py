from PageObjects.CheckOutPaymentPage import CheckOutPaymentPage
from selenium.webdriver.common.by import By

class CheckOutShippingPage():

    def __init__(self,driver):
        self.driver = driver
    
    #WebElements
    termsCheckBox = (By.ID, "cgv")
    checkOutButton = (By.NAME, "processCarrier")

    #Methods

    def getTermsCheckBox(self):
        return self.driver.find_element(*CheckOutShippingPage.termsCheckBox)

    def goToPaymentPage(self):
        self.driver.find_element(*CheckOutShippingPage.checkOutButton).click()
        return CheckOutPaymentPage(self)


