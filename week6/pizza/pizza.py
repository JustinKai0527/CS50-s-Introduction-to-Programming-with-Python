import csv
import sys
import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

try:
    table = list(list())
    with open(sys.argv[1]) as file:
        headers = file.readline().strip().split(",")    # list
        # print(headers)
        table_list = csv.reader(file)
        for i in table_list:
            table.append(i)
        # print(table)
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
# table = [["spam",42],["eggs",451],["bacon",0]]
# headers = ["item", "qty"]
# print(tabulate.tabulate(table, headers, tablefmt="plain"))