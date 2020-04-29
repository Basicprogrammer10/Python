import random, easygui, sys
from configparser import ConfigParser

def list(num):
    '''Creates a file with some Ideas!'''
    colors = []
    file = open(filepre + NounFile, 'r')
    noun = file.readlines()
    file.close()

    file = open(filepre + VerbFile, 'r')
    color = file.readlines()
    file.close()

    file = open(filepre + NewIdeaFile, 'w')

    for i in range(num):
        word = str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)])
        if word not in colors:
            file.write(word)
            colors.append(word)
            file.write("----------\n")
        else:
            i = i + 1
    file.write("Entrepreneur Opportunities Gen. V1 | By Connor Slade")
    file.close()

def showideas(file, title):
    '''Shows all Ideas in "NewIdeas.txt"'''
    try:
        f = open(filepre + file, "r")
        text = f.read()
        f.close()
        easygui.codebox(text)
    except:
        error("You Must First Create a Idea List!")

def goodideas(num):
    '''Does some Nosetastic Stuff!!'''
    colors = []
    file = open(filepre + NounFile, 'r')
    noun = file.readlines()
    file.close()

    file = open(filepre + VerbFile, 'r')
    color = file.readlines()
    file.close()

    file = open(filepre + GoodIdeaFile, 'w')

    choices = ["Yes", "No", "Exit"]
    for i in range(num):
        word = str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)])
        if word not in colors:
            opt = easygui.buttonbox("Is\n"+word+"A Good Idea?", choices=choices)
            if opt == "Yes":
                file.write(word)
                colors.append(word)
                file.write("----------\n")
        elif opt == "Exit":
            pass
        else:
            i = i + 1
        if opt == "Exit":
            break
    file.write("Entrepreneur Opportunities Gen. V1 | By Connor Slade")
    file.close()

def about():
    '''Info About Me!'''
    easygui.msgbox("This Entrepreneur Opportunities Gen was made by Connor Slade!\nEmail: connor@connorcode.com\nSorry for the Win95 UI", "Error")

def error(message):
    '''Error Message lol'''
    easygui.msgbox(message, "Error")

try:
    config = ConfigParser()
    config.read('V:\Programming\Python\IdeaGen\EXE\Config.ini')
    filepre = config.get("Setup", "filepre")
    NounFile = config.get("File", "NounFile")
    VerbFile = config.get("File", "VerbFile")
    NewIdeaFile = config.get("File", "NewIdeaFile")
    GoodIdeaFile = config.get("File", "GoodIdeaFile")
    print(NounFile)
except:
    error("Error Reading Config File")

while True:
    choices = ["List", "Good Ideas", "Show Ideas", "About", "Quit"]
    opt = easygui.buttonbox("Chose an option", choices=choices)
    if opt == "Quit":
        quit()
    elif opt == "List":
        try:
            num = int(easygui.enterbox(msg="How many Entrepreneur Opportunities would you like to make?"))
            list(num)
        except:
            error("You can only input numbers.")
            pass
    elif opt == "Show Ideas":
        choices = ["New Ideas", "Good New Ideas"]
        opt = easygui.buttonbox("Chose an option", choices=choices)
        if opt == "New Ideas":
            showideas(filepre + NewIdeaFile, "New Ideas")
        elif opt == "Good New Ideas":
            showideas(filepre + GoodIdeaFile,  "Good New Ideas")
    elif opt == "Good Ideas":
        try:
            num = int(easygui.enterbox(msg="How many Entrepreneur Opportunities would you like to Look at?"))
            goodideas(num)
        except:
            error("You can only input numbers.")
            pass
    elif opt == "About":
        about()
    else:
        quit()