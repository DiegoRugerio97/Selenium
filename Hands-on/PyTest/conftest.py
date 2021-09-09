#Test configuration file.
#This file will be exposed to all test files present in the directory.
#Used to share fixtures across all test files
import pytest

#To run fixture just once before executing all test cases
#@pytest.fixture(scope="class")
#Applying the fixture at the class level, running the fixture just once at beginning and at the end.
@pytest.fixture()
def setup():
    print("This method will be executed first")
    #Using yield keyword we pass control to the test case
    yield
    #Finishing the test case function, control will be returned
    print("This will be executed last")


#Loading data to test cases using fixtures
@pytest.fixture()
def dataLoader():
    print("Data created")
    #Must return the data to be used by test case function t
    return ["First name", "Last name", "email@email.com"]


#Parametrized fixtures
#On first run it will use first param, then second,then third,...
#Can send nested lists, tuples list, etc...
@pytest.fixture(params=[['Chrome','Data A'], ['Firefox', 'Data B'], ['IE','Data C']])
#Must pass on request as an argument to access the parameters, only when using parametrized fixtures
def crossBrowser(request):
    return request.param
