

def main():
    text = input("Input: ").strip()

    print("Ouput: ", end = "")
    print(shorten(text))

    exit()

def shorten(word):
    STR = ""
    for i in word:
        test = i                      # missing to change to lowercase vowel
        if not (test == 'a' or test == 'e' or test == 'i' or test == 'o' or test == 'u'):
            STR += i

    return STR


if __name__ == "__main__":
    main()