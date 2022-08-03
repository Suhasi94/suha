import pytest
from selenium import webdriver

'''
@pytest.fixture()
def greet():
    print("----------hai--------------")

def test_span(greet):
    print("in test span")

def test_display(greet):
    print("in test display")

##by using autouse=True no need to pass fixture function to test function
# by default all the test function will execute
@pytest.fixture(autouse=True)
def greet():
    print("----------hai--------------")

def test_span():
    print("in test span")

def test_display():
    print("in test display")

#### sharing the fixture among the class
@pytest.fixture(autouse=True,scope="class")
def greet():
    print("--------- hai ----------------")
    yield
    print("---------- bye ---------------")

class TestSample:
    def test_span(self,greet):
        print("in test span")

def test_display():
    print("In test display")
'''

