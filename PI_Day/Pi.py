import os
os.system('cls' if os.name == 'nt' else 'clear')
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470"
digits  = 11
dig = digits + 1
playing = True
a = 0

while playing == True:
    guess = input()
    if guess == pi[a]:
        os.system('cls' if os.name == 'nt' else 'clear')
        a = a + 1
        for i in range(a):
            print('\033[32m' + pi[i], end="", flush=True)
        print()
    else:
        print('\033[31m' + "You Faild")
        print('\033[31m' + pi[a+1])
        break
    if a == dig:
        print('\033[33m' + "Nice Job: " + str(digits) + " Digits!")
        playing = False
    if a == len(pi):
        print('\033[33m' + "Nice Job: " + str(len(pi)-1) + " Digits!")
        playing = False