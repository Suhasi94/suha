from pytest import mark

@mark.smoke
def test_login_validate():##smoke
    print("executing login test")

@mark.regression
def test_shopping():    #regression
    print("executing test shopping")

@mark.regression
def test_payment():
    print("executing test payment")

@mark.smoke
def test_registration():
    print("executing test registration")

