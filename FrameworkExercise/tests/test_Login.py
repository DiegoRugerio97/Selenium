from TestData.LoginData import LoginData
import pytest
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

#Login test case
#Test the Login Functionality in the Store App.

class TestLogin(BaseClass):

    #Defining the data loader fixtures for each test scenario
    @pytest.fixture(params = LoginData.test_Login_data_A)
    def getData_test_A(self,request):
        return request.param
    
    @pytest.fixture(params = LoginData.test_Login_data_B)
    def getData_test_B(self,request):
        return request.param

    @pytest.fixture(params = LoginData.test_Login_data_C)
    def getData_test_C(self,request):
        return request.param

    #Verify that entering an invalid email on Sign In, the error message is displayed on app.
    def test_invalidLoginMail(self, getData_test_A):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.signIn(getData_test_A['mail'], getData_test_A['password'])

        alertMessage = authenticationPage.getAlertMessage()
        
        assert "Invalid email" in alertMessage, logger.error("APP DID NOT DISPLAY ERROR MESSAGE")

        logger.info("Test completed succesfully")
        
        authenticationPage.goToHomePage()

    #Verify that entering an invalid password on Sign In form, the error message is displayed on app.
    def test_invalidLoginPasswd(self, getData_test_B):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        authenticationPage.signIn(getData_test_B['mail'], getData_test_B['password'])

        alertMessage = authenticationPage.getAlertMessage()
        
        assert "Authentication failed" in alertMessage, logger.error("APP DID NOT DISPLAY ERROR MESSAGE")

        logger.info("Test completed succesfully")

        authenticationPage.goToHomePage()

    #Verify that entering an valid Email and Password on Sign In, the app loads up the correct username
    def test_validLogin(self, getData_test_C):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        authenticationPage = homePage.goToAuthenticationPage()

        accountPage = authenticationPage.signIn(getData_test_C['mail'], getData_test_C['password'])

        accountName = accountPage.getAccountLabel()
        
        assert accountName == "Diego Rugerio", logger.error("APP DID NOT LOG IN CORRECT USER")

        logger.info("Test completed succesfully")




