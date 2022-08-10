import csv
import sys
import tabulate

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

name = list(dict())
try:
    with open(sys.argv[1]) as file:
        row = csv.DictReader(file)

        for i in row:

            last_name, first_name = i["name"].split(", ")

            person = {
                "first": first_name, "last": last_name, "house": i["house"]
            }

            name.append(person)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2],'w') as file:

        Fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=Fieldnames)
        writer.writeheader()              # you got the fieldnames when you init the DictWriter and if you
                                          # want your csv file have header you just call writeheader
        for row in name:
            writer.writerow(row)