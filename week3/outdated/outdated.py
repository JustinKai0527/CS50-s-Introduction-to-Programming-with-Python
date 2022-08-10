
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():

    while True:

        try:
            date = input("Date: ").strip()

            if "/" in date:
                Month, day, year = date.split("/")
                Month = int(Month)
                day = int(day)
                year = int(year)

            else:
                Month = date[:date.index(" ")]
                Month = month.index(Month)+1
                # print(Month)

                day = date[date.index(" "):date.index(",")]
                day = int(day)
                # print(day)

                year = date[date.rindex(" "):]
                year = int(year)
                # print(year)

            if day > 31 or day < 0 or Month > 12 or Month < 0:
                    raise ValueError
            print(f"{year}-{Month:02}-{day:02}")
            break

        except ValueError:
            pass


if __name__ == "__main__":
    main()