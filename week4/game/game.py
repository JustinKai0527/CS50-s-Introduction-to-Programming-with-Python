import random

def get_level():
    while True:
        try:
            Range = int(input("Level: "))
            if Range < 1:
                raise ValueError
            return Range
        except ValueError:
            pass

def guess():
    while True:
        try:
            return int(input("Guess: "))
        except ValueError:
            pass

def main():

    Range = get_level()

    val = random.randint(1,Range)

    print(val)
    while True:
        guess_val = guess()
        if val == guess_val:
            print("Just right!")
            break
        elif val > guess_val:
            print("Too small!")
        else:
            print("Too large!")

if __name__ == "__main__":
    main()