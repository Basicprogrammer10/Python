import sys
from Color import *
file = open('PerfectNumber.txt', 'w')
file.write("Perfect Number Finder V3\n")
file.write("Made By Connor Slade\n")
file.write("-------------------------\n")
file.close()
MN = int(input("Min: "))
MA = int(input("Max: "))
for x in range(MN, MA):
    a = []
    t = 0
    for i in range(1, x + 1):
        if x % i == 0:
            a.append(i)
    a.remove(x)
    for i in range(len(a)):
        t = t + a[i]
    if x == t:
        file = open('PerfectNumber.txt', 'a')
        file.writelines(str(x))
        file.write("\n")
        file.close()

file = open('PerfectNumber.txt', 'r')
l = file.readlines()
l.remove("Perfect Number Finder V3\n")
l.remove("Made By Connor Slade\n")
l.remove("-------------------------\n")
cprint(l, GREEN)
