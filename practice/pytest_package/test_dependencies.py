import pytest
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")
driver.get('https://demo.actitime.com/login.do')
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.mark.dependency()
def test_login():
    driver.find_element_by_name("username1").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_xpath('//div[text()="Login "]').click()

@pytest.mark.dependency(depends=["test_login"])
def test_logout():
    driver.find_element_by_id("logoutLink").click()
