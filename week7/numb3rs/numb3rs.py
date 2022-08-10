import re
import sys

def main():
    print(validate(input("IPv4 Adddress: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):   # :=  walrus operator
        for i in range(4):
            if not (255 >= int(matches.group(i+1)) >= 0):
                return False
        return True
    return False


if __name__ == "__main__":
    main()