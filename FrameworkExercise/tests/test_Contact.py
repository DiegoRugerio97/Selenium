from TestData.ContactData import ContactData
import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

#Contact Test Case
#Test the Contact Us Functionality in the Store App.

class TestContact(BaseClass):
    
    #Defining the data loader fixture for the test scenarios
    @pytest.fixture(params = ContactData.test_Contact_data_A)
    def getData_test_A(self,request):
        return request.param

    #Verify that the Contact Us Message is sent correctly to the Back-End.
    def test_ContactMessage(self,getData_test_A):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        contactPage = homePage.goToContactPage()

        self.verifyElementPresence(contactPage.headingDropDown)

        self.selectFromDropDown(contactPage.getHeadingDropDown(),getData_test_A['heading'])

        contactPage.submitContactMessage(getData_test_A['mail'],getData_test_A['order'],getData_test_A['message'])

        message = contactPage.getMessageText()

        assert "successfully" in message, logger.error("CONTACT MESSAGE SUBMISSION FAILED")

        logger.info("Test completed succesfully")


    
