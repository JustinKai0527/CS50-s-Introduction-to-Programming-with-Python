import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if matches := re.search(r"([0-9]+):?([0-9]+)? (AM|PM) to ([0-9]+):?([0-9]+)? (PM|AM)", s):

        minute1 = 0
        if matches.group(2):
            if int(matches.group(2)) >= 60:
                raise ValueError
            else:
                minute1 = int(matches.group(2))

        minute2 = 0
        if matches.group(5):                               # it will get a val or None if don't have get
            if int(matches.group(5)) >= 60:
                raise ValueError
            else:
                minute2 = int(matches.group(5))

        hour1 = int(matches.group(1))
        hour2 = int(matches.group(4))
        if hour1 > 12 or hour2 > 12:
            raise ValueError

        if matches.group(3) == "PM":
            if hour1 != 12:
                hour1 = (hour1+12)
        elif hour1 == 12:
            hour1 = 0

        if matches.group(6) == "PM":
            if hour2 != 12:
                hour2 = (hour2+12)
        elif hour2 == 12:
            hour2 = 0


        # print(hour1)
        # print(hour2)
        # print(minute1)
        # print(minute2)

        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()