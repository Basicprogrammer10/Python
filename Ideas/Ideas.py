import random
from Color import *
file = open("ideas.txt", "r+")
f = file.read()
g = f.split("\n")
def main():
    r = random.randint(0, len(g)-1)
    print(g[r])
    x = input("Good Idea? ")
    if x == "Y":
        cprint(g[r], GREEN)
        for i in range(len(g)):
            if i != g[r]:
                f.seek(r)
                file.write('')
        f.truncate()
        exit()
    else:
        main()
main()