from selenium.webdriver.common.by import By

#PAGE OBJECT MODEL
#This class represents the confirm purchase page, the last page we arrive at, where we select the country and confirm the purchase.
#The WebElement instances related to this specific page, are declared as attributes and methods of this class

class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    #WebElements

    countryInput = (By.XPATH, "//input[@id='country']")
    suggestionLink = (By.LINK_TEXT, "United Kingdom")
    checkBox = (By.XPATH, "//input[@id='checkbox2']")
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    successMessage = (By.CLASS_NAME, "alert-success")


    #Methods
    def getCountryInput(self):
        return self.driver.find_element(*ConfirmPage.countryInput)

    def getSuggestion(self):
        return self.driver.find_element(*ConfirmPage.suggestionLink)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)