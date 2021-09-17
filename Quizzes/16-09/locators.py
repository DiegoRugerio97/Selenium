#Initial setup
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe', options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#1 -  What are the different type element locators in Selenium?
# There are several ways of locating a Web Element in Selenium, which one is the most appropiate its going to 
# depend on the attributes available, as well as the use case.

#.find_element_by_id(...)
#Allows to find a web element by its unique HTML id attribute.
textField = driver.find_element_by_id("autocomplete")
textField.send_keys("This is textField")

#.find_element_by_name(...)
#Allows to find a web element by its name HTML attribute.
nameField = driver.find_element_by_name("enter-name")
nameField.send_keys("This is nameField")

#.find_element_by_xpath(...)
#Allows to find a web element by an xpath expression, querying the HTML document and locating nodes.
#Using XPath its possible to traverse through elements and locate them using different attributes like id, name
#class, type,...
textField = driver.find_element_by_xpath("//input[@id='autocomplete']")
#Using XPath we could also find this element with, both options work.
textField = driver.find_element_by_xpath("//input[@class='inputs ui-autocomplete-input']")
textField.clear()
textField.send_keys("Using XPath")

#.find_element_by_link_text(...)
#Allows to find a web element by the text in an <a> tag.
homeLink = driver.find_element_by_link_text("Home")

#.find_element_by_link_text(...)
#Allows to find a web element by partial text in an <a> tag.
homeLink = driver.find_element_by_partial_link_text("Ho")

#.find_element_by_tag_name(...)
#Allows to find a web element by its HTML tag.
header = driver.find_element_by_tag_name("h1")
print(header.text)

#.find_element_by_class_name(...)
#Allows to find a web element by its class attribute. Only one class.
tabButton = driver.find_element_by_class_name("class2")

#.find_element_by_css_selector(...)
#Allows to find a web element using css selector syntax, used in css to locate and style HTML elements.
#Very similar to XPath but with certain limitations.
textField = driver.find_element_by_css_selector("input[id='autocomplete']")
textField.clear()
textField.send_keys("Using CSS Selector")

#2 -  What is the difference between find_element and find_elements?
# find_element will return the very first Web Element that matches with the locator, find_elements will return a list
# containing all of the matching elements, allowing us to loop through them.

#First matching element
checkBoxInput = driver.find_element_by_xpath("//input[@type='checkbox']")
checkBoxInput.click()

#All elements
checkBoxInputs = driver.find_elements_by_xpath("//input[@type ='checkbox']")
print(len(checkBoxInputs))

for input in checkBoxInputs:
    input.click()

#3 - Difference between absolute and relative XPath
#Absolute xpath will begin the expression at the very start of the HTML document the root element (<html>), 
# meanwhile relative will start with a reference to the element you want to start from

#Locating the textField Element using relative XPath
textField = driver.find_element_by_xpath("//input[@id='autocomplete']")
textField.clear()
textField.send_keys("Using Relative XPath")

time.sleep(2)

#Locating the textField Element using absolute XPath
textField = driver.find_element_by_xpath("/html/body/div/div[@id='select-class-example']/fieldset/input")
textField.clear()
textField.send_keys("Using Absolute XPath")

#The problem with absolute XPath is that any change in the structure of the HTML document will render the locator
#useless, therefore its always better to use relative XPath. 

# 4-  What is XPath-axes tag with example.
#An axis represents a relationship to the context (current) node, and is used to locate nodes 
#relative to that node on the tree, this is one of the ways we can traverse through elements
#using XPath.

#Moving through the textField WebElement to the second of the radio buttons.
#Using the parent axis we can go up one level to the parent element specified in the xpath.
#In this case we first locate the textField element, then using the parent:: axis we go 3 levels up, to the
# parent div of the radio buttons div, then we go down towards the radio buttons. 
radioButton2 = driver.find_element_by_xpath("//input[@id='autocomplete']/parent::fieldset/parent::div/parent::div/div[@id='radio-btn-example']/fieldset/label[@for='radio2']/input")
radioButton2.click()

#parent:: is one of the several axis that are available, others are:
#ancestor:: , child:: , following:: , parent:: , ancestor:: ...

