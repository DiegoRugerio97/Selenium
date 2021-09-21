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

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys(getData_test_A['item'])

        self.verifyElementPresenceByClass("ac_even")

        logger.info("Moving to Product Page")

        productPage = homePage.goToProductPage()

        productPage.getAddToCartButton().click()

        self.verifyElementClickableByXPATH("//a[@title='Proceed to checkout']")

        summaryPage = productPage.goToCheckOut()

        logger.info("Moving to CheckOut Page")
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        logger.info("Signing in")

        addressPageSummary = authenticationPage.signInCheckOut(getData_test_A['mail'],getData_test_A['password'])

        logger.info("In Address Summary page.")

        updateAddressPage = addressPageSummary.goUpdateAddressPage()

        logger.info("Updating address.")

        updateAddressPage.getCityInput().clear()

        newCity = getData_test_A['city']

        updateAddressPage.getCityInput().send_keys(newCity)

        logger.info("Updated city to {}".format(newCity))

        updateAddressPage.getSubmitButton().click()

        addressText = addressPageSummary.getAddressText()

        assert newCity in addressText, logger.error("ADDRESS DID NOT GET UPDATED")

        logger.info("Test completed succesfully")

        addressPageSummary.signOut()

        addressPageSummary.goToHomePage()
    
    def test_EndToEnd(self,getData_test_B):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys(getData_test_B['item'])

        self.verifyElementPresenceByClass("ac_even")

        productPage = homePage.goToProductPage()

        logger.info("Moving to Product Page")

        productPage.getAddToCartButton().click()

        self.verifyElementClickableByXPATH("//a[@title='Proceed to checkout']")

        summaryPage = productPage.goToCheckOut()

        logger.info("Moving to CheckOut Page")
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        logger.info("Signing in")

        addressPageSummary = authenticationPage.signInCheckOut(getData_test_B['mail'],getData_test_B['password'])

        shippingPage = addressPageSummary.goToShippingPage()

        logger.info("Moving to Shipping Page")

        shippingPage.getTermsCheckBox().click()

        paymentPage = shippingPage.goToPaymentPage()

        logger.info("Moving to Payment Page")

        paymentPage.getCheckPaymentButton().click()

        orderConfirmationPage = paymentPage.goToOrderConfirmationPage()

        logger.info("Moving to order confirmation Page")

        message = orderConfirmationPage.getMessageText()

        assert "Your order on My Store is complete." in message

        logger.info("Test completed succesfully")





