from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#In this case, nameInput.text won't be able to return the text.
# .text will only work for text that loads with the browser, use .get_attribute method that was 'inherited' from
# js DOM.
nameInput = driver.find_element_by_name("name")
nameInput.send_keys("This is text")
print(nameInput.get_attribute("value"))
#Or use JSE

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

#Let's suppose we can't click on a link directly with Selenium, that is when we use JSE.
shopButton = driver.find_element_by_css_selector("a[href='shop']")
driver.execute_script("arguments[0].click();",shopButton)

#Selenium can't scroll down, but js can.
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

