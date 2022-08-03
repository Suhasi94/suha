from time import sleep
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
url = "file:///C:/Users/User/Desktop/selenium/html_files/iframe.html"
driver.get(url)
driver.maximize_window()


driver.switch_to.frame("FR1")
driver.find_element_by_xpath('//input[@name="q"]').send_keys("mobiles")
sleep(3)
#driver.switch_to.default_content()
#driver.find_element_by_xpath('//a[text()="Google"]').click()
driver.switch_to.default_content()
sleep(3)
driver.switch_to.frame("FR2")
driver.find_element_by_xpath('//input[@name="Search Support"]').send_keys('Automobiles')