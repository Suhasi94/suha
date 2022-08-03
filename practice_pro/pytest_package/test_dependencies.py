import pytest
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
url = "https://demo.actitime.com/login.do"
driver.get(url)
driver.maximize_window()
#driver.implicitly_wait(30)

@pytest.mark.dependency()
def test_login():
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("admin")
    driver.find_element_by_xpath('//input[@name="pwd"]').send_keys("manager")
    driver.find_element_by_xpath('//div[text()="Login "]').click()

@pytest.mark.dependency(depends=["test_login"])
def test_logout():
    driver.find_element("id", "logoutLink").click()
