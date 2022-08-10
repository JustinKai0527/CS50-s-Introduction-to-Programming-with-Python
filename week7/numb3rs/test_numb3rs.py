from numb3rs import validate

def test_nothing():
    assert validate("") == False

def test_string():
    assert validate("cat.dog...") == False

def test_valueExceed():
    assert validate("1000.103.432.432") == False

def test_valuesmall():
    assert validate("-1.-1.-2.-2") == False

def test_correct():
    assert validate("15.52.15.255") == True

def test_first():
    assert validate("75.456.76.65") == False