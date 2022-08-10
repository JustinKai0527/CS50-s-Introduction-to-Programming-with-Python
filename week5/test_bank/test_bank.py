from bank import value

def test_Hello():
    assert value("Hello") == 0

def test_Hello_Nweman():
    assert value("Hello, Newman") == 0

def test_how_you_doing():
    assert value("How you doing?") == 20

def test_what_happening():
    assert value("What's happening") == 100