from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By

#Address Page
#This page is used to modify the address data of the account.
#It contains several fields, all defined by its WebElement.

class AddressPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #WebElements

    addressInput = (By.ID, "address1")
    addressInput2 = (By.ID, "address2")
    cityInput = (By.ID, "city")
    stateDropDown = (By.ID, "id_state")
    zipInput = (By.ID, "postcode")
    countryDropDown = (By.ID, "id_country")
    homePhoneInput = (By.ID, "phone")
    mobilePhoneInput = (By.ID, "phone_mobile")
    addInformationArea = (By.ID, "other")
    aliasInput = (By.ID, "alias")
    submitButton = (By.ID, "submitAddress")

    #Methods

    def getAddressInput(self):
        return self.driver.find_element(*AddressPage.addressInput)

    def getAddressInput2(self):
        return self.driver.find_element(*AddressPage.addressInput2)

    def getCityInput(self):
        return self.driver.find_element(*AddressPage.cityInput)

    def getStateDropDown(self):
        return self.driver.find_element(*AddressPage.stateDropDown)
    
    def getZipInput(self):
        return self.driver.find_element(*AddressPage.zipInput)

    def getCountryDropDown(self):
        return self.driver.find_element(*AddressPage.countryDropDown)

    def getHomePhoneInput(self):
        return self.driver.find_element(*AddressPage.homePhoneInput)

    def getMobilePhoneInput(self):
        return self.driver.find_element(*AddressPage.mobilePhoneInput)

    def getAddInformationArea(self):
        return self.driver.find_element(*AddressPage.addInformationArea)

    def getAliasInput(self):
        return self.driver.find_element(*AddressPage.aliasInput)

    def getSubmitButton(self):
        return self.driver.find_element(*AddressPage.submitButton)

    #Method for inputting a new Address in the specified Input field, in the test case its only used to 
    #change one of the fields but its funcionality could be extended.
    def inputNewAddress(self,address,webElement):
        webElement.clear()
        webElement.send_keys(address)
        self.getSubmitButton().click()

