from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestCheckOut(BaseClass):

    def test_updateAddress(self):
        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys("blouse")

        self.verifyElementPresenceByClass("ac_even")

        productPage = homePage.goToProductPage()

        productPage.getAddToCartButton().click()

        self.verifyElementClickableByXPATH("//a[@title='Proceed to checkout']")

        summaryPage = productPage.goToCheckOut()
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        addressPageSummary = authenticationPage.signInCheckOut("diego.rugerio@mail.com","XXXX#")

        updateAddressPage = addressPageSummary.goUpdateAddressPage()

        updateAddressPage.getCityInput().clear()

        newCity = "CityChangeTest4"

        updateAddressPage.getCityInput().send_keys(newCity)

        updateAddressPage.getSubmitButton().click()

        addressText = addressPageSummary.getAddressText()

        assert newCity in addressText

        homePage.signOut()

        homePage.goToHomePage()
    
    def test_EndToEnd(self):

        homePage = HomePage(self.driver)

        homePage.getSearchField().send_keys("blouse")

        self.verifyElementPresenceByClass("ac_even")

        productPage = homePage.goToProductPage()

        productPage.getAddToCartButton().click()

        self.verifyElementClickableByXPATH("//a[@title='Proceed to checkout']")

        summaryPage = productPage.goToCheckOut()
        
        authenticationPage = summaryPage.goToAuthenticationPage()

        addressPageSummary = authenticationPage.signInCheckOut("diego.rugerio@mail.com","XXXX#")

        shippingPage = addressPageSummary.goToShippingPage()

        shippingPage.getTermsCheckBox().click()

        paymentPage = shippingPage.goToPaymentPage()

        paymentPage.getCheckPaymentButton().click()

        orderConfirmationPage = paymentPage.goToOrderConfirmationPage()

        message = orderConfirmationPage.getMessageText()

        assert "Your order on My Store is complete." in message





