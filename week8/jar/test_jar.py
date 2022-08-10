from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(0)
    with pytest.raises(ValueError):
        jar = Jar(-10)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    with pytest.raises(ValueError):
        jar.withdraw(13)