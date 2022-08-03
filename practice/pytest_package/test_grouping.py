from pytest import mark

#############################################
#for batch execution --> pytest -vs
#to ignore any folder --> pytest --ignore=test_modulename.py -vs
#############################################

@mark.smoke
def test_validate_login():
    print('executing login test')

@mark.regression
def test_shopping():
    print('executing shopping test')

@mark.regression
def test_payment():
    print('executing payment test')

@mark.smoke
def test_registration():
    print('executing registration test')
