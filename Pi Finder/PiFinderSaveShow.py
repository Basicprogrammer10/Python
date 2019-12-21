from datetime import datetime
from Color import *
import decimal
file = open('Pi.txt', 'w')
file.write("Pi Finder V2\n")
file.write("Made By Connor Slade\n")
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
file.write("Finished at " + str(datetime.now()))
cprint(pi, GREEN)