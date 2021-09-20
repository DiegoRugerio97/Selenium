from PageObjects.SearchResults import SearchResults
from PageObjects.BasePage import BasePage
from PageObjects.ProductPage import ProductPage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #WebElements
    searchField = (By.ID, "search_query_top")
    autoComplete = (By.CLASS_NAME, "ac_even")
    searchButton = (By.NAME, "submit_search")

    #Methods
    def getSearchField(self): 
        return self.driver.find_element(*HomePage.searchField)

    def goToProductPage(self):
        self.driver.find_element(*HomePage.autoComplete).click()
        return ProductPage(self.driver)

    def goToSearchResults(self):
        self.driver.find_element(*HomePage.searchButton).click()
        return SearchResults(self.driver)


    

        