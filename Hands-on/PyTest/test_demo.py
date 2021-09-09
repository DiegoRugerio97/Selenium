
#Any PyTest file must start with 'test_' followed by name of file or end with '_test'

#PyTest requires test cases wrapped in a function.
#It also requires test function name to start with 'test_...'
#Function names must be unique inside its file, cannot be repeated.

#To tag test cases use @pytest.mark.<mark name> decorator

#Run marked test cases with
# >py.test -m <mark name>

import pytest
#groupName will be a custom mark
@pytest.mark.groupName
def test_firstProgram():
    print("Hello")

def test_secondProgram():
    print("World!")

@pytest.mark.groupName
def test_ShowString():
    print("World!")