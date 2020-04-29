import random, easygui
filepre = "IdeaGen/"
def list(num):
    '''Creates a file with some Ideas!'''
    colors = []
    file = open(filepre + 'PGNouns.txt', 'r')
    noun = file.readlines()
    file.close()
    file = open(filepre + 'Verbs.txt', 'r')
    color = file.readlines()
    file.close()
    file = open(filepre + 'NewIdeas.txt', 'w')
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

def showideas():
    '''Shows all Ideas in "NewIdeas.txt"'''
    f = open("IdeaGen/NewIdeas.txt", "r")
    text = f.read()
    f.close()
    easygui.codebox(text)

def goodideas():
    colors = []
    num = int(input("How many Entrepreneur Opportunities would you like to make? "))
    file = open('IdeaGen/PGNouns.txt', 'r')
    noun = file.readlines()
    file.close()
    file = open('IdeaGen/Verbs.txt', 'r')
    color = file.readlines()
    file.close()
    file = open('IdeaGen/GoodishNewIdeas.txt', 'w')
    for i in range(num):
        word = str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)])
        if word not in colors:
            if input("Is\n"+word+" A Good Idea?") == "Y":
                file.write(word)
                colors.append(word)
                file.write("----------\n")
        else:
            i = i + 1
    file.write("Entrepreneur Opportunities Gen. V1 | By Connor Slade")
    file.close()
