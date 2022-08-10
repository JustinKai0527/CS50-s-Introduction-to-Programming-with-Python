
import fuel
import pytest

def test_Errors():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
    with pytest.raises(ValueError):
        fuel.convert("a/b")

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/1") == 100
    assert fuel.convert("1/3") == 33
    assert fuel.convert("0/1") == 0

def test_guage():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"