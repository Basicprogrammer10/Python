
import random
def win():
        print(" __     __          __          ___       ")
        print(" \ \   / /          \ \        / (_)      ")
        print("  \ \_/ ___  _   _   \ \  /\  / / _ _ __  ")
        print("   \   / _ \| | | |   \ \/  \/ / | | '_ \ ")
        print("    | | (_) | |_| |    \  /\  /  | | | | |")
        print("    |_|\___/ \__,_|     \/  \/   |_|_| |_|")
        c = input("Do You Want to keep playing? (y/n) ")
        if (str(c) == "n"):
                quit()
        elif (str(c) == "c"):
                allrun()
        else :
            all()

def allrun() :
    def Game():
            g = input("Enter Your Guess: ")
            try:
                     int(g)
            except ValueError:
                    print("Enter a Number From 1 To 1000")
                    Game()

            if (int(g)==int(n)):
                    win()
            elif (int(g)>int(n)):
                    print("The Number is Smaller Than " + str(g))
                    Game()
            elif (int(g)<int(n)):
                    print("The Number is Bigger Than " + str(g))
                    Game()
    n=random.randint(1,1000)
    int(n)
    print(" __          __  _                            _______   ")
    print(" \ \        / / | |                          |__   __|  ")
    print("  \ \  /\  / ___| | ___ ___  _ __ ___   ___     | | ___ ")
    print("   \ \/  \/ / _ | |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \ ")
    print("    \  /\  |  __| | (_| (_) | | | | | |  __/    | | (_) |")
    print("     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/ ")
    print("             The Number Guessing Game V1.2 By:Connor")
    print("")
    Game()
allrun()
def all():
        def Game():
                g = input("Enter Your Guess: ")
                try:
                         int(g)
                except ValueError:
                        print("Enter a Number From 1 To 1000")
                        Game()

                if (int(g)==int(n)):
                        win()
                elif (int(g)>int(n)):
                        print("The Number is Smaller Than " + str(g))
                        Game()
                elif (int(g)<int(n)):
                        print("The Number is Bigger Than " + str(g))
                        Game()
        n=random.randint(1,1000)
        int(n)
        print(" __          __  _                            _______   ")
        print(" \ \        / / | |                          |__   __|  ")
        print("  \ \  /\  / ___| | ___ ___  _ __ ___   ___     | | ___ ")
        print("   \ \/  \/ / _ | |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \ ")
        print("    \  /\  |  __| | (_| (_) | | | | | |  __/    | | (_) |")
        print("     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/ ")
        print("             The Number Guessing Game V1.1 By:Connor")
        print(n)
        Game()
all()
