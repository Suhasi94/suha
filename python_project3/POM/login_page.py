from library.selenium_wrapper import *
from Data.ExcelLib import *

read_object = read_locators()

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.sw = SeleniumWrapper(driver)

    def enter_username(self):
        self.sw.enter_text(read_object['txt_username'], 'admin')

    def enter_password(self):
        self.sw.enter_text(read_object['txt_password'], 'manager')

    def click_login(self):
        self.sw.click_login(read_object['btn_login'])
