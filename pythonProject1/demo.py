from selenium import webdriver

#open the browser
#launch the Google.com
#to launch the any web page we want url of the page
#maximize the browser window
#minimize the window
import time

c_driver=webdriver.Chrome(r"C:\Users\User\PycharmProjects\pythonProject1\drivers\chromedriver.exe")

url="https://www.google.com/"

#to launch the url
c_driver.get(url)

#To maximize the window
c_driver.maximize_window()

time.sleep(4)
#to minimize the window
#c_driver.minimize_window()

#to refresh
c_driver.refresh()

#to get the url
print(c_driver.current_url)

#to close()

c_driver.close()

c_driver.quit()