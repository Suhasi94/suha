import time

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")

url="https://www.google.com/"
driver.get(url)
driver.maximize_window()


print(driver.current_url)
print(driver.title)
time.sleep(5)
driver.close()
#driver.quit()
'''
7+1=8
* -
3*3 =9
= =
21 5
'''