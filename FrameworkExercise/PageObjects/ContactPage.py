from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage

#Contact Page
#Used as a portal for the user to contact customer service or the IT team. 

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

    def inputEmail(self,email):
        self.getEmailInput().send_keys(email)

    def inputOrderReference(self,order):
        self.getOrderReferenceInput().send_keys(order)

    def inputMessage(self,message):
        self.getMessageArea().send_keys(message)

    def submitContactMessage(self,email,order,message):
        self.inputEmail(email)
        self.inputOrderReference(order)
        self.inputMessage(message)
        self.getSubmitMessageButton().click()

    