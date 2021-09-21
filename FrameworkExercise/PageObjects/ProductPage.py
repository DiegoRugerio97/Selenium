from PageObjects.CheckOutSummaryPage import CheckOutSummaryPage
from selenium.webdriver.common.by import By

class ProductPage():

    def __init__(self,driver):
        self.driver = driver
    
    #WebElements
    productName = (By.TAG_NAME, "h1")
    addToCardButton = (By.XPATH, "//button[@name='Submit']")
    checkOutButton = (By.XPATH, "//a[@title='Proceed to checkout']")

    #Methods

    def getProductName(self):
        return self.driver.find_element(*ProductPage.productName).text

    def getAddToCartButton(self):
        return self.driver.find_element(*ProductPage.addToCardButton)

    def getCheckOutButton(self):
        return self.driver.find_element(*ProductPage.checkOutButton)

    def goToCheckOut(self):
        self.driver.find_element(*ProductPage.checkOutButton).click()
        return CheckOutSummaryPage(self.driver)