import sys
from Color import *
file = open('PerfectNumbers.txt', 'w')
MN = int(input("Min: "))
MA = int(input("Max: "))
for x in range(MN,MA):
    a = []
    t = 0
    for i in range(1, x + 1):
        if x % i == 0:
            a.append(i)
    a.remove(x)
    for i in range(len(a)):
       t = t + a[i]
    if x == t:
        file.writelines(str(x))
        file.write("\n")
file.close()

file = open('PerfectNumbers.txt', 'r')
l = file.readlines()
color(GREEN)
print(l)