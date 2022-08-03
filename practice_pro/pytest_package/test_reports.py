import pytest

@pytest.fixture(scope="class",autouse=True)
def greet():
    print("--------- hai -------------")#set up
    yield
    print("----------bye--------------")#tear down

class TestSample:

    def test_spam(self,greet):
        print("in test spam")

def test_display():
    print("in test display")