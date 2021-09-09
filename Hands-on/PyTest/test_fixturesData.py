import pytest
#Importing the utility logger class to send messages to logs
from LogClass import LogClass

@pytest.mark.usefixtures("dataLoader")
#Inherit the utility class
class TestExample2(LogClass):
    #Even if the fixture is declared at the class level, because it is returning information, it must be passed
    #on to the test functions
    def test_editProfile(self,dataLoader):
        #Call the getLogger method
        logger = self.getLogger()
        #Normal Print
        #print("Printing data information")
        #print(dataLoader)
        #Using logs
        #Send the information to logs
        logger.info("Printing data information: {}".format(dataLoader))

@pytest.mark.usefixtures("crossBrowser")
class TestExample3(LogClass):
    #In parametrized fixture (see conftest.py) PyTest will iterate through all the parameters in different
    #test runs. Returning a different data set each time. 
    def test_crossBrowser(self,crossBrowser):
        logger = self.getLogger()
        #Normal Print
        #print("Performing test with: ")
        #print(crossBrowser[0])
        #print("With Data: ")
        #print(crossBrowser[1])
        #Using logs
        logger.info("Performing test with: {}".format(crossBrowser[0]))
        logger.info("With Data: {}".format(crossBrowser[1]))
