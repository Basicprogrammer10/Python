import random
from Color import *
file = open("Ideas/ideas.txt", "r")
lines = file.readlines()
#print("Lines:", lines)
f = open("Ideas/ideas.txt", "r").read()
g = f.split("\n")
#print("file.read:", f)
#print("f.split:", g)


def main():
    r = random.randint(0, len(g)-1)
    c = g[r]
    #print("C is", c)
    cprint(g[r], CYAN)
    x = input("Good Idea? ")
    if x == "Y":
        cprint(g[r], GREEN)
        file = open("ideas.txt", "w")
        file.seek(0)
        for i in range(len(g)-1):
            #print("I is", i)
            if i != c:
                file.write(g[i] + "\n")
        open("ideas.txt", "r+").truncate()
        exit()
    else:
        main()


main()
