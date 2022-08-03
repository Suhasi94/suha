from POM.login_page import *

class TestLogin:

    def test_login(self,_driver):
        lp = LoginPage(_driver)
        lp.enter_username()
        lp.enter_password()
        lp.click_login()

