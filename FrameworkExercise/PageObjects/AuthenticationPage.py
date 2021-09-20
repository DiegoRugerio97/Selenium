from selenium.webdriver.common.by import By

class AuthenticationPage:

    def __init__(self,driver):
        self.driver = driver
        
    #WebElements
    signInButton = (By.LINK_TEXT, "Sign in")
    signOutButton = (By.LINK_TEXT, "Sign out")
    mailField = (By.ID, "email")
    passWordField = (By.ID,"passwd")
    submitButton = (By.ID,"SubmitLogin")
    alertMessage = (By.XPATH,"//div[@class='alert alert-danger']/ol/li")
    accountButton = (By.XPATH,"//a[@class='account']")

    #Methods

    def getSignInButton(self):
        return self.driver.find_element(*AuthenticationPage.signInButton)
    
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

    def refreshPage(self):
        self.driver.refresh()