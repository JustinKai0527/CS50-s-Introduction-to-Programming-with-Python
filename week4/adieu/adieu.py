
import inflect

text = list()

while True:
    try:
        name = input("name: ")
        text.append(name)
    except EOFError:
        break
print()

p = inflect.engine()
STR = p.join(text)

print("Adieu, adieu, to " + STR)