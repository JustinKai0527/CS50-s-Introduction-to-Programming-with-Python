def main()
    while True:
        try:
            text = input("Fraction: ")
            x, y = text.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError

            if x > y:
                raise ValueError

            fraction = round(100*x/y)

            if fraction <= 1:
                print("E")
            elif fraction >= 99:
                print("F")
            else:
                print(f"{fraction}%")
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()