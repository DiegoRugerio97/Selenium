from selenium.webdriver.common.by import By

#This class will be used to define common elements through all the pages, including the <img> tag that will 
#load up the homepage, as well as elements present in the NavBar such as the Sing In/Out buttons.

class BasePage():

    def __init__(self,driver):
        self.driver = driver
        
    #WebElements 

    indexLink = (By.XPATH, "//img[@alt='My Store']")
    signOutButton = (By.LINK_TEXT, "Sign out")
    accountButton = (By.XPATH,"//a[@class='account']")
    signInButton = (By.LINK_TEXT, "Sign in")

    #Methods

    def goToHomePage(self):
        self.driver.find_element(*BasePage.indexLink).click()

    def signOut(self):
        self.driver.find_element(*BasePage.signOutButton).click()

    def getAccountLabel(self):
        return self.driver.find_element(*BasePage.accountButton).text

