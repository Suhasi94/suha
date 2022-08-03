from selenium import webdriver
from data import read_objects
from Library.selenium_wrapper import SeleniumWrapper


#driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
#driver.get("https://demo.actitime.com/login.do")
#driver.maximize_window()

login_objects = read_objects.read_locators()
#sel_wrapper = SeleniumWrapper(driver)

'''
def enter_username():
    driver.find_element(*login_objects["txt_username"]).send_keys("admin")

def enter_pwd():
    driver.find_element(*login_objects["txt_password"]).send_keys("manager")

def click_login():
    driver.find_element(*login_objects["btn_login"]).click()
    
'''

'''
class LoginPage:

    def enter_username(self):
        driver.find_element(*login_objects["txt_username"]).send_keys("admin")

    def enter_pwd(self):
        driver.find_element(*login_objects["txt_password"]).send_keys("manager")

    def click_login(self):
        driver.find_element(*login_objects["btn_login"]).click()

lp = LoginPage()
lp.enter_username()
lp.enter_pwd()
lp.click_login()



class LoginPage:

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self):
        sel_wrapper.enter_text(login_objects["txt_username"], "admin")

    def enter_pwd(self):
        sel_wrapper.enter_text(login_objects["txt_password"], "manager")

    def click_login(self):
        sel_wrapper.click_element(login_objects["btn_login"])
'''

#lp = LoginPage()
#lp.enter_username()
#lp.enter_pwd()
#lp.click_login()

#connecting pom and test scripts
class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.sel_wrapper = SeleniumWrapper(driver)

    def enter_username(self):
        self.sel_wrapper.enter_text(login_objects["txt_username"], "admin")

    def enter_pwd(self):
        self.sel_wrapper.enter_text(login_objects["txt_password"], "manager")

    def click_login(self):
        self.sel_wrapper.click_element(login_objects["btn_login"])

