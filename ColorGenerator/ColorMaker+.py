import random, tqdm
colors = []
num = int(input("How many Color Names would you like to make? "))
file = open('ColorGenerator/Nouns.txt', 'r')
noun = file.readlines()
file.close()
file = open('ColorGenerator/Colors.txt', 'r')
color = file.readlines()
file.close()
file = open('ColorGenerator/NewColors.txt', 'w')
for i in tqdm(range(num)):
    word = str(noun[random.randint(0,len(noun)-1)]) + str(color[random.randint(0,len(color)-1)])
    if word not in colors:
        file.write(word)
        colors.append(word)
        file.write("----------\n")
    else:
        i = i + 1
file.write("Color Name Gen. V2 | By Connor Slade")
file.close()