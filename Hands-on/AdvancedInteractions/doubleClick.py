from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()

button = driver.find_element_by_css_selector("input#double-click")

actions = ActionChains(driver)

actions.move_to_element(button).double_click().perform()
#To perform a right-click
#.context_click(WebElement)


alert = driver.switch_to.alert

print(alert.text)
alert.accept()