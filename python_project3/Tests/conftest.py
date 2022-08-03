from selenium import  webdriver
import pytest

@pytest.fixture()
def _driver():
    driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\python_project3\driver\chromedriver.exe')
    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    yield driver
    driver.quit()