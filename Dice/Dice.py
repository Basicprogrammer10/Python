import random
s = int(input("How manny sides on the dice? "))
def roll(d):
    n = random.randint(1, d)
    print(n)
    a = input("Would you like to roll again (N-no, Y-yes): ")
    if a == "N":
        exit()
    else:
        roll(s)
roll(s)
