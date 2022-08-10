from datetime import date, timedelta
import inflect
import re
import sys

# def main():
#     p = inflect.engine()
#     time = input("Date of Birth: ")
#     TIME = check_day(time)
#     past = date.fromisoformat(TIME)

#     nowadays = date.today()
#     delta = nowadays - past

#     words = p.number_to_words(int(delta.total_seconds()/60), andword="")

#     print(f"{words.capitalize()} minutes")


# def check_day(time):
#     if not re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",time):
#         sys.exit("Invalid date")

#     return time

def main():
    p = inflect.engine()
    time = input("Date of Birth: ")

    Time = check_day(time)
    if not Time:
        sys.exit("Invalid date")

    past = date.fromisoformat(Time)

    nowadays = date.today()
    delta = nowadays - past

    words = p.number_to_words(int(delta.total_seconds()/60), andword="")

    print(f"{words.capitalize()} minutes")


def check_day(time):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",time):
        return time

if __name__ == "__main__":
    main()