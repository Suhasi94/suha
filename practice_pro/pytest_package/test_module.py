import pytest

'''
@pytest.fixture()
def greet():
    return "hello world"

def test_spam(greet):
    print("in test spam")

def test_display(greet):
    print("display a message")
'''

@pytest.fixture(scope="class")
def greet():
    print("--------- hai -------------")#set up
    yield
    print("----------bye--------------")#tear down

class TestSample:

    def test_spam(self,greet):
        print("in test spam")

def test_display():
    print("in test display")