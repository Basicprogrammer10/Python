from datetime import datetime
import decimal, sys
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


def cprint(text, color):
    '''Prints text to terminal in color'''
    sys.stdout.write(color)
    print(text)
    sys.stdout.write(RESET)


file = open('Pi.txt', 'w')
file.write("Pi Finder V2\n")
file.write("Made By Connor Slade\n")
start = datetime.now()


def pi():
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
        cprint(s, RED)
    decimal.getcontext().prec -= 2
    return +s               # unary plus applies the new precision


x = int(input("precision: "))
file.write("Precision: " + str(x) + "\n")
file.write("-------------------------\n")
decimal.getcontext().prec = x
pi = pi()
file.write(str(pi) + "\n")
file.write("-------------------------\n")
file.write("Started at " + str(start))
file.write("Finished at " + str(datetime.now()))
cprint(pi, GREEN)
