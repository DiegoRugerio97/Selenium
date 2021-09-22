from TestData.SearchData import SearchData
import pytest
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

#Search Test case
#Test the Search and Sort Functionality in the Store App.


class TestSearch(BaseClass):

    #Defining the data loader fixtures for each test scenario
    @pytest.fixture(params = SearchData.test_Search_data_A)
    def getData_test_A(self,request):
        return request.param

    @pytest.fixture(params = SearchData.test_Search_data_B)
    def getData_test_B(self,request):
        return request.param

    @pytest.fixture(params = SearchData.test_Search_data_C)
    def getData_test_C(self,request):
        return request.param

    #Verify that searching for an specific item in the Search Bar returns the correct Product Page.
    def test_searchItem(self, getData_test_A):

        logger = self.getLogger()
        
        homePage = HomePage(self.driver)

        homePage.searchItem(getData_test_A['item'])

        self.verifyElementPresence(homePage.autoComplete)

        productPage = homePage.goToProductPage()

        productText = productPage.getProductName()
        
        assert getData_test_A['item'] in productText, logger.error("APP DID NOT SEARCH FOR CORRECT ITEM")

        logger.info("Test completed succesfully")

        productPage.goToHomePage()

    #Verify that entering an invalid item in the Search Bar, returns the Search Results page with an error message.
    def test_invalidSearch(self, getData_test_B):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        homePage.searchItem(getData_test_B['item'])

        searchResults = homePage.goToSearchResults()

        alertMessage = searchResults.getAlertText()

        assert "No results" in alertMessage

        logger.info("Test completed succesfully"), logger.error("APP DID NOT DISPLAY ERROR MESSAGE")

        searchResults.goToHomePage()

    #Verify that the sorting functionality is working correctly on the Store App.
    def test_sortedSearch(self, getData_test_C):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        homePage.searchItem(getData_test_C['item'])

        searchResults = homePage.goToSearchResults()

        sortDropDown = searchResults.getSortDropDown()

        productNames = searchResults.getProductNames()
        namesUnSortedList = []

        for name in productNames:
            namesUnSortedList.append(name.text)

        self.selectFromDropDown(sortDropDown,"Product Name: A to Z")

        productNames = searchResults.getProductNames()
        namesSortedList = []

        for name in productNames:
            namesSortedList.append(name.text)

        assert sorted(namesSortedList) == namesSortedList, logger.error("APP DID NOT SORT PRODUCTS CORRECTLY")

        logger.info("Test completed succesfully")



