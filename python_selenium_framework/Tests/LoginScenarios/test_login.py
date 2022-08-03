from Tests import *
from POM import *

headers = read_headers("Shopping", "test_login")
data = read_data("Shopping", "test_login")

@pytest.mark.parametrize(headers, data)
def test_login(_driver, email, password):
    lp = LoginPage(_driver)

    # Click on Login Link
    lp.click_login_link()

    # Enter Username and Password
    lp.enter_email(email)
    lp.enter_password(password)

    # Click on Login
    lp.click_login_button()

    # Verify User login
    lp.verify_user_login(email)