from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestContact(BaseClass):

    def test_ContactMessage(self):

        homePage = HomePage(self.driver)

        contactPage = homePage.goToContactPage()

        self.selectFromDropDown(contactPage.getHeadingDropDown(),"Customer service")

        contactPage.getEmailInput().send_keys("diego.rugerio@mail.com")

        contactPage.getOrderReferenceInput().send_keys("XXXXX")

        contactPage.getMessageArea().send_keys("This is a test message, please ignore.")

        contactPage.getSubmitMessageButton().click()

        message = contactPage.getMessageText()

        assert "successfully" in message

    
