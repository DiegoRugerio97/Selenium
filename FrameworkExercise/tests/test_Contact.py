from TestData.ContactData import ContactData
import pytest
from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestContact(BaseClass):
    
    @pytest.fixture(params = ContactData.test_Contact_data_A)
    def getData_test_A(self,request):
        return request.param


    def test_ContactMessage(self,getData_test_A):

        homePage = HomePage(self.driver)

        contactPage = homePage.goToContactPage()

        self.selectFromDropDown(contactPage.getHeadingDropDown(),getData_test_A['heading'])

        contactPage.getEmailInput().send_keys(getData_test_A['mail'])

        contactPage.getOrderReferenceInput().send_keys(getData_test_A['order'])

        contactPage.getMessageArea().send_keys(getData_test_A['message'])

        contactPage.getSubmitMessageButton().click()

        message = contactPage.getMessageText()

        assert "successfully" in message

    
