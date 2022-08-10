def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    # print(plate[:2])

def is_valid(s):
    
    if not(2 <= len(s) <= 6):
        return False
    elif not s[:2].isalpha():  #letters
        return False
    else:
        for i in s:
            if i.isnumeric():
                if not(s[s.index(i):].isnumeric() and i != "0"):
                    return False
                break

    return True

if __name__ == "__main__":
    main()