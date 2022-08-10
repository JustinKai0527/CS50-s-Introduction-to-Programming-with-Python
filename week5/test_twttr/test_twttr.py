from twttr import shorten

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("!!!!") == "!!!!"


def test_lowercase():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("aeiou") == ""


def test_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("AEIOU") == ""


def test_novowels():
    assert shorten("tst n vwls") == "tst n vwls"