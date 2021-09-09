
#If assert fails, the test case will fail and PyTest will print more details.

#To run select PyTest test files
# >py.test test_fileName.py -v
import pytest

#Use skip mark to skip a test
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi" , "Test failed because strings do not match"

#To run a test but not report its status
@pytest.mark.xfail
def test_SecondProgram():
    a = 4
    b = 6
    assert a+2 == 6 , "Addition don't match"

#To run select PyTest test cases, using a regex.
# Give the test cases, special names using a convention
#In this case, the word String, there is another test case with same String text in its name in
# text_demo.py file

#>py.test -k String -v

def test_PrintString():
    print("World!")


#Testing the fixture in the conftest.py file
def test_FixtureTest(setup):
    print("This will be executed in the middle")