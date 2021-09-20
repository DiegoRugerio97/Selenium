import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser options: chrome/ie/firefox"
    )

@pytest.fixture(scope="class")
def browserSetup(request):

    browser = request.config.getoption("--browser_name")

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe' , options=chrome_options)
    
    #SPECIFICATIONS FOR OTHER BROWSERS, OPTIONS AND DRIVERS
    
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
    driver.close()