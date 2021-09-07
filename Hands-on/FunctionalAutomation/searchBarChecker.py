from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()

searchBar = driver.find_element_by_css_selector("input.search-keyword")
searchBar.send_keys("me") #Search for Melon, Pomegranate and Water Melon

namesToCheck = ['Musk Melon - 1 Kg', 'Pomegranate - 1 Kg', 'Water Melon - 1 Kg']
displayedNames = []


time.sleep(3)

productNames = driver.find_elements_by_css_selector("h4.product-name")
for name in productNames:
    displayedNames.append(name.text)

print(namesToCheck)
print(displayedNames)

assert namesToCheck == displayedNames