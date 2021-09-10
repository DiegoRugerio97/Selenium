
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest


 
class TestHomePage(BaseClass):

    #Pass the data loader fixture into the test case function
    def test_formSubmission(self, getData):
       
        homePage = HomePage(self.driver)

        homePage.getNameForm().send_keys(getData["name"])

        homePage.getEmailForm().send_keys(getData["email"])

        homePage.getCheckBox().click()

        #Select from dropdown code moved to the BaseClass
        self.selectFromDropDown(homePage.getGenderDropDown(),getData["gender"])

        homePage.getSubmitButton().click()

        assert "Success" in homePage.getSuccessAlert().text

        self.driver.refresh()

    
    #Define the data loader fixture
    #BEST PRACTICE
    #Use dictionaries in data loader fixture to make code more readable
    #Put the data into a class for better organization
    @pytest.fixture(params = HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param
    


