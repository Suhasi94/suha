import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
url = 'file:///C:/Users/User/Desktop/selenium/html_files/loading.html'
driver.get(url)
driver.maximize_window()
# 1)explicit wait
# 2)implicit wait
'''
url = "file:///C:/Users/User/Desktop/selenium/html_files/loading.html"
driver.get(url)
driver.maximize_window()
start = time.time()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//input[@name="fname"]').send_keys("pooja")
end = time.time()
print(end - start)
'''

'''
#create an object instance to webdriverwait class
wait = WebDriverWait(driver, 50)
## wait for visibility of "FirstName" Textbox in loading html page
wait.until(expected_conditions.visibility_of_element_located(("name","fname")))
#enter "hello world" in firstname textbox
path = '//input[@name="fname"]'
driver.find_element_by_xpath(path).send_keys("hello world")

#wait for the progress bar to complete 100% in html page
url = 'file:///C:/Users/User/Desktop/selenium/html_files/progressbar.html'
driver.get(url)
driver.maximize_window()
path = '//button[text()="Click Me"]'
driver.find_element_by_xpath(path).click()

wait = WebDriverWait(driver, 30)
#wait until the progress bar is loaded completely(100%) and visible on
#the web page
wait.until(expected_conditions.visibility_of_element_located(("xpath",'//div[text()="100%"]')))
print("done")
'''

##function to check both enability and disability
## _visibility_of_element_located (customized class, overriding __call__
# method of parent class in child class)

driver.get(r"file:///C:/Users/User/Desktop/selenium/html_files/demo.html")
element = driver.find_element_by_xpath('//input[@id="first_name"]')
print(element.is_enabled())
print(element.is_displayed())