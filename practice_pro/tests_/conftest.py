from selenium import webdriver
import pytest


#@pytest.fixture()
#def _driver():
    #driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
'''    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    yield driver
    driver.quit()
'''


### For cross browser testing we have to make use of params keyword in fixture

@pytest.fixture(params=["Chrome", "Firefox"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")

    elif request.param == "Firefox":
        driver = webdriver.Firefox(executable_path=r"C:\Users\User\PycharmProjects\practice_pro\drivers\geckodriver.exe")

    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    yield driver
    driver.quit()
