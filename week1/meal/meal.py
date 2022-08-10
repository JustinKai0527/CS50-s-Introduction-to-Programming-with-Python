def main():
    time = input("What time is it? ").strip()

    val = convert(time)

    if 8 >= val >= 7:
        print("breakfast time")
    elif 13 >= val >= 12:
        print("lunch time")
    elif 19 >= val >= 18:
        print("dinner time")
    exit()

def convert(time):
    hours = float(time[:(time.index(":"))])
    minutes = float(time[(time.index(":")+1):])
    # 7:30 = 7.5      30/60.0
    return hours+minutes/60.0   #float


if __name__ == "__main__":
    main()