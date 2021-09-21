from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from PageObjects.AuthenticationPage import AuthenticationPage

class CheckOutSummaryPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #WebElements

    proceedToCheckoutButton = (By.XPATH, "//p/a[@title='Proceed to checkout']")

    #Methods

    def goToAuthenticationPage(self):
        self.driver.find_element(*CheckOutSummaryPage.proceedToCheckoutButton).click()
        return AuthenticationPage(self.driver)

