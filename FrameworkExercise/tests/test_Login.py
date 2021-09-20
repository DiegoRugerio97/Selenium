from Utilities.BaseClass import BaseClass
from PageObjects.AuthenticationPage import AuthenticationPage


class TestLogin(BaseClass):

    def test_invalidLoginMail(self):

        authenticationPage = AuthenticationPage(self.driver)

        authenticationPage.getSignInButton().click()

        authenticationPage.getMailField().send_keys("diego.rugeriomail.com")

        authenticationPage.getPassWordField().send_keys("XXXX#")

        authenticationPage.getSubmitButton().click()

        alertMessage = authenticationPage.getAlertMessage().text
        
        assert "Invalid email" in alertMessage
        
        authenticationPage.refreshPage()

    def test_invalidLoginPasswd(self):

        authenticationPage = AuthenticationPage(self.driver)

        authenticationPage.getSignInButton().click()

        authenticationPage.getMailField().send_keys("diego.rugerio@mail.com")

        authenticationPage.getPassWordField().send_keys("YYYY#")

        authenticationPage.getSubmitButton().click()

        alertMessage = authenticationPage.getAlertMessage().text
        
        assert "Authentication failed" in alertMessage

        authenticationPage.refreshPage()


    def test_validLogin(self):

        authenticationPage = AuthenticationPage(self.driver)
        
        authenticationPage.getSignInButton().click()

        authenticationPage.getMailField().send_keys("diego.rugerio@mail.com")

        authenticationPage.getPassWordField().send_keys("XXXX#")

        authenticationPage.getSubmitButton().click()

        accountName = authenticationPage.getAccountButton().text
        assert accountName == "Diego Rugerio"

        authenticationPage.getSignOutButton().click()


