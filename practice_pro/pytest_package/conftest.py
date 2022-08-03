### it is an special file which is used to import the fixture
# among the modules/test cases

import pytest
from selenium import webdriver

@pytest.fixture()
def _driver():
    driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
    url = "http://demowebshop.tricentis.com/"
    driver.get(url)
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.quit()