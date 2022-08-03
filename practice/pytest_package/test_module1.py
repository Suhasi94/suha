'''
class TestClassName:
    pass
'''


################ 1st way of executing the fixture #################
"""
@pytest.fixture()
def greet():
    print("-----------hai----------")

def test_span(greet):
    print("in test span")

def test_display(greet):
    print("displaying the message")
"""
import  pytest

'''
@pytest.fixture(autouse=True)
def greet():
    print("-----------hai----------")
    yield
    print("-----------bye-----------")

class TestSample:
    def test_span(self):
        print("in test span")

def test_display():
    print("displaying the message")
'''
@pytest.fixture(scope="class")
def greet():
    print("-----------hai----------")
    yield
    print("-----------bye-----------")

class TestSample:
    def test_span(self,greet):
        print("in test span")

def test_display():
    print("displaying the message")