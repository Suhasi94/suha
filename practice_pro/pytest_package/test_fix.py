import pytest
from selenium import webdriver

def test_login(_driver):
    _driver.find_element_by_link_text("Log in").click()

def test_register(_driver):
    _driver.find_element_by_link_text("Register").click()



