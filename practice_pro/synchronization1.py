from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
url = 'file:///C:/Users/User/Desktop/selenium/html_files/loading.html'
driver.get(url)

class _visibility_of_element_located(visibility_of_element_located):

    def __call__(self, driver):

        displayed = super().__call__(driver)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()

        else:
            return False

wait = WebDriverWait(driver, 30)

print(wait.until(_visibility_of_element_located(("name","fname"))))
driver.find_element_by_name("fname").send_keys("hello world")