from selenium import webdriver
#Needed for Explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.maximize_window()    
searchBar = driver.find_element_by_css_selector("input[type='search']")
searchBar.send_keys("ber")

time.sleep(2)

products = driver.find_elements_by_xpath("//div[@class='products']/div")
numberOfProducts = len(products)
assert numberOfProducts == 3

addButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(addButtons))

for button in addButtons:
    button.click()

#Apply wait directly from Python package, not recommended. 
time.sleep(2)

shoppingCart = driver.find_element_by_xpath("//img[@alt='Cart']")
shoppingCart.click()

checkoutButton = driver.find_element_by_xpath("//div[@class='action-block']/button")
checkoutButton.click()

#Explicit Wait
#Set wait time for specific element/step in the script.

#Must have a WebDriverWait instance
wait = WebDriverWait(driver,6)

#Explicitly telling Selenium to wait until the element with locator input.promoCode is present in the page.
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.promoCode")))

promoCodeInput = driver.find_element_by_xpath("//input[@class='promoCode']")
promoCodeInput.send_keys("rahulshettyacademy")

applyButton = driver.find_element_by_xpath("//button[@class='promoBtn']")
applyButton.click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
messageSpan = driver.find_element_by_xpath("//span[@class='promoInfo']")
message = messageSpan.text
print(message)