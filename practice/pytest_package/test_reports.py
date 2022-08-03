import  pytest

#pip install pytest-html
#command to run pytest modulename.py -vs --html="reportname.html"

@pytest.fixture(scope="class" , autouse=True)
def greet():
    print("-----------hai----------")
    yield
    print("-----------bye-----------")

class TestSample:
    def test_span(self):
        print("in test span")

def test_display():
    print("displaying the message")
