import pytest
from selenium import webdriver

#PyTest command line arguments
#Enabling browser selection at run time from the CLI.
#>py.test ... --browser_name chrome/ie/firefox
#Initializing a run time variable
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser options: chrome/ie/firefox"
    )

@pytest.fixture(scope="class")
def browserSetup(request):
    #Moved all the initial browser setup to a fixture
    #Applied scope to class so fixture will only run once.

    #Retrieve the value of the run time variable
    browser = request.config.getoption("--browser_name")

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe' , options=chrome_options)
    
    #SPECIFICATIONS FOR OTHER BROWSERS, OPTIONS AND DRIVERS
    
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    #STANDARD/BEST PRACTICE
    #Use this method to assign the local WebDriver instance to the class driver.
    #By applying scope="class" and using the .useFixture decorator on test case class,
    #the latter will have access to class attributes, including the WebDriver instance.
    request.cls.driver = driver
    #STANDARD/BEST PRACTICE
    #Use yield keyword to give control to the test case code, then when it ends, continue the fixture
    #code, in this case, closing the browser.
    yield
    driver.close()