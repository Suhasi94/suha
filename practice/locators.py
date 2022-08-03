import time
from selenium import webdriver

driver=webdriver.Chrome(r"/drivers/chromedriver.exe")

url="https://www.google.com/"
driver.get(url)

driver.maximize_window()
#by name
'''
element = driver.find_element("name", "q")
print(element)

element.send_keys("python")

element = driver.find_element_by_name("q")
print(element)

#by class name #error
element = driver.find_element_by_class_name("gLFyf gsfi")
print(element)


#tag name
element = driver.find_element_by_tag_name("input")
print(element)
'''


#link text locator
element = driver.find_element_by_link_text("Register")
element.click()
time.sleep(3)

#partial link text
driver.back()
time.sleep(3)

re_partial_link = driver.find_elements_by_partial_link_text("reg")
re_partial_link.click()

