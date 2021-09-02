from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Diego\\Downloads\\Programas a Instalar\\2021\\Drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://www.google.com.mx/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.get("https://www.youtube.com/")
driver.back()
driver.close()