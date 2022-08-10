import random


def main():
    level = get_level()
    grade = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for i in range(3):
            try:
                val = int(input(f"{x} + {y} = "))
                if val == (x+y):
                    grade += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            if i == 2:                                                    #possible miss because range(3)
                print(f"{x} + {y} = {x+y}")                               #so you will think that will be i == 3

    print(f"Score: {grade}")


def get_level():
    while True:
        try:
            Range = int(input("Level: "))
            if Range not in [1,2,3]:
                raise ValueError
            return Range
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()