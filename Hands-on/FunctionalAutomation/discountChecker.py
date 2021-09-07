from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.maximize_window()

searchBar = driver.find_element_by_css_selector("input.search-keyword")
searchBar.send_keys("ca")

time.sleep(3)

addButtons = driver.find_elements_by_css_selector("div[class='product-action'] button")
for button in addButtons:
    button.click()

cart = driver.find_element_by_css_selector("img[alt='Cart']")
cart.click()

checkoutButton = driver.find_element_by_css_selector("div[class='action-block'] button")
checkoutButton.click()

wait = WebDriverWait(driver,7)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.promoCode")))

promoCodeInput = driver.find_element_by_xpath("//input[@class='promoCode']")
promoCodeInput.send_keys("rahulshettyacademy")

applyButton = driver.find_element_by_xpath("//button[@class='promoBtn']")
applyButton.click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))

totalAmount = driver.find_element_by_css_selector("span.totAmt").text
discountedAmount = float(totalAmount)-(float(totalAmount)*.10)

totalAfterDiscount = float(driver.find_element_by_css_selector("span.discountAmt").text)

print(discountedAmount)
print(totalAfterDiscount)

assert(discountedAmount == totalAfterDiscount)