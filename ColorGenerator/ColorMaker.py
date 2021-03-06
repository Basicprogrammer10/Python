import random
colors = []
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    if iteration == total: 
        print()
num = int(input("How many Color Names would you like to make? "))
file = open('ColorGenerator/Nouns.txt', 'r')
noun = file.readlines()
file.close()
file = open('ColorGenerator/Colors.txt', 'r')
color = file.readlines()
file.close()
file = open('ColorGenerator/NewColors.txt', 'w')
for i in range(num):
    word = str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)])
    if word not in colors:
        file.write(word)
        colors.append(word)
        file.write("----------\n")
    else:
        i = i + 1
    printProgressBar(i, num)
file.write("Color Name Gen. V2 | By Connor Slade")
file.close()