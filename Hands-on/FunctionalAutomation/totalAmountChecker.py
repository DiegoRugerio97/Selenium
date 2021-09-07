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

time.sleep(4)

totalAmount = float(driver.find_element_by_css_selector("span.totAmt").text)
totalCalculated = 0

#Traversing the table
#Using p.amount would return double elements as price and total were styled with the same class
#Therefore we had to locate the total p tag traversing through the table.
#Starting with tr - table row, then locating last td - table data, which represented the total column.
#Finally locating the p tag inside this td to obtain the total text.
totalTable = driver.find_elements_by_xpath("//tr/td[5]/p")

for total in totalTable:
    totalCalculated += float(total.text)

assert(totalAmount == totalCalculated)