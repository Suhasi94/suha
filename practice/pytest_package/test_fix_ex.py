import pytest
from selenium import webdriver

def test_login(fixture_):
    fixture_.find_element_by_link_text('Log in').click()

def test_Register(fixture_):
    fixture_.find_element_by_link_text('Register').click()
