from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self,driver):
        self.driver = driver
        
    #WebElements 

    indexLink = (By.XPATH, "//img[@alt='My Store']")
    signOutButton = (By.LINK_TEXT, "Sign out")


    #Methods

    def goToHomePage(self):
        self.driver.find_element(*BasePage.indexLink).click()

    def signOut(self):
        self.driver.find_element(*BasePage.signOutButton).click()

