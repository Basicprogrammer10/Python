#   ©ConnorSlade 2020
import argparse
import sys
import re
import math
from random import randint, shuffle
ver = 3.12
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
hi = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text", required=False,
                help="The Text (EX: -t 'KHOOR ZRUOG')")
ap.add_argument("-f", "--file", required=False,
                help="File name to output to. (EX: -t 'KHOOR ZRUOG' -f 'text')")
ap.add_argument("-d", "--duck", required=False,
                help="Searches Duckduckgo! (EX: -d 'Nose')")
ap.add_argument("-nose", "--nose", required=False,
                help="NOSE! (EX: -n')", action='store_true')
ap.add_argument("-v", "--version", required=False,
                help="Displays Version INFO (EX: -v')", action='store_true')
ap.add_argument("-u", "--unmix", required=False,
                help="Un Mix a Word (EX: -u estt')")
args = vars(ap.parse_args())


def colored(text, color):
    code = 'ERROR'
    if color == 'blue':
        code = '\033[34m'
    elif color == 'yellow':
        code = '\033[33m'
    elif color == 'cyan':
        code = '\033[36m'
    elif color == 'magenta':
        code = '\033[35m'
    elif color == 'red':
        code = '\033[31m'
    elif color == 'green':
        code = '\033[32m'
    elif color == 'reset':
        code = '\033[0m'

    return code + text + "\033[0m"


if args["version"] != False:
    print(colored("BrainChaseSolver™", 'blue') + " | " + colored("V" +
                                                                 str(ver), 'yellow') + " | " + colored("By: Connor Slade", 'green'))

elif args["duck"] != None:
    print(colored("https://duckduckgo.com/?q=" + args["duck"], 'cyan'))

elif args["nose"] != False:
    print(colored("^..^      /\n/_/\_____/\n   /\   /\\\n  /  \ /  \\", 'yellow'))

elif args["unmix"] != None:
    try:
        try:
            string = args["unmix"].lower()
            words = input("Word File: ")
            wordfile = open(words, 'r')
            wordlines = wordfile.readlines()
            formatwords = []
            print(
                colored("Reformatting Word Database (This may take some time...)", 'yellow'))
            for i in range(len(wordlines)):
                formatwords.append(str(wordlines[i])[:-2])
            print(colored("Done Reformatting Word Database", 'green'))
            running = True
            shuffleld = []

            def shuffle_word(word):
                word = list(word)
                shuffle(word)
                return ''.join(word)
            print(colored("Shuffleing Words... (This may take some Time)", 'yellow'))
            c = 0
            while running:
                c = c + 1
                working = shuffle_word(string)
                if working not in shuffleld:
                    shuffleld.append(working)
                if len(shuffleld) == math.factorial(len(string)) or c >= len(formatwords):
                    running = False
            print(colored("Done Shuffleing Words...", 'green'))
            workingarray = []
            for i in range(len(shuffleld)):
                print(colored("Checking ", 'cyan') + colored("#" + str(i),
                                                             'magenta') + " | " + colored(shuffleld[i], 'blue'))
                for b in range(len(formatwords)):
                    if str(shuffleld[i]) in str(formatwords[b]):
                        if len(str(formatwords[b])) <= len(str(shuffleld[i])):
                            if str(formatwords[b]) not in workingarray:
                                workingarray.append(str(formatwords[b]))
                                print(colored("    >", 'green') +
                                      colored(str(formatwords[b]), 'blue'))
        except KeyboardInterrupt:
            pass
    except:
        try:
            string = user[1].lower()
            running = True
            shuffleld = []

            def shuffle_word(word):
                word = list(word)
                shuffle(word)
                return ''.join(word)

            while running:
                working = shuffle_word(string)
                if working not in shuffleld:
                    shuffleld.append(working)
                if len(shuffleld) == math.factorial(len(string)):
                    running = False
            for i in range(len(shuffleld)):
                print("#" + str(i) + " | " + shuffleld[i])
        except KeyboardInterrupt:
            pass
        except IndexError:
            print(colored("You Must Supply Text To unscramble", 'red'))

