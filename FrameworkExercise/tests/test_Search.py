from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

class TestSearch(BaseClass):

    def test_searchShirt(self):
        
        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys("shirt")

        self.verifyElementPresenceByClass("ac_even")

        productPage = homePage.goToProductPage()

        productText = productPage.getProductName()
        
        assert "shirt" in productText

        homePage.goToHomePage()

    def test_invalidSearch(self):

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys("XXXX")

        searchResults = homePage.goToSearchResults()

        alertMessage = searchResults.getAlertText()

        assert "No results" in alertMessage

        homePage.goToHomePage()

    def test_sortedSearch(self):

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys("dress")

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






    

