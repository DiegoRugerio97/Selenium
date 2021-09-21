from TestData.LoginData import LoginData
import pytest
from PageObjects.HomePage import HomePage
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

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.signIn(getData_test_A['mail'], getData_test_A['password'])

        alertMessage = authenticationPage.getAlertMessage()
        
        assert "Invalid email" in alertMessage, logger.error("APP DID NOT DISPLAY ERROR MESSAGE")

        logger.info("Test completed succesfully")
        
        authenticationPage.goToHomePage()

    def test_invalidLoginPasswd(self, getData_test_B):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.signIn(getData_test_B['mail'], getData_test_B['password'])

        alertMessage = authenticationPage.getAlertMessage()
        
        assert "Authentication failed" in alertMessage, logger.error("APP DID NOT DISPLAY ERROR MESSAGE")

        logger.info("Test completed succesfully")

        authenticationPage.goToHomePage()


    def test_validLogin(self, getData_test_C):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        accountPage = authenticationPage.signIn(getData_test_C['mail'], getData_test_C['password'])

        accountName = accountPage.getAccountLabel()
        
        assert accountName == "Diego Rugerio", logger.error("APP DID NOT LOG IN CORRECT USER")

        logger.info("Test completed succesfully")




