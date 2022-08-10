
Grocery = list()
count_grocery = dict()

def main():
    while True:
        try:
            text = input("").upper().strip()
            if text not in count_grocery:
                Grocery.append(text)
                count_grocery[text] = 1
            else:
                count_grocery[text] += 1
        except EOFError:
            break

    print()
    # print(count_grocery)
    for i in sorted(Grocery):
        print(count_grocery[i], i)


if __name__ == "__main__":
    main()