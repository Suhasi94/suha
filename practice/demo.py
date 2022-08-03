import time
from selenium import webdriver


driver=webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")

#launh the url by using get method
url="https://www.google.com/"
driver.get(url)

#maximize the window browser maximize_window
driver.maximize_window()
time.sleep(3)

#driver.minimize_window()

#to get the url
c_url=driver.current_url
print(c_url)

#to get the title of the browser
print(driver.title)

#to close the current window
#driver.close()

#quit()-used to close all the browser instances launched by the current webdriver
#driver.quit()