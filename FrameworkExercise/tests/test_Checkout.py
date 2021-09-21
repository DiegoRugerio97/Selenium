import pytest
from TestData.CheckOutData import CheckOutData
from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestCheckOut(BaseClass):

    @pytest.fixture(params = CheckOutData.test_CheckOut_data_A)
    def getData_test_A(self,request):
        return request.param

    @pytest.fixture(params = CheckOutData.test_CheckOut_data_B)
    def getData_test_B(self,request):
        return request.param


    def test_updateAddress(self,getData_test_A):

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys(getData_test_A['item'])

        self.verifyElementPresenceByClass("ac_even")

        productPage = homePage.goToProductPage()

        productPage.getAddToCartButton().click()

        self.verifyElementClickableByXPATH("//a[@title='Proceed to checkout']")

        summaryPage = productPage.goToCheckOut()
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        addressPageSummary = authenticationPage.signInCheckOut(getData_test_A['mail'],getData_test_A['password'])

        updateAddressPage = addressPageSummary.goUpdateAddressPage()

        updateAddressPage.getCityInput().clear()

        newCity = getData_test_A['city']

        updateAddressPage.getCityInput().send_keys(newCity)

        updateAddressPage.getSubmitButton().click()

        addressText = addressPageSummary.getAddressText()

        assert newCity in addressText

        addressPageSummary.signOut()

        addressPageSummary.goToHomePage()
    
    def test_EndToEnd(self,getData_test_B):

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys(getData_test_B['item'])

        self.verifyElementPresenceByClass("ac_even")

        productPage = homePage.goToProductPage()

        productPage.getAddToCartButton().click()

        self.verifyElementClickableByXPATH("//a[@title='Proceed to checkout']")

        summaryPage = productPage.goToCheckOut()
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        addressPageSummary = authenticationPage.signInCheckOut(getData_test_B['mail'],getData_test_B['password'])

        shippingPage = addressPageSummary.goToShippingPage()

        shippingPage.getTermsCheckBox().click()

        paymentPage = shippingPage.goToPaymentPage()

        paymentPage.getCheckPaymentButton().click()

        orderConfirmationPage = paymentPage.goToOrderConfirmationPage()

        message = orderConfirmationPage.getMessageText()

        assert "Your order on My Store is complete." in message





