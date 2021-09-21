from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

class SearchResults(BasePage):

    def __init__(self,driver):
        self.driver = driver
    
    #WebElements

    alertText = (By.XPATH , "//p[@class='alert alert-warning']")
    sortDropDown = (By.ID, "selectProductSort")
    productNames = (By.XPATH, "//div[@class='right-block']/h5/a[@class='product-name']")


    #Methods 

    def getAlertText(self):
        return self.driver.find_element(*SearchResults.alertText).text

    def getSortDropDown(self):
        return self.driver.find_element(*SearchResults.sortDropDown)

    def getProductNames(self):
        return self.driver.find_elements(*SearchResults.productNames)