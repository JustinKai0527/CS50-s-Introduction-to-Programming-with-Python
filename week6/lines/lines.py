import sys


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

count = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.lstrip()
            if line != "":
                if line[0] != "#":
                    count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(count)