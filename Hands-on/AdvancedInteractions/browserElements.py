from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Hovering mouse over an web element
#Must import ActionChains
action = ActionChains(driver)

button = driver.find_element_by_css_selector("button#mousehover")


#ActionChains instance let us chain simple actions to achieve more complex ones like
#Hovering, Double click, right click, drag and drop...
#After establishing the set of instructions perform() method must be called to perform these instructions. 
action.move_to_element(button).perform()

topLink = driver.find_element_by_link_text("Reload")
action.move_to_element(topLink).click().perform()

hiddenInput = driver.find_element_by_css_selector("input#displayed-text")

assert hiddenInput.is_displayed()

toggleButton = driver.find_element_by_css_selector("input#hide-textbox")
toggleButton.click()

assert not hiddenInput.is_displayed()