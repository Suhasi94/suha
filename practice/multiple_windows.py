import time
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")

'''
url = "http://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)
#click on twitter link present on the footer of the webpage
driver.find_element_by_link_text("Twitter").click()

#"Twitter" page opens in a new tab in the browser
#In order to switch the tab, get window_handles
#window_handles returns a list of windows ID
handles = driver.window_handles
print(handles)

#switch to window handle of Twitter
driver.switch_to.window(handles[1])
#driver.find_element_by_xpath("//span[text()='Follow']").click()

#example
#driver.find_element_by_xpath('//input[@placeholder="Search Twitter"]').send_keys('hello')

#switch back to parent window
driver.switch_to.window(handles[0])

#click on register link present on demowebshop page
driver.find_element_by_xpath("//a[text()='Register']").click()
'''
################################ Java Script Pop up #################################
'''
url = "http://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)

element = driver.find_element_by_xpath("//input[@value='Search']").click()

alert_obj = driver.switch_to.alert
alert_obj.accept()
print(alert_obj.text)
alert_obj.dismiss()
'''

################################# file upload popup #############################

url = "file:///C:/Users/User/Desktop/selenium/html_files/demo.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath("//input[@type='file']").send_keys(r"C:\Users\User\Desktop\filehandling\files\access-log.txt")
