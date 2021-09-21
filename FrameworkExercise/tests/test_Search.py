from TestData.SearchData import SearchData
import pytest
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

class TestSearch(BaseClass):

    @pytest.fixture(params = SearchData.test_Search_data_A)
    def getData_test_A(self,request):
        return request.param

    @pytest.fixture(params = SearchData.test_Search_data_B)
    def getData_test_B(self,request):
        return request.param

    @pytest.fixture(params = SearchData.test_Search_data_C)
    def getData_test_C(self,request):
        return request.param

    def test_searchShirt(self, getData_test_A):
        
        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys(getData_test_A['item'])

        self.verifyElementPresenceByClass("ac_even")

        productPage = homePage.goToProductPage()

        productText = productPage.getProductName()
        
        assert getData_test_A['item'] in productText

        productPage.goToHomePage()

    def test_invalidSearch(self, getData_test_B):

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys( getData_test_B['item'])

        searchResults = homePage.goToSearchResults()

        alertMessage = searchResults.getAlertText()

        assert "No results" in alertMessage

        searchResults.goToHomePage()

    def test_sortedSearch(self, getData_test_C):

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys( getData_test_C['item'])

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

        assert sorted(namesSortedList) == namesSortedList


