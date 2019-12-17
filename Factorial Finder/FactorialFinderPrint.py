from Color import *
g = int(input("Do you want to print var a? (1 for yes, 2 for no): "))
def main1():
    a = int(input("Number: "))
    b = a
    c = a
    e = 0
    while b > 1:
        a = a * b
        b = b - 1
        cprint(a, RED)
        cprint(b, CYAN)
    f = c, "Factorial is", a
    cprint(f, GREEN)
    d = list(str(a))
    for i in range(len(d)):
        e = e + int(d[i])
    f = ("The sum of the digets in", a, "is", e)
    cprint(f, GREEN)
def main2():
    a = int(input("Number: "))
    b = a
    c = a
    e = 0
    while b > 1:
        a = a * b
        b = b - 1
        cprint(b, CYAN)
    f = c, "Factorial is", a
    cprint(f, GREEN)
    d = list(str(a))
    for i in range(len(d)):
        e = e + int(d[i])
    f = ("The sum of the digets in", a, "is", e)
    #cprint(f, GREEN)
if g == 1:
    main1()
else:
    main2()