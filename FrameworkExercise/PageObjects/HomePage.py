from PageObjects.ContactPage import ContactPage
from PageObjects.AuthenticationPage import AuthenticationPage
from PageObjects.SearchResults import SearchResults
from PageObjects.BasePage import BasePage
from PageObjects.ProductPage import ProductPage
from selenium.webdriver.common.by import By

#Home Page
#First page that will be loaded.
#Used in all of the cases, therefore it has connection to most of the other Page Classes.

class HomePage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #WebElements
    searchField = (By.ID, "search_query_top")
    autoComplete = (By.CLASS_NAME, "ac_even")
    searchButton = (By.NAME, "submit_search")
    contactButton = (By.LINK_TEXT, "Contact us")

    #Methods
    def getSearchField(self): 
        return self.driver.find_element(*HomePage.searchField)

    #Redirection Methods
    def goToProductPage(self):
        self.driver.find_element(*HomePage.autoComplete).click()
        return ProductPage(self.driver)

    def goToSearchResults(self):
        self.driver.find_element(*HomePage.searchButton).click()
        return SearchResults(self.driver)

    def goToAuthenticationPage(self):
        self.driver.find_element(*HomePage.signInButton).click()
        return AuthenticationPage(self.driver)

    def goToContactPage(self):
        self.driver.find_element(*HomePage.contactButton).click()
        return ContactPage(self.driver)

    def searchItem(self,item):
        self.getSearchField().send_keys(item)

    

        