import random
import sys
from pyfiglet import Figlet


figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("input: ")
    f = random.choice(font_list)
    font = figlet.setFont(font=f)
    print(figlet.renderText(s))

elif len(sys.argv) == 3 and sys.argv[2] in font_list and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    s = input("input: ")
    f = sys.argv[2]
    font = figlet.setFont(font=f)
    print(figlet.renderText(s))

else:
    sys.exit("Invalid usage")


