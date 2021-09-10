from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

#STANDARD
#All test cases wrapped in a class

#STANDARD
# request.cls.driver belongs to this test case class
#By defining a base class, we can inherit from it, optimizing code, omitting the application of the
#fixtures decorator.
class TestOne(BaseClass):

    def test_e2e(self):
        #Using the E2E test case in Hands-on/EndToEnd
        #STANDARD
        #Move all of the initial browser setup to a fixture, reducing size of actual Selenium script.
        #In the fixture, we passed on the driver initialized there, as a class attribute, therefore
        #we call this WebDriver instance by self.driver

        #STANDARD/BEST PRACTICE
        #Use the Page Object Model to move all WebElement instances related to an specific page, to a class.

        #Get the logger from the base class
        logger = self.getLogger()
        
        #Instantiate a Page Object Model HomePage instance and pass the driver
        homePage = HomePage(self.driver)

        #Going to shop page
        # goToCheckOutPage() method creates an instance of the CheckOutPage class and returns it.
        # Cleaning that part of the code from here.
        checkOutPage =  homePage.goToCheckOutPage()
        logger.info("Moving to Checkout Page")

        #Adding an iphone X and Blackberry to the cart
        logger.info("Getting all cards")
        cards = checkOutPage.getCards()
        for card in cards:
            productName = checkOutPage.getProductName(card)
            if productName == 'Blackberry' or productName == 'iphone X':
                logger.info("{} card found, adding to cart.".format(productName))
                button = checkOutPage.getAddButton(card)
                button.click()

        #Open checkout
        checkOutPage.getCheckOutButton().click()
        #Go to the confirm page goToConfirmPage() method instantiates a ConfirmPage object and returns it to confirmPage
        confirmPage = checkOutPage.goToConfirmPage()
        logger.info("Moving to Confirm Page")
        #Input the string "Un" to start the autosuggestion
        confirmPage.getCountryInput().send_keys("Un")

        #Moved explicit wait code to the BaseClass
        self.verifyLinkPresence("United Kingdom")

        #Then click the link once it is present
        confirmPage.getSuggestion().click()
        logger.info("Link is present, clicking it.")

        #Trying to click the input directly wont work, either use ...css_selector("[type='submit'") or JSE
        #JSE
        self.driver.execute_script("arguments[0].click();",confirmPage.getCheckBox())
        #Confirm the purchase
        confirmPage.getPurchaseButton().click()

        logger.info("Text received from page: {}".format(confirmPage.getSuccessMessage().text))

        assert ('Success' in confirmPage.getSuccessMessage().text)


        

