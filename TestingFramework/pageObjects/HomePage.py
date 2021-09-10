from pageObjects.CheckOutPage import CheckOutPage
from selenium.webdriver.common.by import By
#PAGE OBJECT MODEL
#This class represents the home page, the first page we arrive at, starting the test.
#The WebElement instances related to this specific page, are declared as attributes and methods of this class.

class HomePage:

    #driver will be received from test case code and assigned in constructor when instantiated.
    def __init__(self, driver):
        self.driver = driver

    #WebElements
    shop = (By.LINK_TEXT,"Shop")
    nameForm = (By.NAME, "name")
    emailForm = (By.NAME,"email")
    checkBox = (By.ID, "exampleCheck1")
    submitButton = (By.XPATH, "//input[@value='Submit']")
    successAlert = (By.CLASS_NAME,"alert-success")
    genderDropDown = (By.XPATH, "//select[@id='exampleFormControlSelect1']")

    def getNameForm(self):
        return self.driver.find_element(*HomePage.nameForm)

    def getEmailForm(self):
        return self.driver.find_element(*HomePage.emailForm)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getSuccessAlert(self):
        return self.driver.find_element(*HomePage.successAlert)

    def getGenderDropDown(self):
        return self.driver.find_element(*HomePage.genderDropDown)
    
    #This functions represents self.driver.find_element_by_link_text("Shop") step.
    def goToCheckOutPage(self):
        #* to unpack the tuple
        #We can optimize POM instance creation in the test code by identifying trigger points that will 
        #redirect us to other pages.
        self.driver.find_element(*HomePage.shop).click()
        #Instantiate the next page here, and return it to the test code.
        return CheckOutPage(self.driver)