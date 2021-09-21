from TestData.LoginData import LoginData
import pytest
from PageObjects.HomePage import HomePage
from PageObjects.AuthenticationPage import AuthenticationPage
from Utilities.BaseClass import BaseClass



class TestLogin(BaseClass):

    @pytest.fixture(params = LoginData.test_Login_data_A)
    def getData_test_A(self,request):
        return request.param
    
    @pytest.fixture(params = LoginData.test_Login_data_B)
    def getData_test_B(self,request):
        return request.param

    @pytest.fixture(params = LoginData.test_Login_data_C)
    def getData_test_C(self,request):
        return request.param


    def test_invalidLoginMail(self, getData_test_A):

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.getMailField().send_keys(getData_test_A['mail'])

        authenticationPage.getPassWordField().send_keys(getData_test_A['password'])

        authenticationPage.getSubmitButton().click()

        alertMessage = authenticationPage.getAlertMessage().text
        
        assert "Invalid email" in alertMessage
        
        authenticationPage.goToHomePage()

    def test_invalidLoginPasswd(self, getData_test_B):

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.getMailField().send_keys(getData_test_B['mail'])

        authenticationPage.getPassWordField().send_keys(getData_test_B['password'])

        authenticationPage.getSubmitButton().click()

        alertMessage = authenticationPage.getAlertMessage().text
        
        assert "Authentication failed" in alertMessage

        authenticationPage.goToHomePage()


    def test_validLogin(self, getData_test_C):

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.getMailField().send_keys( getData_test_C['mail'])

        authenticationPage.getPassWordField().send_keys( getData_test_C['password'])

        accountPage = authenticationPage.goToAccountPage()

        accountName = accountPage.getAccountLabel()
        
        assert accountName == "Diego Rugerio"



