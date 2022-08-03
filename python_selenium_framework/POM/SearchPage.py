from POM import *
from Data import *


class SearchPage(SeleniumWrapper):
    SearchPage_objects = read_locators("SearchPage")

    def enter_search(self, gadget_name):
        locator = SearchPage.SearchPage_objects["txt_search"]
        self.enter_text(locator, value=gadget_name)

    def click_search_btn(self):
        locator = SearchPage.SearchPage_objects["btn_search"]
        self.click_element(locator)