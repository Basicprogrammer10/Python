import random
from Color import *
file = open("ideas.txt", "r")
lines = file.readlines()
print("Lines:", lines)
f = open("ideas.txt", "r").read()
g = f.split("\n")
print("file.read:", f)
print("f.split:", g)


def main():
    r = random.randint(0, len(g)-1)
    c = g[r]
    print("C is", c)
    print(g[r])
    x = input("Good Idea? ")
    if x == "Y":
        cprint(g[r], GREEN)
        file = open("ideas.txt", "w")
        file.seek(0)
        for i in range(len(g)-1):
            print("I is", i)
            if i != c:
                file.write(g[i])
        open("ideas.txt", "r+").truncate()
        exit()
    else:
        main()


main()
