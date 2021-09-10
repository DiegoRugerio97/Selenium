from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage
#PAGE OBJECT MODEL
#This class represents the shop page, the second page we arrive at,where we select the item, and go to checkout.
#The WebElement instances related to this specific page, are declared as attributes and methods of this class.

class CheckOutPage:

    #driver will be received from test case code and assigned in constructor when instantiated.
    def __init__(self, driver):
        self.driver = driver

    #WebElements
    cards = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    addButton = (By.XPATH, "div/button")
    checkOutButton = (By.PARTIAL_LINK_TEXT,"Checkout")
    confirmButton = (By.XPATH,"//button[@class='btn btn-success']")
    
    #This functions represents self.driver.find_elements_by_xpath("//div[@class='card h-100']")) step.
    def getCards(self):
        #First locate the overall wrapping div, common parent of elements.
        #Each element is //div[@class='card h-100']
        return self.driver.find_elements(*CheckOutPage.cards)

    #Get the product name for that specific card
    def getProductName(self,card):
        return card.find_element(*CheckOutPage.productName).text

    #Get the button for that specific card
    def getAddButton(self,card):
        return card.find_element(*CheckOutPage.addButton)

    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)

    def goToConfirmPage(self):
        self.driver.find_element(*CheckOutPage.confirmButton).click()
        #Instantiate the next page here, and return it to the test code.
        return ConfirmPage(self.driver)
