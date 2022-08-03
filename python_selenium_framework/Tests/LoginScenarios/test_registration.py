from Tests import *
from POM import *

headers = read_headers("Shopping", "test_registration")
data = read_data("Shopping", "test_registration")


@pytest.mark.parametrize(headers, data)
def test_registration(_driver, fname, lname, email, password):
    rp = RegistrationPage(_driver)
    rp.click_register()
    rp.select_male()
    rp.enter_firstname(fname)
    rp.enter_lastname(lname)
    rp.enter_email(email)
    rp.enter_password(password)
    rp.enter_confirm_password(password)
    rp.click_register_button()
    rp.verify_registration_successful()