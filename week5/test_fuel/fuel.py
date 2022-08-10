def main():

    text = input("Fraction: ")

    fraction = convert(text)

    percent = gauge(fraction)

    if percent.isnumeric():
        print(percent+"%")
    else:
        print(percent)


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError

        return round(100*x/y+40)
    # except ZeroDivisionError:
    #     main()
    # except ValueError:
    #     main()

def gauge(percentage):
    if percentage <= 10:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)


if __name__ == "__main__":
    main()