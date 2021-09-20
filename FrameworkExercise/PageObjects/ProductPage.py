from selenium.webdriver.common.by import By

class ProductPage():

    def __init__(self,driver):
        self.driver = driver
    
    #WebElements
    productName = (By.TAG_NAME, "h1")

    #Methods

    def getProductName(self):
        return self.driver.find_element(*ProductPage.productName).text