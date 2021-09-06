from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

#Needed to submit password
nameForm = driver.find_element_by_name("name")
nameForm.send_keys("Diego Rugerio")
emailForm = driver.find_element_by_name("email")
emailForm.send_keys("diego.rugerio@email.com")


#Locate the dropdown element
genderDropDown = driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']")

#Using Select support class from Selenium, we can pass the webElement
selector = Select(genderDropDown)

#Can select and deselect by value, index (starting from 0) and visible text.
selector.select_by_visible_text("Female")


submitButton = driver.find_element_by_xpath("//input[@value='Submit']")
submitButton.click()

successAlert = driver.find_element_by_class_name("alert-success")
message = successAlert.text

#Assert if test case failed or was successful
assert("Success" in message)