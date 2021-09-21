from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

class ContactPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    #WebElements

    headingDropDown = (By.ID, "id_contact")
    emailInput = (By.ID, "email")
    orderReferenceInput = (By.ID, "id_order")
    messageArea = (By.ID, "message")
    submitMessageButton =(By.NAME,"submitMessage")
    messageText = (By.XPATH, "//p[@class='alert alert-success']")

    #Methods

    def getHeadingDropDown(self):
        return self.driver.find_element(*ContactPage.headingDropDown)

    def getEmailInput(self):
        return self.driver.find_element(*ContactPage.emailInput)

    def getOrderReferenceInput(self):
        return self.driver.find_element(*ContactPage.orderReferenceInput)

    def getMessageArea(self):
        return self.driver.find_element(*ContactPage.messageArea)
    
    def getSubmitMessageButton(self):
        return self.driver.find_element(*ContactPage.submitMessageButton)

    def getMessageText(self):
        return self.driver.find_element(*ContactPage.messageText).text