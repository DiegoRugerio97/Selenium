from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

#Implicit/Global wait
#Wait up to s seconds if object is not displayed. Selenium will keep monitoring the page.
# s - Max timeout. If component loads before s seconds have passed, Selenium will resume script.
driver.implicitly_wait(5)

driver.maximize_window()    
searchBar = driver.find_element_by_css_selector("input[type='search']")
searchBar.send_keys("ber")

#Apply wait directly from Python package, not recommended. 
#time.sleep(2)

products = driver.find_elements_by_xpath("//div[@class='products']/div")
numberOfProducts = len(products)
assert numberOfProducts == 3

addButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(addButtons))

for button in addButtons:
    button.click()


#time.sleep(2)

shoppingCart = driver.find_element_by_xpath("//img[@alt='Cart']")
shoppingCart.click()

checkoutButton = driver.find_element_by_xpath("//div[@class='action-block']/button")
checkoutButton.click()

promoCodeInput = driver.find_element_by_xpath("//input[@class='promoCode']")
promoCodeInput.send_keys("rahulshettyacademy")

applyButton = driver.find_element_by_xpath("//button[@class='promoBtn']")
applyButton.click()

messageSpan = driver.find_element_by_xpath("//span[@class='promoInfo']")

message = messageSpan.text

print(message)