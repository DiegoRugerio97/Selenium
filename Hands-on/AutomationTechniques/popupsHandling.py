from selenium import webdriver

validateText = "Message"
driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

inputBox = driver.find_element_by_name("enter-name")
inputBox.send_keys("Message")

alertButton = driver.find_element_by_id("alertbtn")
alertButton.click()

#Use this class to interact with alert prompts. 
#It contains methods for dismissing, accepting, inputting, and getting text from alert prompts.
# .switch_to.<> will switch driver context to <>, in this case, to alert/popups
alert = driver.switch_to.alert

print(alert.text)
alertText = alert.text
assert (validateText in alertText)
#To select 'positive' option in alert
alert.accept()
#alert.dismiss() to close popup/ accept 'negative' option

