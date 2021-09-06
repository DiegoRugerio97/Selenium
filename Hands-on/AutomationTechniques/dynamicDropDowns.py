from selenium import webdriver
import time

#Initial Setup
driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

countrySearch = driver.find_element_by_id("autosuggest")
countrySearch.send_keys("me")
#Website has a slight delay between inputing characters and the showing of the autosuggest list.
#Apply delay to compensate for that delay
time.sleep(2)

#Reach a common locator for the options in the dynamic dropdown.
#<li class="ui-menu item..."
#   <a....> DESIRED TEXT ....
#.find_elements_by... returns a list of webElements
countryOptions = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print("Number of options: ")
print(len(countryOptions))
#Iterating through countryOptions list.
for opt in countryOptions:
    print(opt.text)
    #.text returns a string with the text between tags
    #Searching for Mexico option and clicking it.
    if opt.text == "Mexico":
        opt.click()
        break

#.text might not be reflected immediately after clicking the option.
# Therefore it is recomenden to use .get_attribute('value') as an alternative, this method reflects the changes.
assert("Mexico" == countrySearch.get_attribute('value'))