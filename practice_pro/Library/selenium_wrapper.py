from selenium import webdriver

#driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")

class SeleniumWrapper:

    def __init__(self,driver):
        self.driver=driver

    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()