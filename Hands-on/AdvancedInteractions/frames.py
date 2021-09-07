from selenium import webdriver
import time

#Tags for declaring frames
#iframe, frameset, frame
#This means there is a frame in page. HTML driver cannot find it. 

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

#Switch to frame using id/name/or index (0 being the first frame in the web app).
driver.switch_to.frame("mce_0_ifr")

frameBody = driver.find_element_by_css_selector("body#tinymce")
frameBody.clear()
frameBody.send_keys("This is automated text!")

#To return to HTML page/Default content from the frame context.
driver.switch_to.default_content()
