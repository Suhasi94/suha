import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")

'''
url = "file:///C:/Users/User/Desktop/selenium/html_files/loading.html"
driver.get(url)
driver.maximize_window()
start = time.time()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//input[@name="fname"]').send_keys("pooja")
end = time.time()
print(end - start)
'''

'''
#implicitly_wait

f_path = 'file:///C:/Users/User/Desktop/selenium/html_files/progressbar.html'
driver.get(f_path)
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath('//button[text()="Click Me"]').click()
driver.find_element_by_xpath('//div[text()="100%"]')
driver.find_element_by_xpath('//button[text()="Click Me"]').click()
'''

#explicit_wait
#import webDriverWait
#import expected_conditions
'''
f_path = 'file:///C:/Users/User/Desktop/selenium/html_files/progressbar.html'
driver.get(f_path)
driver.maximize_window()

driver.find_element_by_xpath('//button[text()="Click Me"]').click()

wait_ = WebDriverWait(driver, 30)
wait_.until(ec.presence_of_element_located(("xpath", '//div[text()="100%"]')))

driver.find_element_by_xpath('//button[text()="Click Me"]').click()
'''

#function to check both enability and disability

driver.get(r"file:///C:/Users/User/Desktop/selenium/html_files/demo.html")
element = driver.find_element_by_xpath('//input[@id="first_name"]')
print(element.is_enabled())
print(element.is_displayed())
#element.send_keys("hello world")



