import pytest
from selenium import webdriver

@pytest.fixture()
def fixture_():
    driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe')
    driver.get("http://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.quit()