from POM import *
from Data import *
import pytest
from POM import *

# data = read_data_as_list("UserData")
# headers = read_headers("UserData")


# @pytest.mark.parametrize(headers, data)
def test_login(_driver, email, password):
    lp = LoginPage(_driver)
    lp.click_login_link()
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login_button()