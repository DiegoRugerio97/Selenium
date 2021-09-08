from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe' , options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Going to shop page
driver.find_element_by_link_text("Shop").click()

#Adding an iphone X to the cart
#First locate the overall wrapping div, common parent of elements.

cards = driver.find_elements_by_xpath("//div[@class='card h-100']")
#Each element is //div[@class='card h-100']
for card in cards:
    # IMPORTANT ADVANCED XPATH
    # Omit // at start of the path to continue searching from current WebElement's XPath
    # If not omitted, search will begin from top.
    productName = card.find_element_by_xpath("div/h4/a").text #Note omitted // at start of xpath search
    if productName == 'iphone X':
        button = card.find_element_by_xpath("div/button")
        button.click()

checkOutButton = driver.find_element_by_partial_link_text("Checkout")
checkOutButton.click()

confirmPurchaseButton = driver.find_element_by_xpath("//button[@class='btn btn-success']")
confirmPurchaseButton.click()

countryInput = driver.find_element_by_xpath("//input[@id='country']")
countryInput.send_keys("Un")

#Wait for auto suggestion to show desired link
wait = WebDriverWait(driver,6)
#Wait until the link with the desired text is present
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"United Kingdom")))

#Then click the link once it is present
suggestion = driver.find_element_by_link_text("United Kingdom")
suggestion.click()

#Trying to click the input directly wont work, either use ...css_selector("[type='submit'") or JSE
#JSE
checkBox = driver.find_element_by_xpath("//input[@id='checkbox2']")
driver.execute_script("arguments[0].click();",checkBox)

purchaseButton = driver.find_element_by_xpath("//input[@value='Purchase']")
purchaseButton.click()

successMessage = driver.find_element_by_class_name("alert-success")
print(successMessage.text)

assert ('Success' in successMessage.text)

#Take a screenshot of the page
#driver.get_screenshot_as_file("screen.png")