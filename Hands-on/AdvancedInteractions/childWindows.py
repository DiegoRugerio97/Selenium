from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

openWindow = driver.find_element_by_link_text("Click Here")
openWindow.click()

#.window_handles is a list with all the windows IDs opened by Selenium
#[0] is the parent window, the first opened by Selenium.
#Then the rest of indexes are other windows opened.
childWindow = driver.window_handles[1]

driver.switch_to.window(childWindow)
text = driver.find_element_by_tag_name("h3").text
print(text)
driver.close()

driver.switch_to.window(driver.window_handles[0])
text = driver.find_element_by_tag_name("h3").text
print(text)
