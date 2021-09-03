from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

#Name locator in HTML ...name="name"
nameForm = driver.find_element_by_name("name")

#CSS Selector with syntax 
#tagname[attribute='value']
nameForm = driver.find_element_by_css_selector("input[name='name']")

#Simulate typing into a component
nameForm.send_keys("Diego Rugerio")

emailForm = driver.find_element_by_name("email")
emailForm.send_keys("diego.rugerio@email.com")

#Finding element by its HTML id ...id="id"
checkBox = driver.find_element_by_id("exampleCheck1")
#Simulate clicking
checkBox.click()

#XPath Selector with syntax
#//tagname=[@attribute='value']
submitButton = driver.find_element_by_xpath("//input[@value='Submit']")
submitButton.click()

successAlert = driver.find_element_by_class_name("alert-success")
print(successAlert.text)

driver.get("https://login.salesforce.com/")

# Special syntax for CSS selector with know ID
# tagname#id
userNameForm = driver.find_element_by_class_name("input#username")
userNameForm.send_keys("DiegoRugerio")

passwordForm = driver.find_element_by_class_name("input.password")
passwordForm.send_keys("password")

forgotPassLink = driver.find_element_by_link_text("¿Olvidó la contraseña?") 
forgotPassLink.click()

#XPath based on text
# //tagname[text()='text']

cancelButton = driver.find_element_by_xpath("//a[text()='¿Necesita ayuda para iniciar sesión?']")
cancelButton.click()

driver.get("https://login.salesforce.com/")

#Traversing tags with xpath
# //parentTag[@attribute='value']/childTag
# Useful when atrributes in childTag are not unique/static
# Also possible to traverse multiple tags
#//tag1[@attribute='value']/tag2[index_number]/tag3......

userLabel = driver.find_element_by_xpath("//div[@id='usernamegroup']/label")
print(userLabel.text)

#Traversing tags with CSS selector
#parentTag[attribute='value'] childTag:nth-child(index_number)
#Whitespace in between
# tag1[attribute='value'] tag2:nth-child(index_number) tag3:nth-child(index_number)...

passwordLabel = driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)")
print(passwordLabel.text)
