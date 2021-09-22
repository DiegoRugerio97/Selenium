import pytest
from TestData.CheckOutData import CheckOutData
from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

#Checkout Test case.
#Test the CheckOut Functionality in the Store App.

class TestCheckOut(BaseClass):

    #Defining Data loader fixtures for each test scenario.
    @pytest.fixture(params = CheckOutData.test_CheckOut_data_A)
    def getData_test_A(self,request):
        return request.param

    @pytest.fixture(params = CheckOutData.test_CheckOut_data_B)
    def getData_test_B(self,request):
        return request.param

    #Verify that updating the Shipping Address in CheckOut is reflected immediately by the App.

    def test_updateAddress(self,getData_test_A):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        homePage.searchItem(getData_test_A['item'])

        self.verifyElementPresence(homePage.autoComplete)

        logger.info("Moving to Product Page")

        productPage = homePage.goToProductPage()

        productPage.clickAddToCartButton()

        self.verifyElementClickable(productPage.checkOutButton)

        summaryPage = productPage.goToCheckOut()

        logger.info("Moving to CheckOut Page")
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        logger.info("Signing in")

        addressPageSummary = authenticationPage.signIn(getData_test_A['mail'],getData_test_A['password'])

        logger.info("In Address Summary page.")

        updateAddressPage = addressPageSummary.goUpdateAddressPage()

        logger.info("Updating address.")

        newCity = getData_test_A['city']

        updateAddressPage.inputNewAddress(newCity,updateAddressPage.getCityInput())

        logger.info("Updated city to {}".format(newCity))

        addressText = addressPageSummary.getAddressText()

        assert newCity in addressText, logger.error("ADDRESS DID NOT GET UPDATED")

        logger.info("Test completed succesfully")

        addressPageSummary.signOut()

        addressPageSummary.goToHomePage()

    # Verify that the CheckOut functionality is working from Beginning to End.    
    def test_EndToEnd(self,getData_test_B):

        logger = self.getLogger()

        homePage = HomePage(self.driver)

        homePage.searchItem(getData_test_B['item'])

        self.verifyElementPresence(homePage.autoComplete)

        productPage = homePage.goToProductPage()

        logger.info("Moving to Product Page")

        productPage.clickAddToCartButton()

        self.verifyElementClickable(productPage.checkOutButton)

        summaryPage = productPage.goToCheckOut()

        logger.info("Moving to CheckOut Page")
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        logger.info("Signing in")

        addressPageSummary = authenticationPage.signIn(getData_test_B['mail'],getData_test_B['password'])

        shippingPage = addressPageSummary.goToShippingPage()

        logger.info("Moving to Shipping Page")

        shippingPage.checkTermsCheckBox()

        paymentPage = shippingPage.goToPaymentPage()

        logger.info("Moving to Payment Page")

        paymentPage.clickCheckPayment()

        orderConfirmationPage = paymentPage.goToOrderConfirmationPage()

        logger.info("Moving to order confirmation Page")

        self.verifyElementPresence(orderConfirmationPage.message)

        message = orderConfirmationPage.getMessageText()

        assert "Your order on My Store is complete." in message

        logger.info("Test completed succesfully")





