from PageObjects.HomePage import HomePage
from PageObjects.AuthenticationPage import AuthenticationPage
from Utilities.BaseClass import BaseClass



class TestLogin(BaseClass):

    def test_invalidLoginMail(self):

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.getMailField().send_keys("diego.rugeriomail.com")

        authenticationPage.getPassWordField().send_keys("XXXX#")

        authenticationPage.getSubmitButton().click()

        alertMessage = authenticationPage.getAlertMessage().text
        
        assert "Invalid email" in alertMessage
        
        homePage.goToHomePage()

    def test_invalidLoginPasswd(self):

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.getMailField().send_keys("diego.rugerio@mail.com")

        authenticationPage.getPassWordField().send_keys("YYYY#")

        authenticationPage.getSubmitButton().click()

        alertMessage = authenticationPage.getAlertMessage().text
        
        assert "Authentication failed" in alertMessage

        homePage.goToHomePage()


    def test_validLogin(self):

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.getMailField().send_keys("diego.rugerio@mail.com")

        authenticationPage.getPassWordField().send_keys("XXXX#")

        accountPage = authenticationPage.goToAccountPage()

        accountName = accountPage.getAccountLabel()
        assert accountName == "Diego Rugerio"



