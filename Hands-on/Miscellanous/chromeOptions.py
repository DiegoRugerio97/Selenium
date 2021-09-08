from selenium import webdriver
import time

#Provide options on how browser should be invoked, give behaviour to browser.
chrome_options = webdriver.ChromeOptions()
#Start maximized
chrome_options.add_argument("--start-maximized")
#Don't show the actual browser, run in the back.
chrome_options.add_argument("headless")
#Ignore certificate warnings
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='C:\Users\Diego\Downloads\Programas a Instalar\2021\Drivers\chromedriver_win32\chromedriver.exe',options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