elif args["text"] != None:
    if args["file"] != None:
        file = open(args["file"]+'.txt', 'a')
        DoFile = True
    else:
        DoFile = False
    encrypted_text = args["text"]
    for i in range(26):
        shift = i
        plain_text = ""
        for c in encrypted_text:
            if c in low:
                done = []
                final = ''
                for i in c:
                    done.append(hi[low.index(i)])
                for i in done:
                    final = final + i
                b = final
            else:
                b = c
            if b.isupper():
                c_unicode = ord(b)
                c_index = ord(b) - ord("A")
                new_index = (c_index - shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                plain_text = plain_text + new_character
            else:
                plain_text += c

        if shift < 10:
            print(colored("Shift: 0" + str(shift), 'magenta') +
                  colored(" | ", 'white') + colored(plain_text, 'blue'))
        else:
            print(colored("Shift: " + str(shift), 'magenta') +
                  colored(" | ", 'white') + colored(plain_text, 'blue'))
        if DoFile == True:
            if shift < 10:
                file.write("Shift: 0" + str(shift) + " " + plain_text + "\n")
            else:
                file.write("Shift: " + str(shift) + " " + plain_text + "\n")
else:
    print(colored("You have entered the BrainChaseSolver™ Shell", "blue") +
          colored("\nType `exit` to exit\nType `help` for help\n", 'green'))
    while True:
        userin = input("\033[92m" + ">>> " + "\x1b[0m")
        PATTERN = re.compile(r'''((?:[^;"']|"[^"]*"|'[^']*')+)''')
        user = PATTERN.split(userin)[1::2]
        command = user[0].lower()

        if command == 'version':
            print(colored("BrainChaseSolver™", 'blue') + " | " + colored("V" +
                                                                         str(ver), 'yellow') + " | " + colored("By: Connor Slade", 'green'))

        elif command == 'help':
            print(colored("Debug         Lets you run code               ;CodeToRun\nDecode        Decodes Caesar ciphers          ;Text;File\nDuck          Duckduckgos Somthing            ;CuteTurtle\nExit          Exits the Shell\nHelp          Shows this nice mesage\nNose          Noses you\nUnmix         Unmixes a string                ;String;Auto\nVersion       Gives you Version Info", 'blue'))

        elif command == 'duck':
            try:
                print(colored("https://duckduckgo.com/?q=" + user[1], 'cyan'))
            except IndexError:
                print(colored("You Must Supply a Search Term", 'red'))

        elif command == 'nose':
            print(colored("^..^      /\n/_/\_____/\n   /\   /\\\n  /  \ /  \\", 'yellow'))

        elif command == 'debug':
            try:
                exec(user[1])
            except IndexError:
                print(colored("You Must Supply a Command", 'red'))
            except SyntaxError as e:
                print(colored(e, 'cyan'))
        elif command == 'unmix':
            try:
                try:
                    string = user[1].lower()
                    words = user[2]
                    wordfile = open(words, 'r')
                    wordlines = wordfile.readlines()
                    formatwords = []
                    print(
                        colored("Reformatting Word Database (This may take some time...)", 'yellow'))
                    for i in range(len(wordlines)):
                        formatwords.append(str(wordlines[i])[:-2])
                    print(colored("Done Reformatting Word Database", 'green'))
                    running = True
                    shuffleld = []

                    def shuffle_word(word):
                        word = list(word)
                        shuffle(word)
                        return ''.join(word)
                    print(
                        colored("Shuffleing Words... (This may take some Time)", 'yellow'))
                    c = 0
                    while running:
                        c = c + 1
                        working = shuffle_word(string)
                        if working not in shuffleld:
                            shuffleld.append(working)
                        if len(shuffleld) == math.factorial(len(string)) or c >= len(formatwords):
                            running = False
                    print(colored("Done Shuffleing Words...", 'green'))
                    workingarray = []
                    for i in range(len(shuffleld)):
                        print(colored("Checking ", 'cyan') + colored("#" + str(i),
                                                                     'magenta') + " | " + colored(shuffleld[i], 'blue'))
                        for b in range(len(formatwords)):
                            if str(shuffleld[i]) in str(formatwords[b]):
                                if len(str(formatwords[b])) <= len(str(shuffleld[i])):
                                    if str(formatwords[b]) not in workingarray:
                                        workingarray.append(
                                            str(formatwords[b]))
                                        print(colored("    >", 'green') +
                                              colored(str(formatwords[b]), 'blue'))
                    for d in workingarray:
                        print(colored(str(d), 'green') + " | ", end="")
                    print("\n")

                except KeyboardInterrupt:
                    pass
            except:
                try:
                    string = user[1]
                    string = string.lower()
                    running = True
                    shuffleld = []

                    def shuffle_word(word):
                        word = list(word)
                        shuffle(word)
                        return ''.join(word)

                    while running:
                        working = shuffle_word(string)
                        if working not in shuffleld:
                            shuffleld.append(working)
                        if len(shuffleld) == math.factorial(len(string)):
                            running = False
                    for i in range(len(shuffleld)):
                        print("#" + str(i) + " | " + shuffleld[i])
                except KeyboardInterrupt:
                    pass
                except IndexError:
                    print(colored("You Must Supply Text To unscramble", 'red'))

        elif command == 'decode':
            try:
                try:
                    if user[1] != None:
                        file = open(args["file"]+'.txt', 'a')
                        DoFile = True
                    else:
                        DoFile = False
                except:
                    DoFile = False
                encrypted_text = user[1]
                for i in range(26):
                    shift = i
                    plain_text = ""
                    for c in encrypted_text:
                        if c in low:
                            done = []
                            final = ''
                            for i in c:
                                done.append(hi[low.index(i)])
                            for i in done:
                                final = final + i
                            b = final
                        else:
                            b = c
                        if b.isupper():
                            c_unicode = ord(b)
                            c_index = ord(b) - ord("A")
                            new_index = (c_index - shift) % 26
                            new_unicode = new_index + ord("A")
                            new_character = chr(new_unicode)
                            plain_text = plain_text + new_character
                        else:
                            plain_text += c

                    if shift < 10:
                        print(colored("Shift: 0" + str(shift), 'magenta') +
                              " | " + colored(plain_text, 'blue'))
                    else:
                        print(colored("Shift: " + str(shift), 'magenta') +
                              " | " + colored(plain_text, 'blue'))
                    if DoFile == True:
                        if shift < 10:
                            file.write("Shift: 0" + str(shift) +
                                       " " + plain_text + "\n")
                        else:
                            file.write("Shift: " + str(shift) +
                                       " " + plain_text + "\n")
            except IndexError:
                print(colored("You Must Supply a Command", 'red'))
        elif command == 'exit':
            print(colored("Exiting...", 'red'))
            exit()
        else:
            print(colored("Unknown Command", 'red'))
