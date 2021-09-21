from PageObjects.CheckOutShippingPage import CheckOutShippingPage
from PageObjects.AddressPage import AddressPage
from selenium.webdriver.common.by import By

class CheckOutAddressPage():

    def __init__(self,driver):
        self.driver = driver

    #WebElements

    sameAddressCheck = (By.ID, "addressesAreEquals")
    updateAddressButton = (By.XPATH, "//a[@title='Update']")
    addressText = (By.XPATH, "//li[@class='address_city address_state_name address_postcode']")
    checkoutButton = (By.NAME, "processAddress")

    #Methods

    def getAddressCheck(self):
        return self.driver.find_element(*CheckOutAddressPage.sameAddressCheck)

    def goUpdateAddressPage(self):
        self.driver.find_element(*CheckOutAddressPage.updateAddressButton).click()
        return AddressPage(self.driver)

    def getAddressText(self):
        return self.driver.find_element(*CheckOutAddressPage.addressText).text

    def goToShippingPage(self):
        self.driver.find_element(*CheckOutAddressPage.checkoutButton).click()
        return CheckOutShippingPage(self.driver)
        
    
    