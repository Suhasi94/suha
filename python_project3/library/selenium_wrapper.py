class SeleniumWrapper():

    def __init__(self,driver):
        self.driver = driver

    def enter_text(self,locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def click_login(self,locator):
        self.driver.find_element(*locator).click()

#sw = SeleniumWrapper()

#sw.enter_text(read_object['txt_username'],'admin')
#sw.enter_text(read_object['txt_password'],'manager')
#sw.click_login(read_object['btn_login'])
