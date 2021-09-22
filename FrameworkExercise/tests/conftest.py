import pytest
from selenium import webdriver

#This file defines some pytest properties. 
#Adding the option of specifying the browser to be used as a CLI command.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser options: chrome/firefox"
    )

#Defining the fixture that will be used for all of the test cases scripts.
#This fixture instances a Chrome/Firefox driver and uses it to load the My Store app.
#This will be the first step in all of the test cases, therefore it is a good practice to define these steps
# as a fixture in this file.
@pytest.fixture(scope="class")
def browserSetup(request):

    browser = request.config.getoption("--browser_name")

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe' , options=chrome_options)
    
    #SPECIFICATIONS FOR OTHER BROWSERS, OPTIONS AND DRIVERS
    #elif browser == "firefox":
        #driver = webdriver.Firefox(executable_path='<Path to geckodriver.exe>')
    
    driver.get("http://automationpractice.com/index.php")

    #STANDARD/BEST PRACTICE
    #Use this method to assign the local WebDriver instance to the class driver.
    #By applying scope="class" and using the .useFixture decorator on test case class,
    #the latter will have access to class attributes, including the WebDriver instance.
    request.cls.driver = driver
    #STANDARD/BEST PRACTICE
    #Use yield keyword to give control to the test case code, then when it ends, continue the fixture
    #code, in this case, closing the browser.
    yield
    driver.delete_all_cookies()
    driver.close()