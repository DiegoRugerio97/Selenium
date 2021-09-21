from PageObjects.CheckOutAddressPage import CheckOutAddressPage
from PageObjects.BasePage import BasePage
from PageObjects.AccountPage import AccountPage
from selenium.webdriver.common.by import By

class AuthenticationPage(BasePage):

    def __init__(self,driver):
        self.driver = driver
        
    #WebElements
    
    signOutButton = (By.LINK_TEXT, "Sign out")
    mailField = (By.ID, "email")
    passWordField = (By.ID,"passwd")
    submitButton = (By.ID,"SubmitLogin")
    alertMessage = (By.XPATH,"//div[@class='alert alert-danger']/ol/li")
   

    #Methods

    def getSignOutButton(self):
        return self.driver.find_element(*AuthenticationPage.signOutButton)

    def getMailField(self):
        return self.driver.find_element(*AuthenticationPage.mailField)
    
    def getPassWordField(self):
        return self.driver.find_element(*AuthenticationPage.passWordField)

    def getSubmitButton(self):
        return self.driver.find_element(*AuthenticationPage.submitButton)

    def getAlertMessage(self):
        return self.driver.find_element(*AuthenticationPage.alertMessage)

    def getAccountButton(self):
        return self.driver.find_element(*AuthenticationPage.accountButton)

    def goToAccountPage(self):
        self.driver.find_element(*AuthenticationPage.submitButton).click()
        return AccountPage(self.driver)

    def signInCheckOut(self,mail,password):
        self.driver.find_element(*AuthenticationPage.mailField).send_keys(mail)
        self.driver.find_element(*AuthenticationPage.passWordField).send_keys(password)
        self.driver.find_element(*AuthenticationPage.submitButton).click()
        return CheckOutAddressPage(self.driver)

        

