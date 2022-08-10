
import sys
from pyfiglet import Figlet
import random

if len(sys.argv) > 1:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")

figlet = Figlet()
Fig_list = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[2] not in Fig_list:
        sys.exit("Invalid usage")

text = input()

s = random.choice(Fig_list)
# print(s)
if len(sys.argv) == 3:
    s = sys.argv[2]
    # print(s)
    # if s in Fig_list:
        # print(s)

figlet.setFont(font = s)

print(figlet.renderText(text))