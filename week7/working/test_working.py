from working import convert
import pytest

def test_incorrect_hours():
    with pytest.raises(ValueError):
        convert("13:00 AM to 14:00 PM")

def test_incorrect_minutes():
    with pytest.raises(ValueError):
        convert("11:61 AM to 10:78 PM")

def test_omit_to():
    with pytest.raises(ValueError):
        convert("11:12 AM  10:11 PM")

def test_check():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_invalie_format():
    with pytest.raises(ValueError):
        convert("cat dog to frog ox")
