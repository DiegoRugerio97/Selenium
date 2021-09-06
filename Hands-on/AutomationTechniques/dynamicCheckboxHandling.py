from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Finding all the checkboxes, common attribute is type = 'checkbox'
#Using find_elements_by... method to get a list of all the webElements matching the CSS selector
checkBoxes = driver.find_elements_by_css_selector("input[type='checkbox']")

#Looping through list of the checkboxes web elements and clicking each one of them.
for box in checkBoxes:
    box.click()
    #For assertion purposes we can check if a webElement is selected, in this case, the check boxes.
    assert box.is_selected()

for box in checkBoxes:
    box.click()

for box in checkBoxes:
    #Extract attributes of tags with .get_attribute method. 
    if box.get_attribute('value') == "option2":
        box.click()

#Radio Inputs are handled in a similar way
radioInputs = driver.find_elements_by_xpath("//input[@type='radio']")
print(len(radioInputs))
radioInputs[1].click()