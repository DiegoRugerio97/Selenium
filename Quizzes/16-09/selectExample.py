#Initial setup
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe', options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# 5 - How to select from dropdown using Selenium
#To select from an static dropdown, one where the options are not dynamic, we need to use the Select class from the 
#selenium support package.

#First locate the dropdown web element
dropDown = driver.find_element_by_xpath("//select[@id='dropdown-class-example']")

#Then initialize a Select instance, and pass the webElement as an argument.
selector = Select(dropDown)

#Can select and deselect by value, index (starting from 1) and visible text.
selector.select_by_visible_text("Option1")
time.sleep(2)

selector.select_by_value("option2")
time.sleep(2)

selector.select_by_index(3)
time.sleep(2)

#For deselect, its only possible when the select element supports multiple selections. 
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

multiDropDown = driver.find_element_by_xpath("//select[@id='second']")

selector = Select(multiDropDown)

selector.select_by_value("pizza")
selector.select_by_value("burger")
time.sleep(2)
selector.deselect_all()