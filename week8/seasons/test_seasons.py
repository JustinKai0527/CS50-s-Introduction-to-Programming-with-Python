import seasons
import sys

def main():
    seasons.check_day()

def test_main():
    assert seasons.check_day("19999-01-1") == None
    assert seasons.check_day("1999-01-02") == ("1999-01-02")
    assert seasons.check_day("July-01-02") == None
    assert seasons.check_day("January 1, 02") == None

if __name__ == "__main__":
    main()