import pytest

#Fixtures
#Fixtures initialize test functions. They provide a fixed baseline so that tests execute reliably and produce
#consistent, repeatable results.

#Set a fixture function with decorator @pytest.fixture()
#It is also possible to use a coroutine to execute code after the test case has been executed.
@pytest.fixture()
def setup():
    print("This method will be executed first")
    #Using yield keyword we pass control to the test case
    yield
    #Finishing the test case function, control will be returned
    print("This will be executed last")

#Then pass the fixture function to the test case functions as an argument
def test_fixtureDemo(setup):
    print("This method will be executed second")

#In case many test cases use the same fixture in a file
#We can wrap them in a class and use the usefixtures("fixtureName") mark 

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo2(self):
        print("This is fixture demo 2")

    def test_fixtureDemo3(self):
        print("This is fixture demo 3")

    def test_fixtureDemo4(self):
        print("This is fixture demo 4")

    def test_fixtureDemo5(self):
        print("This is fixture demo 5")

    def test_fixtureDemo6(self):
        print("This is fixture demo 6")

    

    
    