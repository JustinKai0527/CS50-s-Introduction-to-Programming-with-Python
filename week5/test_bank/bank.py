

#if text have " " in the seperate
    # text = text[:text.index(" ")]

def main():
    text = input("Greeting: ").strip().lower()
    val = value(text)
    print(f"${val}")


def value(greeting):
    if "hello" in greeting:
        return 100
    elif greeting[0] == "h":
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()