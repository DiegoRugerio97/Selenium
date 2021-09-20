from Utilities.BaseClass import BaseClass

class TestSearch(BaseClass):

    def test_searchShirt(self):

        searchField = self.driver.find_element_by_id("search_query_top")
        searchField.send_keys("shirt")

        self.verifyElementPresenceByClass("ac_even")

        autoCompletion = self.driver.find_element_by_class_name("ac_even")
        autoCompletion.click()

        productText = self.driver.find_element_by_tag_name("h1").text
        
        assert "shirt" in productText

        homePage = self.driver.find_element_by_xpath("//img[@alt='My Store']")
        homePage.click()

    def test_invalidSearch(self):

        searchField = self.driver.find_element_by_id("search_query_top")
        searchField.send_keys("XXXX")

        searchButton = self.driver.find_element_by_name("submit_search")
        searchButton.click()

        alertMessage = self.driver.find_element_by_xpath("//p[@class='alert alert-warning']").text

        assert "No results" in alertMessage

        homePage = self.driver.find_element_by_xpath("//img[@alt='My Store']")
        homePage.click()

    

