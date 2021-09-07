from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(5)
driver.maximize_window()

itemsToCheck = []
allItemsAdded = True

searchBar = driver.find_element_by_css_selector("input.search-keyword")
searchBar.send_keys("ca")

time.sleep(5)

productNames = driver.find_elements_by_css_selector("h4.product-name")
for name in productNames:
    #print(name.text)
    itemsToCheck.append(name.text)

addButtons = driver.find_elements_by_css_selector("div[class='product-action'] button")
for button in addButtons:
    button.click()

cart = driver.find_element_by_css_selector("img[alt='Cart']")
cart.click()

checkoutButton = driver.find_element_by_css_selector("div[class='action-block'] button")
checkoutButton.click()

time.sleep(4)

itemsInTable = driver.find_elements_by_css_selector("p[class='product-name']")
print("In Table:")
print(len(itemsInTable))
for item in itemsInTable:
    print(item.text)
    if item.text not in itemsToCheck:
        allItemsAdded = False
    

assert allItemsAdded