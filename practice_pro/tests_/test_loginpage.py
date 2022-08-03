from POM.login_page import LoginPage
#from selenium import webdriver


#driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
#driver.get("https://demo.actitime.com/login.do")
#driver.maximize_window()

class TestloginPage:

    def test_login(self,_driver):
        lp = LoginPage(_driver)
        lp.enter_username()
        lp.enter_pwd()
        lp.click_login()